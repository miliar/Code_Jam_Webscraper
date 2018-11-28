#include <iostream>
using namespace std;

static const int UNIT_SIZE = 10000;
static const int UNIT_WIDTH = 4;
static const int MAX_UNIT_NUM = 100 / UNIT_WIDTH;
static const int POWER10[UNIT_WIDTH] = {1, 10, 100, 1000};

struct BigInt
{
    int sign;
    int size;
    int digit[MAX_UNIT_NUM];

    BigInt()
    {
        sign = 0;
        size = 0;
        memset(digit, 0, MAX_UNIT_NUM * sizeof(int));
    }

    BigInt(int n)
    {
        sign = sgn(n);
        n *= sgn(n);
        size = 0;
        memset(digit, 0, MAX_UNIT_NUM * sizeof(int));
        while (n > 0)
        {
            digit[size++] = n % UNIT_SIZE;
            n /= UNIT_SIZE;
        }
        normalize();
    }

    BigInt(const char s[])
    {
        const char* p = s;
        const char* q = s + strlen(s);
        sign = 1;
        if (*p == '-')
            sign = -1;
        while (!isdigit(*p))
            p++;
        size = (int) (q - p + UNIT_WIDTH - 1) / UNIT_WIDTH;
        memset(digit, 0, MAX_UNIT_NUM * sizeof(int));
        for (int i = 0; p != q--; i++)
            digit[i / UNIT_WIDTH] += (*q - '0') * POWER10[i % UNIT_WIDTH];
        normalize();
    }

    BigInt(const string& s)
    {
        operator=(BigInt(s.data()));
    }

    BigInt(const BigInt& n)
    {
        sign = n.sign;
        size = n.size;
        memmove(digit, n.digit, MAX_UNIT_NUM * sizeof(int));
    }

    ~BigInt()
    {
    }

    static int sgn(const int n)
    {
        if (n > 0)
            return 1;
        else if (n < 0)
            return -1;
        else
            return 0;
    }

    static int sgn(const BigInt& n)
    {
        return n.sign;
    }

    int getSize() const
    {
        return size;
    }

    int getSign() const
    {
        return sign;
    }

    const BigInt& operator=(int n)
    {
        operator=(BigInt(n));
        return *this;
    }

    const BigInt& operator=(const BigInt& n)
    {
        if (this != &n)
        {
            sign = n.sign;
            size = n.size;
            memmove(digit, n.digit, MAX_UNIT_NUM * sizeof(int));
        }
        return *this;
    }
    
    int compareTo(const BigInt& n) const
    {
        if (sign != n.sign)
            return sign - n.sign;
        if (size != n.size)
            return sign * (size - n.size);
        if (size == 0)
            return 0;
        int i = size - 1;
        while (i > 0 && digit[i] == n.digit[i])
            i--;
        return sign * (digit[i] - n.digit[i]);
    }

    void normalize()
    {
        while (size > 0 && digit[size - 1] == 0)
            size--;
        if (size == 0)
            sign = 0;
    }

    int toInt() const
    {
        int remain = 0;
        for (int i = size - 1; i >= 0; i--)
            remain = remain * UNIT_SIZE + digit[i];
        return remain;
    }

    string toString() const
    {
        if (sign == 0)
            return string("0");
        char format[8];
        sprintf(format, "\%%.%dd", UNIT_WIDTH);
        char buffer[8];
        sprintf(buffer, "%d", digit[size - 1] * sign);
        string result(buffer);
        for (int i = size - 2; i >= 0; i--)
        {
            sprintf(buffer, format, digit[i]);
            result += buffer;
        }
        return result;
    }

    char* toCharArray(char* output) const
    {
        if (sign == 0)
        {
            output = "0";
            return output;
        }
        char format[8];
        sprintf(format, "\%%.%dd", UNIT_WIDTH);
        sprintf(output, "%d", digit[size - 1] * sign);
        char* offset = output + strlen(output);
        for (int i = size - 1; i >= 0; i--)
        {
            sprintf(offset, format, digit[i]);
            while (*offset) offset++;
        }
        return output;
    }

    int unsignedCompareTo(const BigInt& n) const
    {
        if (size != n.size)
            return size - n.size;
        if (size == 0)
            return 0;
        int i = size - 1;
        while (i > 0 && digit[i] == n.digit[i])
            i--;
        return digit[i] - n.digit[i];
    }

    void unsignedAdd(const BigInt& n)
    {
        int carry = 0;
        for (int i = 0; i < n.size || carry > 0; i++)
        {
            carry += digit[i];
            if (i < n.size)
                carry += n.digit[i];
            if (carry < UNIT_SIZE)
                digit[i] = carry;
            else
                digit[i] = carry - UNIT_SIZE;
            carry = (carry >= UNIT_SIZE);
            if (i + 1 > size) size = i + 1;
        }
        normalize();
    }

