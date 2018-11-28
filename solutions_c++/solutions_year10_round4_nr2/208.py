#include <algorithm>
#include <iostream>
#include <complex>
#include <numeric>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(),(a).end()
#define sz(a) int((a).size())
#define FOR(i,a,b) for(int i=a; i<b; ++i)
#define REP(i,n) FOR(i,0,n)
#define UN(a) sort(all(a)),(a).erase(unique(all(a)), (a).end())
#define CL(a,b) memset(a,b,sizeof a)
#define pb push_back
#define X first
#define Y second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

#define P 10
#define inf 1000000000

int n,p;
int m[1<<P];
int c[P][1<<P];
int f[1<<(P+1)][P+1];

int calc(int d,int k,int i,int j)
{
	if(f[i][j]==-1)
	{
		if(d==p)
		{
			if(i==13 && j>0)
			{
				int s=0;
			}
			if(m[k]<j)
				f[i][j]=inf;else
				f[i][j]=0;
		}else
		{
			f[i][j]=min(
				c[d][k]+calc(d+1,2*k,2*i,j)+calc(d+1,2*k+1,2*i+1,j),
				calc(d+1,2*k,2*i,j+1)+calc(d+1,2*k+1,2*i+1,j+1)
			);
			if(f[i][j]>inf)
				f[i][j]=inf;
		}
	}
	return f[i][j];
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int test;
	scanf("%d",&test);
	REP(t,test)
	{
		scanf("%d",&p);
		REP(i,1<<p)
			scanf("%d",&m[i]);
		REP(i,p)
			REP(j,1<<(p-i-1))
				scanf("%d",&c[p-i-1][j]);
		memset(f,-1,sizeof(f));
		printf("Case #%d: %d\n",t+1,calc(0,0,1,0));
	}
	return 0;
}
