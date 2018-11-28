// google-B edit.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class longint
{
public:
	int a[64];
	int digit;
	longint(longint &a);
	longint();
	friend longint operator +(longint &a,longint &b);
	friend longint operator -(longint &a,longint &b);
	friend longint operator /(longint &a,longint &b);
	friend longint operator %(longint &a,longint &b);
	friend istream& operator >> (istream& input,longint& a);
	friend ostream& operator << (ostream& output,longint& a);
};


int cmp(longint &a,longint &b)
{
	if (a.digit>b.digit) return 1;
	if (a.digit<b.digit) return -1;
	int i=a.digit-1;
	while (i>=0)
	{
		if (a.a[i]>b.a[i]) return 1;
		if (a.a[i]<b.a[i]) return -1;
		i--;
	}
	return 0;
}

void gcd(longint &a,longint &b)
{
	while(1)
	{
		if (cmp(a,b)>0) 
		{
			a=a%b;
			if ((a.digit==1)&&(a.a[0]==0))
			{
				a=b;
				break;
			}
		}
		else 
		{
			b=b%a;
			if ((b.digit==1)&&(b.a[0]==0)) break;
		}
	}
}
istream& operator >> (istream& input,longint& a)
{
	string str;
	int i;
	input>>str;
	a.digit=str.length();
	for (i=0;i<a.digit;i++)
		a.a[i]=str[a.digit-i-1]-48;
	return input;
}

ostream& operator << (ostream& output,longint& a)
{
	int i;
	for (i=a.digit-1;i>=0;i--)
		output<<a.a[i];
	return output;
}

longint operator + (longint &a,longint &b)
{
	longint sum;
	int i,digit;
	if (a.digit>b.digit) digit=a.digit;
	else digit=b.digit;
	sum.a[0]=a.a[0]+b.a[0];
	for (i=1;i<=digit;i++)
	{
		sum.a[i]=a.a[i]+b.a[i];
		sum.a[i]+=sum.a[i-1]/10;
		sum.a[i-1]=sum.a[i-1]%10;
	}
	if (sum.a[digit]>0) sum.digit=digit+1;
	return sum;
}

longint operator - (longint &a,longint &b)
{
	longint ans;
	int i,digit;
	digit=a.digit;
	ans.a[0]=a.a[0]-b.a[0];
	for (i=1;i<b.digit;i++)
	{
		ans.a[i]=a.a[i]-b.a[i];
		if (ans.a[i-1]<0) 
		{
			ans.a[i-1]+=10;
			ans.a[i]-=1;
		}
	}
	for (;i<a.digit;i++)
	{
		ans.a[i]=a.a[i];
		if (ans.a[i-1]<0) 
		{
			ans.a[i-1]+=10;
			ans.a[i]-=1;
		}
	}
	while ((ans.a[digit-1]==0)&&(digit>1)) digit--;
	ans.digit=digit;
	return ans;
}

void multiply10(longint &a)     
{
	int i;
    for(i=a.digit-1;i>=0;i--)
		a.a[i+1]=a.a[i];
	a.a[0]=0;
    a.digit++;
    while((a.digit>1)&&(a.a[a.digit-1]==0)) a.digit--;
}

longint operator /(longint &a,longint &b)
{
	longint ans,r,t;
	int i,digit;
	digit=a.digit;
	r.digit=1;
	for (i=digit-1;i>=0;i--)
	{
		multiply10(r);
		r.a[0]=a.a[i];
		while (cmp(r,b)>=0)
		{
			r=r-b;
			ans.a[i]++;
		}
	}
	while ((digit>1)&&(ans.a[digit-1]==0)) digit--;
	ans.digit=digit;
	return ans;	
}

longint operator %(longint &a,longint &b)
{
	longint ans,r,t;
	int i,digit;
	digit=a.digit;
	r.digit=1;
	for (i=digit-1;i>=0;i--)
	{
		multiply10(r);
		r.a[0]=a.a[i];
		while (cmp(r,b)>=0)
		{
			r=r-b;
			ans.a[i]++;
		}
	}
	while ((digit>1)&&(ans.a[digit-1]==0)) digit--;
	ans.digit=digit;
	return r;	
}

longint::longint (longint &b)
{
	int i;
	digit=b.digit;
	for (i=0;i<64;i++) a[i]=b.a[i];
}
longint::longint()
{
	int i;
	digit=1;
	for (i=0;i<64;i++) a[i]=0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin("B-large.in",ios::binary|ios::binary);
	ofstream fout("out.txt",ios::binary|ios::binary);

	longint min,a,b,last,current;
	int n,t,i,c;
	fin>>t;
	for (c=1;c<=t;c++)
	{
		fin>>n;
		fin>>last;
		min=last;
		for (i=1;i<n;i++)
		{
			fin>>current;
			if (cmp(last,current)>0) a=last-current;
			else a=current-last;
			if (cmp(min,current)>0) min=last;
			if ((a.digit>1)||(a.a[0]>0)) break;
		}
		i++;
		for(;i<n;i++)
		{
			fin>>current;
			if (cmp(min,current)>0) min=current;
			if (cmp(last,current)>0) b=last-current;
			else b=current-last;
			if ((b.digit==1)&&(b.a[0]==0)) continue;
			gcd(a,b);
			last=current;
		}
		while(cmp(min,a)==1)
		{
			min=min%a;
		}
		if ((min.digit>1)||(min.a[0]>0)) min=a-min;
		fout<<"Case #"<<c<<": "<<min<<endl;
	}
	return 0;
}

