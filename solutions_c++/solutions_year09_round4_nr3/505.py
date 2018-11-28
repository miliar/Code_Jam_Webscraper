#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define PII pair<int,int>
#define SZ(x) (int)x.size()
#define LL unsigned long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 100000000

#define GI(x) scanf("%d", &x)

using namespace std;
int N, K;
int d[51][51];
int isok[51][51];
int dp[(1<<16)+100];
int foo()
{
	int lim = 1<<N;
	int i, j, k;
	int ans = 1;
	for(i = 1; i < lim; i++)
	{
		vector<int> v;
		for(j = 0; j < N; j++)
		{
			if(i&(1<<j))
			v.PB(j);
		}
		int flag = 1;
		for(j = 0; j < v.size(); j++)
		{
			for(k = 0; k < v.size(); k++)
			{
				if(j == k)
					continue;
				if(isok[v[j]][v[k]])
				{
					flag = 0;
					break;
				}
			}
			if(flag == 0)
				break;
		}
		if(j == v.size())
		{
			ans = max(ans, __builtin_popcount(i));
		}
	}
	return ans;
}

int solve()
{
	CLRM(dp);
	CLR(isok);
	int i, j, k;
	for(i = 0; i < N; i++)
	{
		for(j = 0; j < N; j++)
		{
			if(i == j)
				continue;
			int flag = 1;
			if(K == 1)
			{
				if(d[i][0] == d[j][0])
				{
					flag = 0;
					break;
				}
			}
			else
			{
				for(k = 0; k < K-1; k++)
				{
					int a = d[i][k], b = d[j][k];
					int an = d[i][k+1], bn = d[j][k+1];
					if(a == b || an == bn)
					{
						flag = 0;
						break;
					}
					if(a > b && an < bn)
					{
						flag = 0;
						break;
					}
					if(a < b && an > bn)
					{
						flag = 0;
						break;
					}
				}
			}				
			if(flag == 1)
			{
				isok[i][j] = 1;
			}
		}
	}
	int ans = foo();
	return ans;
}
int main()
{
	int tes;
	cin >> tes;
	for(int t = 1; t <= tes; t++)
	{
		int i, j, k;
		CLR(d);
		cin >> N >> K;
		for(i = 0; i < N; i++)
		{
			for(j = 0; j < K; j++)
			{
				cin >> k;
				d[i][j] = k;
			}
		}
		int ans = solve();
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
