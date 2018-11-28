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

#define forn(i,n) forsn(i,0,n)
#define forsn(i,s,n) for( tint ___n=tint(n), i=tint(s) ; i<___n ; ++i )
#define fordn(i,n) fordsn(i,0,n)
#define fordsn(i,s,n) for( tint ___s=tint(s), i=tint(n)-1 ; i>=___s ; --i )
#define forall(i,c) for( typeof((c).begin()) i=(c).begin() ; i!=(c).end() ; ++i )
#define all(c) (c).begin(), (c).end()
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

//remember back_inserter(container);
//remember cin >> ws;

// #define cin ent
// #define cout sal
typedef vector<pair<string,int> >::iterator iter;
int count( string& s, int pos ){
	int sol = s[pos]!='/';
	forsn(i,pos,sz(s)) sol += s[i] == '/';
	return sol;
}

int main(){
	ifstream ent("A-large.in");
	ofstream sal("s1.out");

	int maxcase;
	ent >> maxcase;
	forn( ncase, maxcase ){

		tint sol = 0;

		int n, m;
		ent >> n >> m;
		vector<pair<string,int> > v(n+m);
		forn(i,n){
			ent >> v[i].first;
			v[i].second = 0;
		}
		forn(i,m){
			ent >> v[i+n].first;
			v[i+n].second = 1;
		}

		sort(all(v));
		if( v[0].second == 1 ) sol += count(v[0].first,0);
		forsn(i,1,n+m){
			int j;
			for(j=0;j<sz(v[i-1].first)&&j<sz(v[i].first);j++)
				if( v[i-1].first[j]!=v[i].first[j] )
					break;
			if( v[i].second && j<sz(v[i].first) )
				sol+=count(v[i].first,j);
		}
		D(sol);
		sal << "Case #" << ncase+1 << ": " << sol << endl;
	}
}