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

int a[1023],b[1023];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t,tt;
	int n,i,j,ans;
	scanf("%d",&t);
	for (tt=0; tt<t; ++tt)
	{
		scanf("%d",&n);
		ans=0;
		for (i=0; i<n; ++i)
		{
			scanf("%d%d",&a[i],&b[i]);
			for (j=0; j<i; ++j)
				if ((a[j]-a[i])*(b[j]-b[i])<0) ans++;
		}
		printf("Case #%d: %d\n",tt+1,ans);
	}
	return 0;
}