    void unsignedSubtract(const BigInt& n) //*this >= n
    {
        int carry = 0;
        for (int i = 0; i < n.size || carry < 0; i++)
        {
            carry += digit[i];
            if (i < n.size)
                carry -= n.digit[i];
            if (carry >= 0)
                digit[i] = carry;
            else
                digit[i] = carry + UNIT_SIZE;
            carry = -(carry < 0);
        }
        normalize();
    }

    void unsignedReverseSubtract(const BigInt& n) //*this <= n
    {
        int carry = 0;
        for (int i = 0; i < n.size; i++)
        {
            carry += n.digit[i];
            if (i < size)
                carry -= digit[i];
            if (carry >= 0)
                digit[i] = carry;
            else
                digit[i] = carry + UNIT_SIZE;
            carry = -(carry < 0);
        }
        size = n.size;
        normalize();
    }

    BigInt operator-() const
    {
        BigInt result(*this);
        result.sign *= -1;
        return result;
    }

    BigInt operator+(int n) const
    {
        return BigInt(*this).operator+=(n);
    }

    const BigInt& operator+=(int n)
    {
        return operator+=(BigInt(n));
    }

    BigInt operator+(const BigInt& n) const
    {
        return BigInt(*this).operator+=(n);
    }

    const BigInt& operator+=(const BigInt& n)
    {
        if (sgn(n) == 0)
            return *this;
        if (sign == 0)
            return operator=(n);
        if (sign == sgn(n))
            unsignedAdd(n);
        else
        {
            int cmp = unsignedCompareTo(n);
            if (cmp >= 0)
                unsignedSubtract(n);
            else
            {
                unsignedReverseSubtract(n);
                sign *= -1;
            }
        }
        normalize();
        return *this;
    }

    BigInt operator-(int n) const
    {
        return BigInt(*this).operator-=(n);
    }

    const BigInt& operator-=(int n)
    {
        return operator-=(BigInt(n));
    }

    BigInt operator-(const BigInt& n) const
    {
        return BigInt(*this).operator-=(n);
    }

    const BigInt& operator-=(const BigInt& n)
    {
        if (sgn(n) == 0)
            return *this;
        if (sign == 0)
        {
            operator=(n);
            sign *= -1;
            return *this;
        }
        if (sign != sgn(n))
            unsignedAdd(n);
        else
        {
            int cmp = unsignedCompareTo(n);
            if (cmp >= 0)
                unsignedSubtract(n);
            else
            {
                unsignedReverseSubtract(n);
                sign *= -1;
            }
        }
        normalize();
        return *this;
    }

    BigInt operator*(int n) const
    {
        return BigInt(*this).operator*=(n);
    }

    const BigInt& operator*=(int n)
    {
        sign *= sgn(n);
        n *= sgn(n);
        int carry = 0;
        for (int i = 0; i < size || carry > 0; i++)
        {
            carry += digit[i] * n;
            digit[i] = carry % UNIT_SIZE;
            carry /= UNIT_SIZE;
            if (i + 1 > size) size = i + 1;
        }
        normalize();
        return *this;
    }

    BigInt operator*(const BigInt& n) const
    {
        BigInt result;
        result.size = size + n.size;
        result.sign = sign * n.sign;
        for (int i = 0; i < size; i++)
            for (int j = 0; j < n.size; j++)
            {
                result.digit[i + j] += digit[i] * n.digit[j];
                result.digit[i + j + 1] += result.digit[i + j] / UNIT_SIZE;
                result.digit[i + j] %= UNIT_SIZE;
            }
        result.normalize();
        return result;
    }

    const BigInt& operator*=(const BigInt& n)
    {
        return operator=(operator*(n));
    }

    BigInt operator/(int n) const
    {
        return BigInt(*this).operator/=(n);
    }

    const BigInt& operator/=(int n)
    {
        if (n == 0)
            n /= n; //force a divide-zero crash
        sign *= sgn(n);
        n *= sgn(n);
        int remain = 0;
        for (int i = size - 1; i >= 0; i--)
        {
            remain = remain * UNIT_SIZE + digit[i];
            digit[i] = remain / n;
            remain %= n;
        }
        normalize();
        return *this;
    }

    int binarySearchQuotient(const BigInt& n)
    {
        int left = 0, right = UNIT_SIZE - 1;
        while (left < right)
        {
            int mid = (left + right + 1) / 2;
            if (operator>=(n.operator*(mid * n.sign)))
                left = mid;
            else
                right = mid - 1;
        }
        return left;
    }
    
