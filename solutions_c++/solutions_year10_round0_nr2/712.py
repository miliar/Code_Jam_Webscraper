#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <cmath>
using namespace std;

class BigInteger
{
  public:
    const static int BASE = 10;

    vector<int> digits;

    /** The Big Integer's digits */
    inline int size() const { return digits.size(); }

    /** Constructors */
    BigInteger() { (*this) = 0; }
    BigInteger(int init) { (*this) = init; }
    BigInteger(const string & str) { (*this) = str; }
    BigInteger(const BigInteger & other) { digits = other.digits; }

    /** IO operation */
    friend ostream & operator << (ostream & out, const BigInteger &x);
    friend istream & operator >> (istream & in, BigInteger & x);

    /** Assignment operatoion */
    BigInteger & operator = (int init);
    BigInteger & operator = (const string & str);
    BigInteger & operator = (const BigInteger & other);

    /** Calculate operation */
    BigInteger operator * (const BigInteger & other);
    BigInteger operator + (const BigInteger & other);
    BigInteger operator / (const BigInteger & other);
    BigInteger operator - (const BigInteger & other);
    BigInteger operator % (const BigInteger & other);
    BigInteger operator * (int other);
    BigInteger operator / (int other);
    BigInteger operator % (int other);

    /** Additional calculate operation */
    /** power(x,y) */
    BigInteger operator ^ (int other);

    bool operator < (const BigInteger & other) const { return compare(other) < 0; }
    bool operator > (const BigInteger & other) const { return compare(other) > 0; }
    bool operator <= (const BigInteger & other) const { return compare(other) <= 0; }
    bool operator >= (const BigInteger & other) const { return compare(other) >= 0; }
    bool operator == (const BigInteger & other) const { return compare(other) == 0; }
    bool operator != (const BigInteger & other) const { return compare(other) != 0; }
    int compare(const BigInteger & y) const;

    /** Convert operation */
    string toString()
    {
      int len = size();
      string ret(len, '0');
      for (int i = 0; i < len; ++i) 
        ret[i] = getNumChar(digits[len - i - 1]);
      return ret;
    }

    int toInt()
    {
      string str = toString();
      int ret;
      sscanf(str.data(), "%d", &ret);
      return ret;
    }
    
    static inline char getNumChar(int x) { return x < 10 ? '0' + x : 'A' - 10 + x; }
};

/** IO operation */
ostream & operator << (ostream & out, const BigInteger & x)
{
  for (int i = x.digits.size() - 1; i >= 0; i--) 
    out << x.digits[i]; 
  return out; 
}

istream & operator >> (istream & in, BigInteger & x)
{
  string line;
  in >> line;
  x = line;
  return in;
}

/** Assignment operation */
BigInteger & BigInteger::operator = (const string & str)
{
  int len = str.length();
  digits = vector<int>(len);
  for (int i = 0; i < len; ++i) 
    digits[i] = str[len - i - 1] - '0';
  return (*this);
}

BigInteger & BigInteger::operator = (int init)
{
  if (init == 0) {
    digits = vector<int>(1);
    digits[0] = 0;
    return (*this);
  }
  digits.clear();
  while (init > 0) {
    digits.push_back(init % BASE);
    init /= BASE;
  }
  return (*this);
}

BigInteger & BigInteger::operator = (const BigInteger & other)
{
  if (&other != this) digits = other.digits;
  return (*this);
}

/** Calculation operations */
BigInteger BigInteger::operator * (const BigInteger & other)
{
  BigInteger ret;
  int lena = size();
  int lenb = other.size();
  int len = lena + lenb;
  ret.digits = vector<int>(len, 0);

  for (int i = 0; i < lena; ++i) 
    for (int j = 0; j < lenb; ++j) 
      ret.digits[i + j] += digits[i] * other.digits[j];

  for (int i = 0; i < len - 1; ++i) { 
    if (ret.digits[i] >= BASE) {
      ret.digits[i + 1] += ret.digits[i] / BASE; 
      ret.digits[i] %= BASE; 
    }
  }

  while (ret.digits[ret.size() - 1] >= BASE) { 
    ret.digits.push_back(ret.digits[ret.size() - 1] / BASE);
    ret.digits[ret.size() - 2] %= BASE;
  }
  while (ret.size() > 1 && ret.digits[ret.size() - 1] == 0) 
    ret.digits.pop_back();
  return ret;
}

/** Multiply int, assume other * BASE < maxint */
BigInteger BigInteger::operator * (int other)
{
  BigInteger ret;
  const static int MAX_INC_LEN = 10;
  ret.digits = vector<int>(size() + MAX_INC_LEN);

  int nowLen = size();
  int len = size() + MAX_INC_LEN;
  for (int i = 0; i < nowLen; ++i) 
    ret.digits[i] = digits[i] * other;
  for (int i = 0; i < len - 1; ++i) 
    if (ret.digits[i] >= BASE) {
      ret.digits[i + 1] += ret.digits[i] / BASE;
      ret.digits[i] %= BASE;
    }
  while (ret.size() > 1 && ret.digits[ret.size() - 1] == 0) 
    ret.digits.pop_back();
  return ret;
}

