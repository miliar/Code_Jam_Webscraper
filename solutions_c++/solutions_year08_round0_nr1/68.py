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
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int n,test;
	for(cin>>n,test=1;test<=n;++test) {
		int s,q;
		string str;
		map<string,int> index;
		cin>>s;getline(cin,str);
		REP(i,s) {
			getline(cin,str);
			index[str]=i;
		}
		cin>>q;getline(cin,str);
		VI sw(q+1,q*q+5);
		VI last(s,-1);
		REP(i,q) {
			getline(cin,str);
			if(index.count(str))
				last[index[str]]=i;
			REP(j,s)
				if(last[j]<i)
					sw[i]=min(sw[i],last[j]<0?0:1+sw[last[j]]);
		}
		cout<<"Case #"<<test<<": "<<sw[q-1]<<endl;
	}
	
	
	fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
	return 0;
} 
