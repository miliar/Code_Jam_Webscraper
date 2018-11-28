#include <string.h>
#include <sstream>
#include <string>
#include <map>
#include <queue>
#include <vector>
#include <set>
#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
#define ll long long

int a[100000];

int main()
{
	int T;
	scanf("%d",&T);
	for(int c =0;c<T;)
	{
		int n;
		scanf("%d",&n);
		int ret = 0;
		for(int i=0;i<n;++i)
		{
			scanf("%d",&a[i]);
			ret^=a[i];
		}

		printf("Case #%d: ",++c);
		if( ret )
			printf("NO\n");
		else
		{
			int sum= a[0];
			int ans = a[0];
			for(int i=1;i<n;++i)
			{
				sum+=a[i];
				ans = min(ans,a[i]);
			}
			printf("%d\n",sum-ans);
		}
	}
}

