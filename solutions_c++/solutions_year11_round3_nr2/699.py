//============================================================================
// Name        : gcj_b.cpp
// Author      : yb
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <queue>
#define ll long long
#define _clr(a) memset(a,0,sizeof(a));
#define FOR(i,x,n) for(int i=x;i<n;i++)
#define max(a,b) a>b?a:b
#define min(a,b) a<b?a:b
#define abs(a) a>0?a:a*-1
#define re return
#define sqr(x) ((x) * (x))
#define inf 268435456;
using namespace std;
const double eps = 1e-10;
const double pi = acos(-1);
int l, n, c;
ll ti;
int a[10005];
int b[1005];
int vis[10005];
ll tmp[10005], ans[10005];
int main()
{
	int cas = 1, t, n, i, j;
	freopen("3.in","r",stdin);
	freopen("3.out","w",stdout);
	scanf("%d", &t);
	while (t--)
	{
		_clr(vis);
		scanf("%d %lld %d %d", &l, &ti, &n, &c);
		for (int i = 0; i < c; i++)
			scanf("%d", &b[i]);
		for (int i = 0, j = 0; i < n; i++, j++)
		{
			a[i] = b[j];
			if (j == c - 1)
				j = -1;
		}
		ans[0] = 0;
		for (int i = 1; i <= n; i++)
		{
			tmp[i - 1] = a[i-1] * 2;
			ans[i] = ans[i - 1] + tmp[i-1];
		}
		ll fuck = ans[n];
		int ind;
		int maxt = 0, temp;
		for (int k = 0; k < l; k++)
		{

			maxt=0;
			ind=0;
			for (int i = 0; i < n ; i++)
			{
				if (!vis[i])
				{
					if (ans[i] > ti)
					{
						temp = a[i];
						if (temp > maxt)
						{
							maxt = temp;
							ind = i;
						}
					}
					else
					{
						temp = (tmp[i] - ti + ans[i]) / 2;
						if (temp > maxt)
						{
							maxt = temp;
							ind = i;
						}
					}
				}

			}vis[ind]=1;
			for(int i=ind+1;i<=n;i++)
			{
				tmp[i-1]-=maxt;
				ans[i]-=maxt;
			}
			fuck=ans[n];
		}
		printf("Case #%d: ", cas++);printf("%lld\n", fuck);
		}
		re 0;
	}