/** operator plus */
BigInteger BigInteger::operator + (const BigInteger & other)
{
  BigInteger ret; 
  int lena = size();
  int lenb = other.size();
  int len = max(lena, lenb) + 1;
  ret.digits = vector<int>(len, 0);
  int i;
  for (i = 0; i < lena || i < lenb || i < len && ret.digits[i]; i++) {
    if (i < lena) ret.digits[i] += digits[i];
    if (i < lenb) ret.digits[i] += other.digits[i];
    if (ret.digits[i] >= BASE) {
      ret.digits[i + 1] = ret.digits[i] / BASE;
      ret.digits[i] %= BASE;
    }
  }
  if (ret.digits[ret.size() - 1] == 0) 
    ret.digits.pop_back();
  return ret;
}

/** Assume this >= other */
BigInteger BigInteger::operator - (const BigInteger & other)
{
  BigInteger ret;
  int lena = this->size();
  int lenb = other.size();
  int len = lena;
  ret.digits = vector<int>(len, 0);

  for (int i = 0, jiewei = 0; i < lena; i++) {
    ret.digits[i] = digits[i] - jiewei;
    if (i < lenb) ret.digits[i] -= other.digits[i];
    jiewei = 0;
    if (ret.digits[i] < 0) { 
      jiewei = 1;
      ret.digits[i] += BASE;
    } 
  }

  while (ret.size() > 1 && ret.digits[ret.size() - 1] == 0) 
    ret.digits.pop_back();
  return ret;
}

BigInteger BigInteger::operator / (const BigInteger & other)
{
  if (other == 0) cerr << "divide zero" << endl;
  
  BigInteger d(0), ret;
  int lena = size();
  int lenb = other.size();
  int len = lena;
  ret.digits = vector<int>(len, 0);

  for (int i = lena - 1; i >= 0; i--) {
    /** if d != 0, d *= 10 */
    if (d != 0) {
      d.digits.push_back(0);
      for (int j = d.size(); j > 0; --j) 
        d.digits[j] = d.digits[j - 1];
      d.digits[0] = 0;
    }
    d.digits[0] = digits[i]; 
    ret.digits[i] = 0;
    while (int j = d.compare(other) >= 0) {
      d = d - other;
      ret.digits[i]++;
      if (j == 0) break;
    }
  }
 
  /** Remove leading zero */
  while (ret.size() > 1 && ret.digits[ret.size() - 1] == 0)
    ret.digits.pop_back();
  return ret;
}

BigInteger BigInteger::operator / (int other)
{
  if (other == 0) cerr << "divide zero" << endl;
  
  int d = 0;
  BigInteger ret;
  int lena = size();
  int len = lena;
  ret.digits = vector<int>(len, 0);

  for (int i = lena - 1; i >= 0; i--) {
    if (d != 0) d *= 10;
    d += digits[i];
    ret.digits[i] = d / other;
    d %= other;
  }
 
  /** Remove leading zero */
  while (ret.size() > 1 && ret.digits[ret.size() - 1] == 0)
    ret.digits.pop_back();
  return ret;
}

BigInteger BigInteger::operator % (const BigInteger & other) 
{
  if (other == 0) cerr << "divide zero" << endl;
  BigInteger div = (*this) / other;
  return (*this) - div * other;
}

BigInteger BigInteger::operator % (int other)
{
  if (other == 0) cerr << "divide zero" << endl;
  
  int d = 0;
  int lena = size();
  int len = lena;

  for (int i = lena - 1; i >= 0; i--) {
    if (d != 0) d *= 10;
    d += digits[i];
    d %= other;
  }
  return d;
}

BigInteger BigInteger::operator ^ (int other)
{
  if (other < 0) cerr << "power negative" << endl;
  if (other == 0) return 1;
  if (other == 1) return (*this);

  int mid = other / 2;
  BigInteger midResult = (*this) ^ mid;
  return other % 2 == 0 ? midResult * midResult : (midResult * midResult) * (*this);
}

/** Compare two bigInteger
 * Actually , return sign(this - other)
 */
int BigInteger::compare(const BigInteger & other) const
{
  if (size() > other.size()) return 1;
  if (size() < other.size()) return -1;
  int i = size() - 1;
  while (i > 0 && digits[i] == other.digits[i]) 
    i--;
  return digits[i] - other.digits[i];
}

BigInteger gcd(BigInteger a, BigInteger b)
{
  if (b == 0) 
    return a;
  else
    return gcd(b, a % b);
}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i)
  {
    int N;
    cin >> N;
    vector<BigInteger> num(N);

    for (int j = 0; j < N; ++j)
      cin >> num[j];

    BigInteger ans = 0;
    for (int j = 0; j < N; ++j)
      for (int k = j + 1; k < N; ++k)
      {
        BigInteger delta;
        if (num[k] > num[j])
          delta = num[k] - num[j];
        else
          delta = num[j] - num[k];

        if (ans == 0) 
          ans = delta;
        else
          ans = gcd(ans, delta);
      }
    
    if (num[0] % ans == 0)
      ans = 0;
    else
      ans = ans - num[0] % ans;
    
    cout << "Case #" << i << ": " << ans << endl;
  }
  return 0;
}


