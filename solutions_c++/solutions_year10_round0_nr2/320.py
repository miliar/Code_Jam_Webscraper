#include <cstdio>
#include <string>
#include <vector>
#include <memory>
#include <cmath>
#include <algorithm>
#include <set>
#include <deque>
#include <stack>
#include <numeric>
#include <functional>
#include <map>
#include <queue>
using namespace std;
class BigInteger{
private:
  enum{MAXLENGTH=100};
  int m[MAXLENGTH];
  int len;

public:
  BigInteger(int n)
  {
    memset(m,0,sizeof(m));
    len=0;
    if (n == 0) len++;
    while (n > 0)
    {
      m[len++] = n % 10;
      n = n / 10;
    }
  }

  BigInteger(void)
  {
    memset(m,0,sizeof(m));
    len=1;
  }

  BigInteger(string s)
  {
    int i;
    len = (int)s.length();
    memset(m,0,sizeof(m));
    for(i=0;i<len;i++)
      m[i] = s[len-i-1]-'0';
  }

  void print(void)
  {
    int temp = len-1;
    while(temp>=0) printf("%d",m[temp--]);
  }

  BigInteger operator+ (const BigInteger &a)
  {
    int i,carry = 0;
    BigInteger Temp(*this);
    if (a.len > Temp.len) Temp.len = a.len;
    for(i=0;i<Temp.len;i++)
    {
      Temp.m[i] += (a.m[i] + carry);
      carry =  Temp.m[i] / 10;
      Temp.m[i] %= 10;
    }
    if (carry > 0) {Temp.m[i] = carry; Temp.len++;}
    return Temp;
  }

  BigInteger operator+ (int a)
  {
    BigInteger Temp(*this);
    int i,carry = a;
    for(i=0;i<Temp.len;i++)
    {
      Temp.m[i] = Temp.m[i] + carry;
      carry = Temp.m[i] / 10;
      Temp.m[i] = Temp.m[i] % 10;
    }
    while (carry > 0) 
    {
      Temp.m[i++] = carry % 10; 
      carry /= 10; 
      Temp.len++;
    }
    return Temp;
  }


  BigInteger operator- (const BigInteger &a) // *this > a !!!
  {
    BigInteger Temp(*this);
    int i,carry = 0;
    for(i=0;i<Temp.len;i++)
    {
      Temp.m[i] = Temp.m[i] - a.m[i] - carry;
      if (Temp.m[i]  < 0) 
      {
        Temp.m[i] = Temp.m[i] +10;
        carry = 1;
      } else carry = 0;
    }
    while (!Temp.m[Temp.len-1] && (Temp.len > 1)) Temp.len--;
    return Temp;
  }

  BigInteger operator- (int a)
  {
    BigInteger Temp(*this);
    int i,carry = a;
    for(i=0;i<Temp.len;i++)
    {
      Temp.m[i] = Temp.m[i] - carry % 10;
      carry = carry / 10;
      if (Temp.m[i] < 0) { carry++; Temp.m[i]+=10;}
    }
    while (Temp.m[Temp.len-1] == 0) Temp.len--;
    return Temp;
  }

  BigInteger operator* (int a)
  {
    BigInteger Temp(0);
    int i,t,carry = 0;
    Temp.len = len;
    for(i=0;i<Temp.len;i++)
    {
      t = a*m[i] + carry;
      Temp.m[i] = t % 10;
      carry = t / 10;
    }
    while (carry > 0) {Temp.m[i++] = carry % 10; carry /= 10; Temp.len++;}
    return Temp;
  }

  BigInteger operator* (const BigInteger &a)
  {
    BigInteger Temp(0);
    int i,j,t,carry;
    for(i=0;i<len;i++)
    {
      carry = 0;
      for(j=0;j<a.len;j++)
      {
        t = Temp.m[i+j] + m[i] * a.m[j] + carry;
        Temp.m[i+j] = t % 10;
        carry = t / 10;
      }
      Temp.m[i+a.len] = carry;
    }
    Temp.len = len + a.len;
    while ((Temp.m[Temp.len-1] == 0) && (Temp.len > 1)) Temp.len--;
    return Temp;
  }

