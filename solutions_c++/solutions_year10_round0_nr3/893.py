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
typedef pair<tint,tint> pii;
typedef complex<double> pto;

typedef vector<tint> vi;
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
#define clr(x,c) memset(x,c,sizeof(x))

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

//#define cin ent
//#define cout sal

int main(){
	ifstream ent("");
	ofstream sal("");

	int maxcase;
	cin >> maxcase;
	forn( ncase, maxcase ){

		tint r,k,n;
		cin >> r >> k >> n;

		vi g(n);
		forn(i,n){
			cin >> g[i];
			g.pb(g[i]);
		}

		vpii d(n,pii(-1,-1));

		tint pos = 0, money = 0, round = 0;
		d[0] = pii(0,0);

		forn( i, min(r,n+2) ){
			tint p = pos, ch = 0;
			round++;
			while( p < pos+n && ch + g[p] <= k ){
				ch += g[p];
				p++;
			}
			pos = p%n;
			money += ch;
			if( d[pos].first == -1 ){
				d[pos] = pii( round , money );
			}else{
				d[pos] = pii( round - d[pos].first , money - d[pos].second );
				break;
			}
		}

// 		if( round < r ){
			r -= round;

switch (ncase+1){case 10:
	case 11: case 15: case 16: case 22:
D(ncase+1); D(r); D(round); D(money); D(d[pos]); D(r/d[pos].first); D(d[pos].second*(r/d[pos].first)); D(r%d[pos].first); D("----------");
}

			money += d[pos].second * ( r / d[pos].first );
			r %= d[pos].first;
			forn(i,r){
				tint p = pos, ch = 0;
				while( p < pos+n && ch + g[p] <= k ){
					ch += g[p];
					p++;
				}
				pos = p%n;
				money += ch;
			}
// 		}

		cout << "Case #" << ncase+1 << ": " << money << endl;
	}
}