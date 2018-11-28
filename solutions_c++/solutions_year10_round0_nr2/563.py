// Fair Warning.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;
struct BigNum
{
	char num[100];
	int count;
	BigNum& operator=(const BigNum& b)
	{
		for(int i=0;i<b.count;i++) num[i]=b.num[i];
		count=b.count;
		num[count]=0;
		return *this;
	}
}bignums[1005];

BigNum operator-(BigNum& a,const BigNum& b)
{
	BigNum c=a;
	for(int i=0;i<b.count;i++)
	{
		c.num[i]=c.num[i]-b.num[i]+'0';
		while(c.num[i]<'0') c.num[i]+=10,c.num[i+1]-=1;
	}
	for(int i=0;i<c.count;i++)
	{
		while(c.num[i]<'0') c.num[i]+=10,c.num[i+1]-=1;
	}
	c.count=0;
	for(int i=a.count-1;i>=0;i--)
	{
		if(c.num[i]!='0')
		{
			c.num[i+1]=0;
			c.count=i+1;
			break;
		}
	}
	if(c.count==0)
	{
		c.num[0]='0';
		c.num[1]=0;
	}
	return c;
	
}
bool operator<(const BigNum& a,const BigNum& b)
{
	if(a.count!=b.count) return a.count<b.count;
	for(int i=a.count-1;i>=0;i--)
	{
		if(a.num[i]!=b.num[i]) return a.num[i]<b.num[i];
	}
	return false;
}
bool operator==(const BigNum& a,const BigNum& b)
{
	if(a.count!=b.count) return false;
	for(int i=a.count-1;i>=0;i--)
	{
		if(a.num[i]!=b.num[i]) return false;
	}
	return true;
}
BigNum GCD(BigNum a,BigNum b)
{
	if(a<b) return GCD(b,a);
	if(b.count==0) return a;//0的情况特殊处理
	while(b<a) a=a-b;
	if(a==b) return a;
	else return GCD(b,a);
}
int main()
{
	freopen("e:\\B-small-attempt1.in","r",stdin);
	freopen("e:\\1.out","w",stdout);
	int C,N,minIndex;
	scanf("%d",&C);
	for(int i=1;i<=C;i++)
	{
		scanf("%d",&N);
		for(int j=0;j<N;j++)
		{
			scanf("%s",bignums[j].num);
			bignums[j].count=strlen(bignums[j].num);
			strrev(bignums[j].num);
		}
		minIndex=0;
		for(int j=1;j<N;j++) 
			if(bignums[j]<bignums[minIndex]) minIndex=j;
		for(int j=0;j<N;j++)
		{
			if(j!=minIndex) bignums[j]=bignums[j]-bignums[minIndex];
		}
		BigNum offence=bignums[minIndex];
		bignums[minIndex]=bignums[minIndex]-bignums[minIndex];
		BigNum gcd=GCD(bignums[0],bignums[1]);
		for(int j=2;j<N;j++) gcd=GCD(gcd,bignums[j]);
		while(gcd<offence) offence=offence-gcd;
		BigNum ans=gcd-offence;
		strrev(ans.num);
		printf("Case #%d: %s\n",i,ans.num);
	}
	return 0;
}

