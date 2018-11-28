#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef unsigned 
long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define	MIN(a, b)	((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))

#define eps 1e-9
#define sqr(x) ((x) * (x))
#define gr(a, b) ((a) > (b) + eps)
#define ge(a, b) ((a) > (b) - eps)
#define le(a, b) ((a) < (b) + eps)
#define ls(a, b) ((a) < (b) - eps)
#define eq(a, b) ((a) > (b) - eps && (a) < (b) + eps) 


string FILE_IN, FILE_OUT ;

void setName() {
	string comm ;
  cin >> comm ;
  FILE_IN = "B-small.in" ;
	FILE_OUT = "B-small.out" ;
  if (comm [0] == 'l' || comm [0] == 'L') {
		FILE_IN = "B-large.in" ;
		FILE_OUT = "B-large.out" ;
	}
}
double dis(double x1, double y1, double z1, double x2, double y2, double z2) {
	return sqrt(sqr(x1 - x2) + sqr(y1 - y2) + sqr(z1 - z2)) ;
}

double dot(double x1, double y1, double z1, double x2, double y2, double z2) {
	return x1 * x2 + y1 * y2 + z1 * z2 ;
}

int n ;
double x [1000], y [1000], z [1000], vx [1000], vy [1000], vz [1000] ;
double cx, cy, cz, cvx, cvy, cvz ;
double tmin, dmin ;

int main(int argc, char **argv) {
	setName() ;	    
	ifstream in(FILE_IN.c_str()) ;
	ofstream out(FILE_OUT.c_str()) ;

	int numTest ;	
	in >> numTest ;
	for (int test = 1 ; test <= numTest ; test ++) {
		
		in >> n ;
		cx = 0 ; cy = 0 ; cz = 0 ; 
		cvx = 0 ; cvy = 0 ; cvz = 0 ;
		
		for (int i = 0 ; i < n ; i ++) {
			in >> x [i] >> y [i] >> z [i] >> vx [i] >> vy [i] >> vz [i] ;
			cx += x [i] ; cy += y [i] ; cz += z [i] ;
			cvx += vx [i] ; cvy += vy [i] ; cvz += vz [i] ;
		}
		cx /= n ; cy /= n ; cz /= n ;
		cvx /= n ; cvy /= n ; cvz /= n ;
		
		tmin = - dot(cx, cy, cz, cvx, cvy, cvz) / sqr(dis(0, 0, 0, cvx, cvy, cvz)) ;
				
		if (le(tmin, 0.0) || (eq(cvx, 0) && eq(cvy, 0) && eq(cvz, 0))) {
			tmin = 0.0 ;
			dmin = dis(0, 0, 0, cx, cy, cz) ;
		}
		else {
			dmin = dis(0, 0, 0, cx + tmin * cvx, cy + tmin * cvy, cz + tmin * cvz) ;
		}
		
		out << "Case #" << test << ": " << dmin << " " << tmin << endl ;
	}
	
	in.close() ;
	out.close() ;
}
