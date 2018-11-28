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
#define INF 1000005
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
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int N,test;
	for(cin>>N,test=1;test<=N;++test) {
		int m,v,cur;
		cin>>m>>v;
		VI gt(m+1);
		VI ch(m+1);
		int res[m+1][2];
		for(int i=1;i<=(m-1)/2;++i)
			cin>>gt[i]>>ch[i];
		for(int i=(m-1)/2+1;i<=m;++i) {
			cin>>cur;
			res[i][cur]=0;
			res[i][1-cur]=INF;
		}
		FORD(i,(m-1)/2,1) {
			int add;
			res[i][0]=res[i][1]=INF;
			// AND
			if(gt[i]==1)add=0;
			else if(ch[i])add=1;
			else add=INF;
			REP(i1,2)REP(i2,2)
				res[i][i1&&i2]=min(res[i][i1&&i2],res[2*i][i1]+res[2*i+1][i2]+add);
			// OR
			if(gt[i]==0)add=0;
			else if(ch[i])add=1;
			else add=INF;
			REP(i1,2)REP(i2,2)
				res[i][i1||i2]=min(res[i][i1||i2],res[2*i][i1]+res[2*i+1][i2]+add);
		}
		cout<<"Case #"<<test<<": ";
		if(res[1][v]>=INF)cout<<"IMPOSSIBLE"<<endl;
		else cout<<res[1][v]<<endl;
	}


	fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
	return 0;
}