  BigInteger operator/ (int a)
  {
    BigInteger Temp(0);
    int i,ost = 0;
    for(i=len-1;i>=0;i--)
    {
      ost = ost*10+m[i];
      Temp.m[i] = ost/a;
      ost = ost % a;
    }
    Temp.len = len;
    while(Temp.m[Temp.len-1] == 0) Temp.len--;
    return Temp;
  }

  BigInteger Factorial(int a)
  {
    int i;
    BigInteger Temp(1);
    for(i=2;i<=a;i++)
      Temp = Temp * i;
    return Temp;
  }

  BigInteger SqrtBin()
  {
    BigInteger a(0),b(*this),t;
    if ((len == 1) && (m[0] == 1)) return BigInteger(1);
    while (a < b)
    {
      t = (a + b) / 2;
      if (t == a) break;
      if (t*t > (*this)) b = t; else a = t;
    }
    return a;
  }

  BigInteger Sqrt()
  {
    BigInteger Answer, Remain, Odd;
    int group,count,ptr = len-1;
    if (len % 2) ptr++;
    while(ptr >= 0)
    {
      group = m[ptr]*10+m[ptr-1];
      Odd = Answer*20+1;
      Remain = Remain*100+group;
      count = 0;
      while(Remain >= Odd)
      {
        count++;
        Remain = Remain - Odd;
        Odd = Odd + 2;
      }
      Answer = Answer*10+count;
      ptr-=2;
    }
    return Answer;
  }

  int operator< (const BigInteger &a)
  {
    int i;
    if (len < a.len) return 1;
    if (len > a.len) return 0;
    for(i=len-1;(m[i] == a.m[i]) && (i>0);i--);
    if (m[i] < a.m[i]) return 1;
    return 0;
  }

  int operator>= (const BigInteger &a)
  {
    return !(*this < a);
  }

  int operator> (const BigInteger &a)
  {
    int i;
    if (len > a.len) return 1;
    if (len < a.len) return 0;
    for(i=len-1;(m[i] == a.m[i]) && (i>0);i--);
    if (m[i] > a.m[i]) return 1;
    return 0;
  }

  int operator<= (const BigInteger &a)
  {
    return !(*this > a);
  }

  int operator== (const BigInteger &a)
  {
    int i;
    if (len != a.len) return 0;
    for(i = len-1;i>=0;i--)
      if (m[i] != a.m[i]) return 0;
    return 1;
  }

  int operator!= (const BigInteger &a)
  {
    return !(*this == a);
  }

  BigInteger operator/ (const BigInteger &div)
  {
    BigInteger a(0),b(*this),t(div);
    if (t == BigInteger(1)) return *this;
    if (t > b) return a;
    while(a < b)
    {
      t = (a + b) / 2;
      if (t == a) break;
      if (t*div > (*this)) b = t; else a = t;
    }
    return a;
  }

  BigInteger mod (const BigInteger &div)
  {
    BigInteger Temp(*this);
    Temp = *this - (Temp/div)*div;
    return Temp;
  }
};
BigInteger Zero(0);
BigInteger GCD(BigInteger a, BigInteger b)
{
  if (b > Zero) return GCD(b,a.mod(b));
  return a;
}
int main(void)
{
	int t,q,i,n;
	string a;
	char s[100];
	BigInteger res;
	freopen("Bb.in","r",stdin);
	freopen("Bb.out","w",stdout);
	vector<BigInteger> v;
	scanf("%d",&t);
	for (q=1;q<=t;q++)
	{
		v.clear();
		scanf("%d",&n);
		for (i=0;i<n;i++)
		{
			scanf("%s",&s);
			a=string(s);
			v.push_back(BigInteger(a));
		}
		res=Zero;
		for (i=1;i<v.size();i++)
		{
			if (v[i]>=v[i-1])
				res=GCD(res,v[i]-v[i-1]); else
				res=GCD(res,v[i-1]-v[i]);
		}
		if (v[0].mod(res)==0)
			printf("Case #%d: 0\n",q); else
		{
			res=res-v[0].mod(res);
			printf("Case #%d: ",q);
			res.print();
			printf("\n");
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}