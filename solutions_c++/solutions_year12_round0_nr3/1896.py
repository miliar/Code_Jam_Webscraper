#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <map>
#include <string>
#include <cmath>
#include <math.h>
#include <fstream>

using namespace std;

int t;

long power(long a,long b)
{
     long ret=1;
     while(b--) ret*=a;
     return ret;
}

int cnt(long k)
{
	int ret=0;
	while(k) {ret++;k/=10;}
	return ret;
}

long leftShift(long k,int s)
{
	return (k%10)*power(10,s-1)+k/10;
}

bool findMin(long k)
{
	long i=leftShift(k,cnt(k));
	int s=cnt(k);
	while(i!=k)
	{
		if(i<k&&cnt(i)==cnt(k)) return false;
		i=leftShift(i,s);
	}
	return true;
}

long check(long k,long a,long b)
{
	int s=cnt(k);
	long i,ret=0;
	while(1)
	{
		i=leftShift(i,s);
		if(i>=a&&i<=b&&cnt(i)==cnt(k)) ret++;
		if(i==k) break;
	}
	return ret*(ret-1)/2;
}

long a[100],b[100];

int main()
{
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
		scanf("%ld%ld",&a[i],&b[i]);
	for(int i=1;i<=t;i++)
		printf("%ld %ld\n",a[i],b[i]);
	for(int tt=1;tt<=t;tt++)
	{
		long ans=0;
		for(long i=power(10,cnt(a[tt])-1);i<power(10,cnt(b[tt]));i++)
		{
			if(findMin(i))
				ans+=check(i,a[tt],b[tt]);
		}
		printf("Case #%d: %ld\n",tt,ans);
	}
	return 0;
}
