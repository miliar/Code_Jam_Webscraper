#include <vector>
#include <string>
#include <list>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <sstream>
#include<iostream>
using namespace std;
int T;
int N;

#define MAXN 9999 
#define DLEN 4 
int const MaxBits = 900;
int const Bits = 4;
int const MaxLen = MaxBits / Bits + 1; 
int const MaxSingle = 10000;

struct BigInt
{
	int Dig[MaxLen];
	int Digs;   
	// void operator = (int n);
	void operator = (char *s);
	void operator = (long long n);
	void Print();
};

void BigInt::Print()
{
	printf("%d",Dig[Digs-1]);
	for(int i = Digs-2,tmp; i >= 0; i--)
	{
		tmp = MaxSingle / 10;
		while(tmp > 1)
		{
			if(Dig[i] < tmp)
				printf("0");
			else
				break;
			tmp /= 10;
		}
		printf("%d",Dig[i]);
	}
}

void BigInt::operator = (long long n)
{
	Digs = 0;
	while(n > 0)
	{
		Dig[Digs++] = n % MaxSingle;
		n /= MaxSingle;
	}
	for(int i = Digs; i < MaxLen; i++)
		Dig[i] = 0;
}

void BigInt::operator = (char *StrNum)
{
	int len = strlen(StrNum), tmp;
	Digs = 0;
	for( ; len >= Bits; len -= Bits)
	{
		tmp = 0;
		for(int i = len - Bits; i < len; i++)
			tmp *= 10, tmp += StrNum[i] - '0';
		Dig[Digs++] = tmp;
	}
	if(len == 0)
		return;
	tmp = 0;
	for(int i = 0; i < len; i++)
		tmp *= 10, tmp += StrNum[i] - '0';
	Dig[Digs++] = tmp;
	for(int i = Digs; i < MaxLen; i++)
		Dig[i] = 0;
}

BigInt operator + (BigInt const &a, BigInt const &b)
{
	BigInt c = a;
	int carry(0);
	c.Digs = c.Digs> b.Digs ? b.Digs : c.Digs;
	for(int i = 0; i < c.Digs; i++)
	{
		c.Dig[i] += b.Dig[i] + carry;
		if(c.Dig[i] >= MaxSingle)
			c.Dig[i] -= MaxSingle, carry = 1;
		else
			carry = 0;
	}
	if(carry > 0)
		c.Dig[c.Digs++] = carry;
	return c;
}

BigInt operator - (BigInt const &a, BigInt const &b)
{   // assume that a > b,  a and b are positive
	BigInt c = a;
	int dec = 0;
	for(int i = 0; i < c.Digs; i++)
	{
		c.Dig[i] -= b.Dig[i] + dec;
		if(c.Dig[i] < 0)
			c.Dig[i] += MaxSingle, dec = 1;
		else
			dec = 0;
	}
	while(c.Digs > 1 && c.Dig[c.Digs-1] == 0)
		c.Digs--;
	return c;
}

BigInt operator * (BigInt const &a, BigInt const &b)
{
	BigInt c;
	for(int i = 0; i < MaxLen; i++)
		c.Dig[i] = 0;
	int carry;
	for(int i = 0; i < a.Digs; i++)
	{
		carry = 0;
		for(int j = 0; j < b.Digs; j++)
		{
			c.Dig[i+j] += a.Dig[i] * b.Dig[j] + carry;
			carry = c.Dig[i+j] / MaxSingle;
			c.Dig[i+j] -= carry * MaxSingle;
		}
		if(carry != 0)
			c.Dig[i+b.Digs] += carry;
	}
	c.Digs = a.Digs + b.Digs;
	while(c.Digs > 1 && c.Dig[c.Digs-1] == 0)
		c.Digs--;
	return c;
}

BigInt operator * (BigInt const &a, int const &b)
{
	BigInt c = a;
	for(int i = 0; i < c.Digs; i++)
		c.Dig[i] *= b;
	int carry = 0;
	for(int i = 0; i < c.Digs; i++)
	{
		c.Dig[i] += carry;
		carry = c.Dig[i] / MaxSingle;
		c.Dig[i] -= carry * MaxSingle;
	}
	while(carry > 0)
		c.Dig[c.Digs++] = carry % MaxSingle, carry /= MaxSingle;
	return c;
}

