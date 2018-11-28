#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;
#define REP(i,n) for(int i=0,n_=(n);i<n_;i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FOR(i,a,b) for (int i=a,b_=b;i<=(b_);i++)
#define ALL(a) a.begin(),a.end()
#define SZ(a) (int)(a).size()
#define SORT(a) sort(ALL(a))
#define INF 1073741823
#define DEB(x) cerr<<#x<<":"<<x<<"\n"
#define PB(b) push_back(b)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define DEBV(b) FOREACH(it,b) cerr<<(*it)<<"\n";cerr <<"\n";
set<pair<int,int> > P;
int dx[]={1,2};
int dy[]={2,1};
long long DP[120][120];
long long MOD=10007;
int W;
int H,R;
long long go (int x,int y)
{
	if (P.find (make_pair(x,y))!=P.end())
		return 0;
//	DEB(x);DEB(y);
	if (x>H||y>W)
		return 0;
	if (x==H&&y==W)
	{
		return 1;
	}
	if (DP[x][y]!=-1)
	{
		return DP[x][y];
	}
	long long &Y=DP[x][y];
	Y=0;
	Y=(Y+go (x+dx[0],y+dy[0]))%MOD;
	Y=(Y+go (x+dx[1],y+dy[1]))%MOD;
	return Y;
}
int main ()
{
	int c,cas=1;
	scanf ("%d",&c);
	
	freopen ("output","w",stdout);
	while (c--)
	{
		
		scanf ("%d%d%d",&H,&W,&R);	
		P.clear();
		REP(i,R)
		{
			int x,y;
			 scanf ("%d%d",&x,&y);
			 P.insert(make_pair(x,y));
		}
		memset(DP,-1,sizeof DP);
		long long y=go (1,1);
		printf ("Case #%d: ",cas++);
		cout<<y;
		
	
		printf ("\n");
	}
	fclose(stdout);
}
