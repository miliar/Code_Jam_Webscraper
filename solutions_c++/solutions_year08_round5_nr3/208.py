const double pi=3.1415926535897932, e=2.7182818284590452;
#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/stack:16000000")
#include <cstdio>
#include <cmath>
#include <complex>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

int C,n,m,mm;

char c[20][20];
int a[20][2024];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	scanf("%d",&C);
	for (int ii=1; ii<=C; ++ii)
	{
		scanf("%d%d\n",&n,&m);
		for (int i=1; i<=n; ++i)
		{
			gets(c[i]);
		}
		memset(a, 0, sizeof a);
		mm=(1<<m);
		for (int i=1; i<=n; ++i)
		{
			for (int j=0; j<mm; ++j)
				for (int k=0; k<mm; ++k)
				{
					if (ii==2 && i==2 && j==2 && k==0)
						printf("");
					bool f=true;
					// битые
					for (int l=0; l<m && f; ++l)
						if (c[i][l]=='x' && (k & (1<<l)))
							f=false;
					// слева/справа
					for (int l=0; l<m-1 && f; ++l)
						if ((k & (3<<l))==(3<<l))
							f=false;
					// спереди-слева/спереди-справа
					for (int l=0; l<m && f; ++l)
					{
						if (l>0 &&   (k & (1<<l)) && (j & (1<<(l-1))))
							f=false;
						if (l<m-1 && (k & (1<<l)) && (j & (1<<(l+1))))
							f=false;
					}
					// теперь плюсуем, если можно
					if (f)
					{
						int r=a[i-1][j];
						for (int l=0; l<m; ++l)
							if (k & (1<<l))
								++r;
						if (a[i][k] < r)
							a[i][k] = r;
						if (r>5)
							printf("");
					}
				}
		}
		int res=0;
		for (int j=0; j<mm; ++j)
			res = max(res, a[n][j]);
		printf("Case #%d: %d\n", ii, res);
	}
	return 0;
}
