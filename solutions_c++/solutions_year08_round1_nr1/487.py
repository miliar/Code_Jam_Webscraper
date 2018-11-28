/*
ID: ferromr1
PROG:
LANG: C++
*/
#include<cstdio>
#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<algorithm>
#include<numeric>
#include<cstdlib>
#include<cmath>
#include<set>
#include<map>
#include<ctime>
#include<utility>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz size()
#define all(qq) qq.begin(),qq.end()
#define rall(qq) qq.rbegin(),qq.rend()
#define clr(qq) memset((qq),0,sizeof(qq))
#define fill(qq) memset((qq),0x3F,sizeof(qq))
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define repd(i,n) for(int i=(int)(n-1);i>=0;i--)
#define rep2(i,a,b) for(int (i)=(int)(a);i<(int)(b);i++)
#define fore(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++)
#define rint(qq) int(floor(qq+0.5))
#define sqr(qq) ((qq) * (qq))
#define ll long long
#define inf 999999999
#define fi first
#define se second

int t,n;
int v1[10],v2[10];

int ccw()
{
	int ret=0;
	rep(i,n)
	{
		ret+=v1[i]*v2[i];
	}
	return ret;
}

int main ()
{
	scanf("%d",&t);
	rep(k,t)
	{
		scanf("%d",&n);
		rep(i,n) scanf("%d",&v1[i]);
		rep(i,n) scanf("%d",&v2[i]);
		sort(v1,v1+n);
		int ret=ccw();
		do
		{
			ret=min(ret,ccw());
		} while(next_permutation(v1,v1+n));
		printf("Case #%d: %d\n",k+1,ret);
	}
	return 0;
}
