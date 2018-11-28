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

char a[25][25];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T, tt;
	scanf("%d", &T);
	for (tt=0; tt<T; ++tt)
	{
		int n, m, d;
		int i, j, r;
		int ii, jj;
		scanf("%d%d%d\n", &n, &m, &d);
		for (i=0; i<n; ++i)
		{
			for (j=0; j<m; ++j)
			{
				scanf("%c", &a[i][j]);
			}
			scanf("\n");
		}
		for (r=min(n, m); r>2; --r)
		{
			for (i=0; i<=n-r; ++i)
			{
				for (j=0; j<=m-r; ++j)
				{
					int ci=2*i+r;
					int cj=2*j+r;
					int mi=0;
					int mj=0;
					for (ii=i; ii<i+r; ++ii)
						for (jj=j; jj<j+r; ++jj)
							if (!(ii==i && jj==j || ii==i+r-1 && jj==j ||
								ii==i && jj==j+r-1 || ii==i+r-1 && jj==j+r-1))
							{	
								mi+=(2*ii+1-ci)*(d+a[ii][jj]-'0');
								mj+=(2*jj+1-cj)*(d+a[ii][jj]-'0');
							}
					if (mi==0 && mj==0)
						break;
				}
				if (j<=m-r)
					break;
			}
			if (i<=n-r)
				break;
		}
		printf("Case #%d: ", tt+1);
		if (r>2)
			printf("%d\n", r);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
