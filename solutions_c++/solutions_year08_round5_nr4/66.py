#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <queue>
#include <iostream>
#include <iterator>
#include <math.h>
#include <cstdio>
#include <cstdlib>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long ll;

const int mod=10007;

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	int n,test;
	
	for(cin>>n,test=1;test<=n;++test) {
		int h,w,r;
		cin>>h>>w>>r;
		VPII bad(r);
		VVI cnt(h+1,VI(w+1));
		REP(i,r) {
			cin>>bad[i].X>>bad[i].Y;
			cnt[bad[i].X][bad[i].Y]=-1;
		}
		cnt[1][1]=1;
		FOR(i,1,h+1)FOR(j,1,w+1)
			if(cnt[i][j]==0) {
				if(i>1&&j>2&&cnt[i-1][j-2]!=-1)cnt[i][j]+=cnt[i-1][j-2];
				if(i>2&&j>1&&cnt[i-2][j-1]!=-1)cnt[i][j]+=cnt[i-2][j-1];
				cnt[i][j]%=mod;
			}
		printf("Case #%d: %d\n",test,cnt[h][w]);
	}
	
	fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
	return 0;
} 
