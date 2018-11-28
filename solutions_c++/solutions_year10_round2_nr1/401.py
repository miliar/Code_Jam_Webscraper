/*
TASK:  
ALGO:
LANG: C++
USER: smilitude
DATE: 2010-05-23 Sun 12:14 AM	
*/

#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for( __typeof(b) i=(a); i<=(b); i++)
#define FORD(i,a,b) for(__typeof(a) i=(a); i>=(b); i--) 
#define SET(t,v) memset((t), (v), sizeof(t))
#define sz size()
#define pb push_back
#define i64 long long
#define ALL(x) x.begin(), x.end()
#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define REV(x) reverse( ALL( x ) )
#define IO freopen("","r",stdin); freopen("","w",stdout);
#define bug(x) if(1) cerr << __LINE__ <<" "<< #x " = " << x << endl
#define VI vector<int>
#define VS vector<string>

int ret = 0, ncase;
void print() {
	printf("Case #%d: %d\n", ++ncase, ret );
}

struct data {
	map<string,int> m;
};

data d[1000000];
int nd;

void insert( vector<string>& v ) {
	int p = 0;
	REP(i,v.sz) {
		if( d[p].m.find( v[i] ) == d[p].m.end() ) {
			ret ++;
			d[p].m[ v[i] ] = ++nd;
			d[nd].m.clear();
			p = nd;
		}else p = d[p].m[ v[i] ];
	}
}

int main() {
	int t, n, m;
	scanf("%d",&t);
	while( t-- ) {
		scanf("%d %d",&n,&m);
		nd = 0;
		d[0].m.clear();
		REP(i,n) {
			char b[1005];
			scanf("%s",b);
			int len = strlen( b );
			REP(j,len) if( b[j] == '/' ) b[j] = ' ';
			stringstream ss( b );
			vector<string> v; string s;
			while( ss >> s ) v.pb( s );
			insert( v );
		}

		ret = 0;
		REP(i,m) {
			char b[1005];
			scanf("%s",b);
			int len = strlen( b );
			REP(j,len) if( b[j] == '/' ) b[j] = ' ';
			stringstream ss( b );
			vector<string> v; string s;
			while( ss >> s ) v.pb( s );
			insert( v );
		}
		
		print();
	}

	return 0;
}

