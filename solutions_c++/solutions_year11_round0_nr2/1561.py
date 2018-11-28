#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <numeric>
using namespace std;

typedef long long tint;
typedef pair<int,int> pii;
typedef complex<double> pto;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vpii;
typedef vector<bool> vb;
typedef vector<string> vs;

#define forn(i,n) forsn(i,0,(n))
#define forsn(i,s,n) for( tint ___n=tint(n), i=tint(s) ; i<___n ; ++i )
#define fordn(i,n) fordsn(i,0,(n))
#define fordsn(i,s,n) for( tint ___s=tint(s), i=tint(n)-1 ; i>=___s ; --i )
#define forit(i,b,e) for( typeof(b) i = (b); i != (e); ++i )
#define forall(i,c) forit(i,(c).begin(),(c).end())
#define fordall(i,c) forit(i,(c).rbegin(),(c).rend())
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define sz(a) ((int)(a).size())
#define pb push_back

#define dot(a,b) (conj(a)*(b)).real()
#define cross(a,b) (conj(a)*(b)).imag()

#define entre(a,b,c) ((a)<=(b)&&(b)<(c))
#define EPS 1e-9
#define eq(a,b) entre(-EPS,(a)-(b),EPS)
#define supeq(a,b) ((a)==(b)||eq(a,b)||eq(((a)-(b))/(a),0))

#define D(x)   cerr << __LINE__ << " :: " << #x << " = " << (x) << endl
#define DBG(x) cerr << __LINE__ << " :: " << #x << " = " << (x); cin.get()

template <class T> ostream& operator<<( ostream& o, vector<T>& v )
{ o << endl; forall(i,v) o << *i << ','; return o; }

template <class U, class V> ostream& operator<<( ostream& o, pair<U,V>& p)
{ o << '(' << p.first << ',' << p.second << ')'; return o; }

const int mx[] = {-1,0,1,0};
const int my[] = {0,-1,0,1};

const int inf=0x7fffffff;

// back_inserter(container);
// cin >> ws;


int main(){
	ifstream ent("2.in");
	ofstream sal("sol.out");

	int maxcase;
	ent >> maxcase;
	forn( ncase, maxcase ) {

		tint c, d, n;
		string s, t;
		map<pii,char> comb;
		vs opos(256);

		ent >> c;
		forn( i, c ) {
			ent >> s;
			comb.insert( make_pair( pii( s[0], s[1] ), s[2] ) );
			comb.insert( make_pair( pii( s[1], s[0] ), s[2] ) );
		}

		ent >> d;
		forn( i, d ) {
			ent >> s;
			opos[ s[0] ].pb( s[1] );
			opos[ s[1] ].pb( s[0] );
		}

		ent >> n >> s;

		forall( i, s ) {

			bool combined = false;
			t.push_back(*i);

			while ( t.size() > 1 ) {

				auto p = comb.find( pii( t[ t.size() - 1 ], t[ t.size() - 2 ] ) );
				if( p == comb.end() ) break;

				combined = true;
				t.resize( t.size() - 2 );
				t.push_back( p->second );
			}

			if( !combined && strpbrk( t.c_str(), opos[*i].c_str() ) )
				t.clear();
		}

		sal << "Case #" << ncase+1 << ": [";

		forn( i, ((int)t.size()) - 1 )
			sal << t[i] << ", ";

		if ( t.size() ) sal << t[ t.size() - 1 ];

		sal << "]\n";
	}
}