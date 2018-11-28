/*
TASK: 
LANG: C++
USER: smilitude1
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
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define SET(t,v) memset((t), (v), sizeof(t))
#define sz size()
#define pb push_back
#define i64 long long
#define ALL(x) x.begin(), x.end()

#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define REV(x) reverse( ALL( x ) )

#define IO freopen("b.in","r",stdin); freopen("b.out","w",stdout);
#define debug(x) cerr << __LINE__ <<" "<< #x " = " << x << endl

string s;
bool bad() {
	string r = s;
	sort( ALL(r) ); REV( r );
	return s == r;
}

int t, ncase = 0;
bool print() {
	string r = s;
	sort( ALL( r ) );
	int first = -1;
	REP(i,r.sz) if( r[i] != '0' && ( first == -1 || r[i] < r[first] ) ) first = i;
	string ans = "";
	ans += r[ first ];
	ans += "0";
	REP(i,r.sz) if( i == first ) continue; else ans += r[ i ];
	printf("Case #%d: %s\n", ++ncase, ans.c_str() );
}

bool smaller( string& a, string& b ) {
	int n = a.sz;
	REP(i,n) if( a[i] < b[i] ) return true; else if( a[i] > b[i] ) return false;
	return false;
}

int main() {
	
	 IO

	scanf("%d",&t);
	while( t-- ) {
		cin >> s;
		if( bad() ) print();
		else {
			int n = s.sz;
			string r, ans = "";
	//		cout << s << endl;
			REP(i,n) {
				// i am moving i to some place;
				int j = -1;
				for(int k=i-1; k>=0; k--) if( s[i] > s[k] ) { j = k;  break; }
				if( j == -1 ) continue;

	//			cout << " for " << i <<" " << j << endl;

				r = "";
				string ss = s;
				REP(l,n) if( l == i ) continue; else if( l == j ) r += ss[i], r += ss[l]; else r += ss[l];
				string rr = r; 
	//			cout << rr << endl;
				for(int p=j+1; p<n; p++) for(int q=p+1; q<n; q++) if( rr[p] > rr[q] ) swap( rr[p], rr[q] );
				if( ans == "" || smaller( rr , ans ) ) if( smaller( s, rr ) ) ans = rr;
			}
			printf("Case #%d: %s\n", ++ncase, ans.c_str() );
		}
	}

	return 0;
}
