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

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int n,test;
	
	for(cin>>n,test=1;test<=n;++test) {
		int r,c;
		cin>>r>>c;
		vector<string> clss(r);
		REP(i,r)cin>>clss[i];
		VVI cnt(2,VI(1<<c));
		int cur=0,pnxt=1;
		FORD(i,r-1,0) {
			int mask=0,s,nxt,cc;
			cnt[pnxt]=VI((1<<c),-INF);
			REP(j,c)if(clss[i][j]=='x')mask|=(1<<j);
			REP(snm,1<<c) {
				REP(m,1<<c) {
					nxt=0;
					s=snm|mask;
					cc=cnt[cur][snm];
					REP(k,c)
						if(m&(1<<k)) {
							if(s&(1<<k))goto end;
							if(k>0)nxt|=(1<<k-1),s|=(1<<k-1);
							if(k+1<c)nxt|=(1<<k+1),s|=(1<<k+1);
							cc++;
						}
					cnt[pnxt][nxt]=max(cnt[pnxt][nxt],cc);
					end:;
				}
			}
			swap(cur,pnxt);
		}
		int res=-INF;
		REP(s,(1<<c))res=max(res,cnt[cur][s]);
		cout<<"Case #"<<test<<": "<<res<<endl;
	}
	
	fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
	return 0;
} 