    //n^2logUNIT_SIZE
    void divide(const BigInt& n, BigInt& result, BigInt& remain) const
    {
        if (n.operator==(0))
        {
            int t = n.sign; //force a divide-zero crash
            t /= t;
        }
        if (unsignedCompareTo(n) < 0)
        {
            result = BigInt(0);
            remain = *this;
            return;
        }
        result = BigInt();
        remain = BigInt();
        remain.size = n.size - 1;
        memmove(remain.digit, digit + size - remain.size, remain.size * sizeof(int));
        for (int i = size - n.size; i >= 0; i--)
        {
            memmove(remain.digit + 1, remain.digit, remain.size * sizeof(int));
            remain.digit[0] = digit[i];
            remain.size++;
            remain.sign = 1;
            remain.normalize();
            result.digit[i] = remain.binarySearchQuotient(n);
            remain.operator-=(n.operator*(result.digit[i] * n.sign));
        }
        result.size = size - n.size + 1;
        result.sign = sign * n.sign;
        remain.sign = sign;
        result.normalize();
        remain.normalize();
    }

    BigInt operator/(const BigInt& n) const
    {
        BigInt result, remain;
        divide(n, result, remain);
        return result;
    }
    
    const BigInt& operator/=(const BigInt& n)
    {
        return operator=(operator/(n));
    }

    int operator%(int n) const
    {
        if (n == 0)
            n /= n; //force a divide-zero crash
        int remain = 0;
        for (int i = size - 1; i >= 0; i--)
        {
            remain = remain * UNIT_SIZE + digit[i];
            remain %= n;
        }
        return remain * sign;
    }

    const BigInt& operator%=(int n)
    {
        return operator=(operator%(n));
    }

    BigInt operator%(const BigInt& n) const
    {
        BigInt result, remain;
        divide(n, result, remain);
        return remain;
    }

    const BigInt& operator%=(const BigInt& n)
    {
        return operator=(operator%(n));
    }

    bool operator<(int n) const
    {
        return compareTo(BigInt(n)) < 0;
    }

    bool operator>(int n) const
    {
        return compareTo(BigInt(n)) > 0;
    }

    bool operator<=(int n) const
    {
        return compareTo(BigInt(n)) <= 0;
    }

    bool operator>=(int n) const
    {
        return compareTo(BigInt(n)) >= 0;
    }

    bool operator==(int n) const
    {
        return compareTo(BigInt(n)) == 0;
    }

    bool operator!=(int n) const
    {
        return compareTo(BigInt(n)) != 0;
    }

    bool operator<(const BigInt& n) const
    {
        return compareTo(n) < 0;
    }

    bool operator>(const BigInt& n) const
    {
        return compareTo(n) > 0;
    }

    bool operator<=(const BigInt& n) const
    {
        return compareTo(n) <= 0;
    }

    bool operator>=(const BigInt& n) const
    {
        return compareTo(n) >= 0;
    }

    bool operator==(const BigInt& n) const
    {
        return compareTo(n) == 0;
    }

    bool operator!=(const BigInt& n) const
    {
        return compareTo(n) != 0;
    }

    friend istream& operator>>(istream& in, BigInt& n)
    {
        string s;
        in >> s;
        n = BigInt(s);
        return in;
    }

    friend ostream& operator<<(ostream& out, const BigInt& n)
    {
        return out << n.toString();
    }

    friend BigInt operator+(int m, const BigInt& n)
    {
        return n.operator+(m);
    }

    friend BigInt operator-(int m, const BigInt& n)
    {
        return n.operator-().operator+(m);
    }

    friend BigInt operator*(int m, const BigInt& n)
    {
        return n.operator*(m);
    }

    friend BigInt operator/(int m, const BigInt& n)
    {
        return BigInt(m).operator/(n);
    }

    friend BigInt operator%(int m, const BigInt& n)
    {
        return BigInt(m).operator%(n);
    }
};

BigInt gcd(BigInt a, BigInt b)
{
    if (b == 0)
        return a;
    else
        return gcd(b, a % b);
}

int n,m,c,x,i;
BigInt a,b,t,d;
BigInt g,s;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	cin >> c;
	for (x=1; x<=c; x++)
	{
		cin >> n;
		cin >> d >> a;		
		g=d-a;
		if (g<0) g=-g;			
		for (i=2; i<n; i++)
		{
			cin >> b;
			t=b-a; if (t<0) t=-t;			
			g=gcd(g,t);
			a=b;
		}		
		s=(d/g)*g;
		if (s<d) s+=g;
		cout << "Case #" << x << ": " << s-d << endl;
	}
//	system("pause");
    return 0;
}
