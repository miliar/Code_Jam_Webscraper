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
#define INFLL 1000000000000000001LL
int a,b,c,d,i,j,n,m,k,kolt,lim;
ll len,ans;
int mas[101];
int gcd(int a,int b)
{
	return b?gcd(b,a%b):a;
}
int dp[2][10105],now,last;
inline ll checkdp(int len,int *mas,int n)
{
	if (len<0) return INFLL;
	memset(dp,63,sizeof(dp));
	now=0,last=1;
	dp[now][0]=0;
	rept(i,n)
	{
		now^=1; last^=1;
		rept(j,10105)
		{
			dp[now][j]=dp[last][j];
			if (j>=mas[i]) dp[now][j]=min(dp[now][j],dp[now][j-mas[i]]+1);
		}
	}
	if (dp[now][len]>=INF) return INFLL; else
	return dp[now][len];
}
int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&kolt);
	srand(25091992^kolt);
	rep(hod,kolt)
	{
		cerr<<hod<<endl;
		printf("Case #%d: ",hod);
		scanf("%I64d%d",&len,&n);
		rept(i,n) scanf("%d",&mas[i]);
		sort(mas,mas+n); reverse(mas,mas+n);
		ans=INFLL;
		ll rr=len/mas[0];
		rept(i,101)
		{
			ll rz=checkdp(len-mas[0]*(rr-i),mas+1,n-1);
			if (rz==INFLL) continue;
			ans=min(ans,rr-i+rz);
		}
		if (ans==INFLL) printf("IMPOSSIBLE\n"); else
		printf("%I64d\n",ans);
	}
}
