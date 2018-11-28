#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <map>
#include <numeric>
#include <limits>
#include <cmath>
#include <algorithm>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define REPR(i,n) for(int i=(n-1);i>=0;--i)
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define FORR(i,z,n) for (int (i)=(n-1);(i)>=(z);--(i))
#define FOREACH(it,c) \
  for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define MP make_pair
#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define ALLOF(c) ((c).begin()), ((c).end())
#define UNIQUE(x) remove(unique((x).begin(),(x).end()),(x).end())
#define CLEAR(x,v) memset((x),(v),sizeof((x)))
#define FORS(i,x) for(int i=0;i<(int)(x).size();i++)

const double EPS = 1.0e-10;
const double INF = numeric_limits<double>::infinity();

typedef long double ld;
typedef vector<ld> VD;
typedef vector<ld> vector_t;
typedef vector<VD> mat;
typedef vector<int> VI;
 
void pivot(mat& A, VD& b, int n, int m, int bi, int nv) {
	ld pd = A[bi][nv];
	REP(j, n+m) A[bi][j] /= pd;
	b[bi] /= pd;
	REP(i, m+2) {
		if (i == bi) continue;
		ld pn = A[i][nv];
		REP(j, n+m) A[i][j] -= A[bi][j] * pn;
		b[i] -= b[bi] * pn;
	}
}

void reinvert(mat& A, VD& b, int n, int m, VI& bx) {
	REP(i,m) {
		int mxpivot=i;
		FOR(ii,i+1,m) if (fabsl(A[i][bx[ii]])>fabsl(A[i][bx[mxpivot]])) mxpivot=ii;
		swap(bx[i],bx[mxpivot]);
		pivot(A,b,n,m,i,bx[i]);
	}
}

// Minimizes $cx$, constraints $Ax=b$, $x>=0$
// Try to have rows in $A$ of norm 1
vector_t simplex(mat A, VD b, VD c) {
	const int n = c.size(), m = b.size(); // n vars, m eqs
	// modify b to non-negative
	REP(i, m) if (b[i] < 0) {
		REP(j, n) A[i][j] *= -1;
		b[i] *= -1;
	}
	// list of base/independent variable ids
	vector<int> bx(m), nx(n);
	REP(i, m) bx[i] = n + i; // aux in base
	REP(i, n) nx[i] = i; // real independent
	// extend A, b
	A.resize(m + 2);
	REP(i, m+2) A[i].resize(n + m, 0); // aux vars
	REP(i, m) A[i][n + i] = 1; // aux vars
	REP(i, m) REP(j, n) A[m][j] = A[m][j]+A[i][j]; // row m is phase 0 costs
	b.push_back(accumulate(ALL(b), ld(0))); // row m is phase 0 costs
	REP(j, n) A[m + 1][j] = -c[j]; // row m+1 is costs
	REP(i, m) A[m + 1][n + i] = -INF; // aux costs
	b.push_back(0);
	mat A_(A);
	VD b_(b);
	VI forbidden(n+m,false);
	// main optimization
	REP(phase, 2) {
		for (int nsteps=0;;++nsteps) {
			// select an independent variable to enter
			int ni = -1;
			REP(i, n) if (!forbidden[nx[i]] && A[m][nx[i]] > EPS && (ni < 0 || nx[i] < nx[ni])) ni = i;
			if (ni == -1) break;
			int nv = nx[ni];
			// select a base variable to leave
			vector_t bound(m);
			REP(i, m) bound[i] = (A[i][nv] < EPS ? INF : b[i] / A[i][nv]);
			if (!(*min_element(ALLOF(bound)) < INF)) return vector_t(n,INF); // unbounded
			int bi = 0;
			REP(i, m)
				if (bound[i] < bound[bi] - EPS ||
					(bound[i] < bound[bi] + EPS && bx[i] < bx[bi])) bi = i;
			// update
			swap(nx[ni], bx[bi]);
			if (false && nsteps%100==0) {
				A=A_;
				b=b_;
				reinvert(A,b,n,m,bx);
			}
			else pivot(A,b,n,m,bi,nv);
		}
		if (phase == 0) {
			if (b[m]>EPS) return vector_t(); // no solution
			REP(i, n+m) if (i>=n || A[m][i] < -EPS) forbidden[i]=true;
			swap(A[m], A[m + 1]);
			swap(b[m], b[m + 1]);
			swap(A_[m], A_[m + 1]);
			swap(b_[m], b_[m + 1]);
		}
	}
	vector_t x(n + m, 0);
	REP(i, m) x[bx[i]] = b[i];
	x.resize(n);
	return x;
}

int main() {
  int T;
  cin >> T;
  FORE(tcase,1,T) {
    int n;
    cin >> n;
    int eqs=(n-1)*(n-2)/2;
    int vars=n+1+eqs;
    mat A(eqs,VD(vars));
    VD b(eqs,0);
    VD c(vars,0);
    c[n]=1;
    int whereami=0;
    FOR(i,0,n-1) {
      int k;
      cin >> k;
      --k;
      for (int j=i+1;j<n;++j) {
        if (j==k) continue;
        A[whereami][k]=j-i;
        A[whereami][j]=i-k;
        A[whereami][i]=k-j;
        A[whereami][n]=1;
        A[whereami][whereami+n+1]=-1;
        b[whereami]=1000000;
        ++whereami;
      }
    }
    cerr << whereami << ' ' << eqs << endl;
    assert(whereami==eqs);
    VD x=simplex(A,b,c);
    cout << "Case #" << tcase << ":";
    if (x[n]>999000) cout << " Impossible";
    else for (int i=0;i<n;++i) cout << ' ' << int(x[i]+.5);
    cout << endl;
  }
}

