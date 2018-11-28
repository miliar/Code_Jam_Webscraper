#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cstring>
#pragma comment(linker, "/STACK:16777216")
using namespace std;
#define pb push_back
#define ppb pop_back
#define pi 3.1415926535897932384626433832795028841971
#define mp make_pair
#define x first
#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pii pair<int,int>
#define pdd pair<double,double>
#define INF 1000000000
#define FOR(i,a,b) for (int _n(b), i(a); i <= _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define L(s) (int)((s).size())
#define C(a) memset((a),0,sizeof(a))
#define VI vector <int>
#define ll long long
int a,b,c,d,i,j,n,m,k,kolt;
int mas[2001];
int dp[10001][11];
int cs[10001];
int rec(int l,int r,int v,int b)
{
	if (dp[v][b]!=-1) return dp[v][b];
	if (l==r-1)
	{
		dp[v][b]=INF;
		if (b>=mas[l]) dp[v][b]=0;
		return dp[v][b];
	}
	dp[v][b]=rec(l,(l+r)/2,v*2,b)+rec((l+r)/2,r,v*2+1,b);
	dp[v][b]=min(dp[v][b],rec(l,(l+r)/2,v*2,b+1)+rec((l+r)/2,r,v*2+1,b+1)+cs[v]);
	if (dp[v][b]>INF) dp[v][b]=INF;
	return dp[v][b];
}
vector<pair<pii,int> > ps;
void readcs(int l,int r,int v)
{
	if (l==r-1) return;
	ps.pb(mp(mp(l,r),v));
	readcs(l,(r+l)/2,v*2);
	readcs((r+l)/2,r,v*2+1);
}
inline bool my_cmp(const pair<pii,int> &a,const pair<pii,int> &b)
{
	int l1=a.x.y-a.x.x,l2=b.x.y-b.x.x;
	if (l1!=l2) return l1<l2; else
	return a<b;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&kolt);
	rep(hod,kolt)
	{
		scanf("%d",&m);
		n=1<<m;
		rept(i,n)
		{
			scanf("%d",&mas[i]);
			mas[i]=m-mas[i];
		}
		ps.clear();
		readcs(0,n,1);
		sort(all(ps),my_cmp);
		rept(i,L(ps))
		{
			scanf("%d",&cs[ps[i].y]);
		}
		memset(dp,-1,sizeof(dp));
		printf("Case #%d: %d\n",hod,rec(0,n,1,0));
	}
}
