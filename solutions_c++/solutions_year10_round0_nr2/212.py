#include <iostream>
#include <cstring>
using namespace std;
const int Base=1000000000,Capacity=100;

struct BigInt
{
   int len;
   int data[Capacity];
   BigInt() { len=0;}
   BigInt(const BigInt &v)
   {
      len = v.len;
      memcpy(data,v.data,len*sizeof(int));
   }
   BigInt(int v)
   {
      len=0;
      while (v) {data[len++]=v%Base;v/=Base;}
   }
   BigInt(long long v)
   {
      len=0;
      while (v) { data[len++]=v%Base;v/=Base;}
   }
   BigInt &operator=(int v)
   {
      len=0;
      while (v) {data[len++]=v%Base;v/=Base;}
      return *this;
   }
   BigInt &operator=(long long v)
   {
      len=0;
      while (v) {data[len++]=v%Base;v/=Base;}
      return *this;
   }
   BigInt &operator=(const BigInt &v)
   {
      len=v.len;
      memcpy(data,v.data,len*sizeof(int));
      return *this;
   }
   int &operator[](int index) { return data[index];}
   int operator[](int index) const { return data[index];}
};

int compare(const BigInt &a,const BigInt &b)
{
   if (a.len!=b.len) return a.len>b.len?1:-1;
   int i=a.len-1;
   while (i>=0 && a[i]==b[i]) i--;
   if (i<0) return 0;
   return a[i]>b[i]?1:-1;
}

BigInt operator+(const BigInt &a,const BigInt &b)
{
   BigInt c;
   int i,carry=0;
   for (i=0;i<a.len || i<b.len || carry>0;i++)
   {
      if (i<a.len) carry+=a[i];
      if (i<b.len) carry+=b[i];
      c[i]=carry%Base;
      carry/=Base;
   }
   c.len=i;
   return c;
}

BigInt operator-(const BigInt &a,const BigInt &b)
{
   BigInt c;
   int carry=0;
   c.len=a.len;
   for (int i=0;i<c.len;i++)
   {
      c[i]=a[i]-carry;
      if (i<b.len) c[i]-=b[i];
      if (c[i]<0)
      {
         carry=1;
         c[i]+=Base;
      }
      else carry=0;
   }
   while (c.len>0 && c[c.len-1]==0) c.len--;
   return c;
}

BigInt operator*(const BigInt &a,const int b)
{
   if (b==0) return 0;
   BigInt c;
   long long carry=0;
   int i;
   for (i=0;i<a.len || carry>0;i++)
   {
      if (i<a.len) carry+=(long long)a[i]*b;
      c[i]=carry%Base;
      carry/=Base;
   }
   c.len=i;
   return c;
}

BigInt operator*(const BigInt &a,const BigInt &b)
{
   if (b.len==0) return 0;
   BigInt c;
   for (int i=0;i<a.len;i++)
   {
      long long carry=0;
      for (int j=0;j<b.len || carry>0;j++)
      {
         if (j<b.len) carry+=a[i]*b[j];
         if (i+j<c.len)
         {
            carry+=c[i+j];
            c[i+j]=carry%Base;
         }
         else c[c.len++]=carry%Base;
         carry/=Base;
      }
   }
   return c;
}

BigInt operator/(const BigInt &a,const int b)
{
   BigInt c;
   long long t=0;
   for (int i=a.len-1;i>=0;i--)
   {
      t=t*Base+a[i];
      c[i]=t/b;
      t%=b;
   }
   c.len=a.len;
   while (c.len>0 && c[c.len-1]==0) c.len--;
   return c;
}

int operator%(const BigInt &a,const int b)
{
   long long t=0;
   for (int i=a.len-1;i>=0;i--)
   {
      t=t*Base+a[i];
      t%=b;
   }
   return t;
}

BigInt operator/(const BigInt &a,const BigInt &b)
{
   BigInt c,carry=0;
   int left,right,mid;
   for (int i=a.len-1;i>=0;i--)
   {
      carry=carry*Base+a[i];
      left=0,right=Base-1;
      while (left<right)
      {
         mid=(left+right+1)/2;
         if (compare(b*mid,carry)<=0) left=mid;else right=mid-1;
      }
      c[i]=left;
      carry=carry-b*left;
   }
   c.len=a.len;
   while (c.len>0 && c[c.len-1]==0) c.len--;
   return c;
}

BigInt operator%(const BigInt &a,const BigInt &b)
{
   BigInt c,carry=0;
   int left,right,mid;
   for (int i=a.len-1;i>=0;i--)
   {
      carry=carry*Base+a[i];
      left=0;right=Base-1;
      while (left<right)
      {
         mid=(left+right+1)/2;
         if (compare(b*mid,carry)<=0) left=mid;else right=mid-1;
      }
      c[i]=left;
      carry=carry-b*left;
   }
   c.len=a.len;
   while (c.len>0 && c[c.len-1]==0) c.len--;
   return carry;
}

istream &operator>>(istream &in, BigInt &v)
{
	char ch;
	for (v = 0; in >> ch;)
	{
		v = v * 10 + (ch - '0');
		if (in.peek() <= ' ') break;
	}
	return in;
}

ostream &operator<<(ostream &out, const BigInt &v)
{
	out << (v.len == 0 ? 0 : v[v.len - 1]);
	for (int i = v.len - 2; i >=0; --i)
		for (int j = Base / 10; j > 0; j /= 10)
			out << v[i] / j % 10;
	return out;
}
const int MAXN = 1000;
int n;
BigInt a[MAXN];
BigInt b[MAXN];
BigInt T, ans;
BigInt gcd(BigInt &a, BigInt &b)
{
	while (b.len != 0)
	{
		BigInt temp = a % b;
		a = b;
		b = temp;
	}
	return a;
}
char ch;
int main()
{
	int cases;
	cin >> cases;
	for (int i = 1; i <= cases; ++i)
	{
		int n;
		cin >> n;
		for (int j = 0; j < n; ++j) cin >> a[j];
		for (int j = 1; j < n; ++j)
		{
			if (compare(a[j - 1], a[j]) > 0)
				b[j] = a[j - 1] - a[j];
			else b[j] = a[j] - a[j - 1];
		}
		T = b[1];
		for (int j = 2; j < n; ++j) T = gcd(T, b[j]);
		ans = (T - a[0] % T) % T;
		cout << "Case #" << i << ": " << ans << endl;
		
	}
	return 0;
}
