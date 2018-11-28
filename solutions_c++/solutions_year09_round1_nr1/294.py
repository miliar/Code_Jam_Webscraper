#include<cstdio>
#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<stack>
#include<deque>
#include<queue>
#include<string>
#include<list>
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
#define sz(x) ((int)x.size())
#define all(qq) qq.begin(),qq.end()
#define rall(qq) qq.rbegin(),qq.rend()
#define clr(qq) memset((qq),0,sizeof(qq))
#define fill(qq) memset((qq),0x3F,sizeof(qq))
#define mset(qq,h) memset((qq),h,sizeof(qq))
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define repd(i,n) for(int i=(int)(n-1);i>=0;i--)
#define rep2(i,a,b) for(int (i)=(int)(a);i<(int)(b);i++)
#define fore(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++)

#define REP(i,n) for(__typeof(n) i=0;i<(n);++i)
#define REPS(i,n) for(int(i)=0;i<int(n.size());++i)
#define FOR(i,a,b) for(__typeof(b) i=(a);i<=(b);++i)
#define FORD(i,a,b) for(__typeof(a) i=(a);i>=(b);--i)
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define rint(qq) int(floor(qq+0.5))
#define sqr(qq) ((qq) * (qq))
#define LL long long
#define LD long double
#define inf 999999999
#define pii pair<int,int>
#define fi first
#define se second
#define PI 3.1415926535897932384626433832795
#define EPS 1e-11

#define MX 10000000

int T;
int happy[11][MX];

int ishappy(int x,int base)
{
	if (x==1) return 1;
	if (x<MX)
	{
		if (happy[base][x]>-1)
		{
			return happy[base][x];
		}
		if (happy[base][x]==-2)
		{
			return happy[base][x]=0;
		}
		happy[base][x]=-2;
	}
	int res=0,y=x;
	while(x>0)
	{
		res+=sqr(x%base);
		x/=base;
	}
	res=ishappy(res,base);
	if (y<MX) happy[base][y]=res;
	return res;
}

int main ()
{
	mset(happy,-1);
	scanf("%d",&T);
	getchar();
	rep(t,T)
	{
		string s;
		getline(cin,s);
		stringstream ss(s);
		vector<int> X(0);
		int x;
		while(ss>>x)
		{
			X.pb(x);
		}
		int ret=1,ok=0;
		do
		{
			++ret;
			ok=1;
			rep(i,sz(X))
			{
				if (!ishappy(ret,X[i]))
				{
					ok=0;
					break;
				}
			}
		} while(!ok);
		printf("Case #%d: %d\n",t+1,ret);
	}
	return 0;
}
