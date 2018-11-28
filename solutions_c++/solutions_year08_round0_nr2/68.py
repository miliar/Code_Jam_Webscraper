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
#define INF 1000000000
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
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int n,test;
	for(cin>>n,test=1;test<=n;++test) {
		int t,na,nb;
		int h1,m1,h2,m2;
		cin>>t>>na>>nb;
		vector<pair<PII,int> > trips;
		REP(i,na) {
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			trips.pb(make_pair(PII(60*h1+m1,60*h2+m2),0));
		}
		REP(i,nb) {
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			trips.pb(make_pair(PII(60*h1+m1,60*h2+m2),1));
		}
		SORT(trips);
		int ans[2];
		multiset<int> trains[2];
		ans[0]=ans[1]=0;
		REP(i,SZ(trips)) {
			int side=trips[i].Y;
			if(!trains[side].empty()&&*trains[side].begin()<=trips[i].X.X) 
				trains[side].erase(trains[side].begin());
			else ans[side]++;
			trains[1-side].insert(trips[i].X.Y+t);
		}
		cout<<"Case #"<<test<<": "<<ans[0]<<" "<<ans[1]<<endl;
	}
	
	fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
	return 0;
} 