BigInt operator + (BigInt const &a, int const &b)
{
	BigInt c = a;
	int carry = b;
	for(int i = 0; carry > 0; i++)
	{
		c.Dig[i] += carry;
		carry = c.Dig[i] / MaxSingle;
		c.Dig[i] -= carry * MaxSingle;
		if(i == c.Digs)
			c.Digs++;
	} 
	return c;
}

bool operator < (BigInt const &a, BigInt const &b)
{
	if(a.Digs == b.Digs)
		for(int i = a.Digs - 1; i >= 0; i--)
			if(a.Dig[i] != b.Dig[i])
				return a.Dig[i] < b.Dig[i];
	return a.Digs < b.Digs;
}

bool operator == (BigInt const &a, BigInt const &b)
{
	if(a.Digs != b.Digs)
		return false;
	for(int i = 0; i < a.Digs; i++)
		if(a.Dig[i] != b.Dig[i])
			return false;
	return true;
}

BigInt operator / (BigInt const &a, BigInt const &b)
{
	BigInt c,t,m;
	for(int i = 0; i < MaxLen; i++)
		c.Dig[i] = t.Dig[i] = 0;
	t.Digs = 1;
	for(int i = a.Digs - 1; i >= 0; i--)
	{
		t = t * MaxSingle;
		t = t + a.Dig[i];
		int left = 0, right = MaxSingle, mid;
		while(left < right - 1)
		{
			mid = ((left + right)>> 1);
			m = b * mid;
			if(m < t) // m >= t
				left = mid;
			else
				if(m == t)
					left = right = mid;   // exit
				else
					right = mid;
		}
		m = b * left;
		c.Dig[i] = left;
		t = t - m;        
	}
	c.Digs = a.Digs;
	while(c.Digs > 1 && c.Dig[c.Digs-1] == 0)
		c.Digs--;
	return c;
}

BigInt operator % (BigInt const &a, BigInt const &b)
{
	return a - (a / b) * b;
}

BigInt pow(BigInt const &a, int n)
{
	BigInt c,t;
	for(int i = 0; i < MaxLen; i++)
		c.Dig[i] = 0;
	c.Dig[0] = 1;
	c.Digs = 1;
	t = a;
	while(n > 0)
	{
		if(n & 1)
			c = c * t;
		t = t * t;
		n = (n>>1);    
	}
	return c;
}




BigInt allNum[1010];
BigInt subNum[1010];
BigInt t_0;

BigInt gcd(BigInt & a, BigInt & b)
{
	//a.Print();printf("\n");
	//b.Print();printf("\n");
	if(b == t_0) return a;
	if(a == t_0) return b;
	if(a < b)
		return gcd(a, b % a);
	else
		return gcd(b, a % b);
}
BigInt getGcd()
{
	if(N == 2)
		return subNum[0];
	BigInt res = gcd(subNum[0], subNum[1]);
	for(int i = 3;i < N - 1;i++)
		res = gcd(res, subNum[i]);
	return res;
}
int main()
{
	freopen("..\\B-small-attempt0.in","r",stdin);
	freopen("..\\B-small-attempt0.out","w",stdout);
	scanf("%d", &T);
	t_0 = 1ll;
	t_0 = t_0 - t_0;
	for(int t = 1;t <= T;t++)
	{
		scanf("%d", &N);
		char buf[100];
		for(int i = 0;i < N;i++)
		{
			scanf("%s",buf);
			allNum[i] = buf;
		}
		for(int i = 1;i < N;i++)
		{
			if(allNum[i] < allNum[i - 1])
				subNum[i - 1] = allNum[i - 1] - allNum[i];
			else
				subNum[i - 1] = allNum[i] - allNum[i - 1];
			/*cout<<"##";
			subNum[i - 1].Print();
			cout<<endl;*/
		}
		BigInt resgcd = getGcd();

		/*cout<<"%%";
		resgcd.Print();
		cout<<endl;*/

		BigInt res_f = (resgcd - (allNum[0] % resgcd)) % resgcd;
		for(int i = 1;i < N;i++)
		{
			if(((resgcd - (allNum[i] % resgcd)) % resgcd) < res_f)
				res_f = (resgcd - (allNum[i] % resgcd)) % resgcd;
		}
		printf("Case #%d: ",t);
		res_f.Print();
		printf("\n");
	}
	return 0;
}
