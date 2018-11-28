#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

__int64 a[100],b[100];

int gcd(__int64 x,__int64 y)
{
	if (y==0) return x;
	return gcd(y,x%y);
}

__int64 xabs(__int64 x)
{
	if (x>=0) return x;
	return -x;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t,tt;
	int n,i,j;
	scanf("%d",&t);
	for (tt=0; tt<t; ++tt)
	{
		scanf("%d",&n);
		for (i=0; i<n; ++i)
			scanf("%I64d",&b[i]);
		for (i=0; i<n; ++i)
			for (j=i+1; j<n; ++j)
				a[i+j]=xabs(b[i]-b[j]);
		__int64 T=a[1];
		for (i=1; i<=n*(n-1)/2; ++i)
			T=gcd(T,a[i]);
		printf("Case #%d: %I64d\n",tt+1,(b[0]+T-1)/T*T-b[0]);
	}
	return 0;
}