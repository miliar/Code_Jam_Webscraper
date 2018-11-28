#include <algorithm>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
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
#define INF 1000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	int N,test;
	for(cin>>N,test=1;test<=N;++test) {
		int k;
		string seq;
		cin>>k>>seq;
		int n=SZ(seq)/k;
		VI p;
		REP(i,k)p.pb(i);
		int res=INF;
		do {
			string seq2(SZ(seq),' ');
			REP(i,n) {
				REP(j,k)seq2[i*k+p[j]]=seq[i*k+j];
			}
			int cnt=0,prv=0;
			REP(i,SZ(seq2)) {
				if(prv!=seq2[i])cnt++;
				prv=seq2[i];
			}
			res=min(res,cnt);
		}while(next_permutation(ALL(p)));
/*		cerr<<seq<<" "<<SZ(seq)<<" "<<k<<endl;
		// init first
		REP(i,27)cnt[i]=0;
		REP(i,k)cnt[seq[i]-'a']++,cerr<<seq[i];
		cerr<<endl;
		int sumc=0;
		REP(i,27)if(cnt[i])sumc++;
		REP(i,27)
			if(cnt[i])len[cur][i]=sumc;
			else len[cur][i]=INF;
		REP(i,3)cerr<<len[cur][i]<<" ";
		cerr<<endl;
		//next
		FOR(kk,1,n) {
			REP(i,27) {
				cnt[i]=0;
				len[nxt][i]=INF;
			}
			REP(i,k)cnt[seq[k*kk+i]-'a']++,cerr<<seq[k*kk+i];
			cerr<<endl;
			int sumc=0;
			REP(i,27)if(cnt[i])sumc++;
			else {
				REP(i1,27)REP(i2,27)
					if(cnt[i2]&&i1!=i2)
						len[nxt][i2]=min(len[nxt][i2],len[cur][i1]+sumc-(cnt[i1]?1:0));
				REP(i,27)
					if(cnt[i]>1)
						len[nxt][i]=min(len[nxt][i],len[cur][i]+sumc);
			}
			swap(nxt,cur);
			REP(i,3)cerr<<len[cur][i]<<" ";
			cerr<<endl;
		}
		int res=len[cur][0];
		REP(i,27)res=min(res,len[cur][i]);*/
		printf("Case #%d: %d\n",test,res);
	}
	fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
	return 0;
}
