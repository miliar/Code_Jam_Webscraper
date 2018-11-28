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
#include <functional>
using namespace std;

#pragma comment(linker,"/STACK:100000000")

bool use[1050];
int a[1050];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input2.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int i;
	int T, tt;
	scanf("%d", &T);
	for (tt=0; tt<T; ++tt)
	{
		int n;
		int ans=0;
		scanf("%d", &n);
		for (i=0; i<n; ++i)
		{
			scanf("%d", &a[i]);
			--a[i];
		}
		memset(use, false, sizeof(use));
		for (i=0; i<n; ++i)
			if (!use[i])
			{
				int cnt=1, cur=i;
				use[i]=true;
				while (a[cur]!=i)
				{
					cnt++;
					cur=a[cur];
					use[cur]=true;
				}
				if (cnt>1)
					ans+=cnt;
			}
		printf("Case #%d: ", tt+1);
		printf("%.7lf\n", double(ans));
	}
	return 0;
}