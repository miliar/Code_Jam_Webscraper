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

const double inf=1e9;
const double eps=1e-8;

struct Event
{
	int x;
	int w;
	Event(){}
	Event(int xx, int ww)
	{
		x=xx;
		w=ww;
	}
};

int b[1005], e[1005], w[1005];
int ind[1005];

bool cmp(int i, int j)
{
	return b[i]<b[j];
}

double f[2][1000500];
int v[250];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input2.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T, tt;
	scanf("%d", &T);
	for (tt=0; tt<T; ++tt)
	{
		int x, s, r, n;
		double t;
		int i, j;
		scanf("%d%d%d%lf%d", &x, &s, &r, &t, &n);
		for (i=0; i<n; ++i)
		{
			scanf("%d%d%d", &b[i], &e[i], &w[i]);
			ind[i]=i;
		}
		sort(ind, ind+n, cmp);
		memset(v, 0, sizeof(v));
		int last=0;
		for (i=0; i<n; ++i)
		{
			v[0]+=(b[ind[i]]-last);
			v[w[ind[i]]]+=(e[ind[i]]-b[ind[i]]);
			last=e[ind[i]];
		}
		if (e[ind[n-1]]<x)
			v[0]+=(x-last);
		double ans=0;
		for (i=0; i<=150; ++i)
		{
			if (t>eps)
			{	
				double rr=double(v[i])/(r+i);
				if (rr<t+eps)
				{
					t-=rr;
					ans+=rr;
				}
				else
				{
					ans+=t;
					ans+=(v[i]-t*(r+i))/(s+i);
					t=0;
				}
			}
			else
			{
				ans+=double(v[i])/(s+i);
			}
		}
		printf("Case #%d: %.8lf\n", tt+1, ans);
	}
	return 0;
}