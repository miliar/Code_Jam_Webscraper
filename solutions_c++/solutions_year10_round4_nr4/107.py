#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <cstring> 
#include <climits> 
#include <cfloat> 
#include <map> 
#include <utility> 
#include <set> 
#include <iostream> 
#include <memory> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <functional> 
#include <sstream> 
#include <complex> 
#include <stack> 
#include <queue> 
#include <numeric>
#include <cassert>

#define FOR(i, min, max) for (int i = (min); i < (max); ++i) 
#define FORE(i, min, max) for (int i = (min); i <= (max); ++i) 
#define REP(i, n) for (int i = 0; i < (n); ++i) 
#define REPV(vec, i) for (int i = 0; i < (int)(vec.size()); ++i) 
#define FOR_EACH(vec, it) for (typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); ++it)

using namespace std; 
static const double EPS = 1e-12; 
typedef long long ll; 

long double getR(pair<long double, long double> a, pair<long double, long double> b) {
    long double dx = a.first-b.first;
    long double dy = a.second-b.second;
    return sqrt(dx*dx+dy*dy);
}

long double getArea(long double d, long double r1, long double r2) {
//    assert(4*d*d*r1*r1-pow((d*d+r1*r1-r2*r2), 2.0) > -EPS);
    long double A = r1*r1*acos((d*d+r1*r1-r2*r2)/(2*d*r1))
        +r2*r2*acos((d*d+r2*r2-r1*r1)/(2*d*r2))
        -0.5*sqrt(4*d*d*r1*r1-pow((d*d+r1*r1-r2*r2), 2.0));
    return A;
}

vector<long double> solve(vector<pair<long double, long double> > &P, vector<pair<long double, long double> > &Q) {
    int N = P.size();
    int M = Q.size();
    assert(N == 2);
    long double d = getR(P[0], P[1]);
    vector<long double> ret;
    REP(i, M) {
        long double ri = getR(P[0], Q[i]);
        long double rj = getR(P[1], Q[i]);
        long double area = getArea(d, ri, rj);
        ret.push_back(area);
    }
    return ret;
}

int main(void)
{
    int T;
    cin >> T;
    REP(_t, T) {
        int N, M;
        cin >> N >> M;
        vector<pair<long double, long double> > P(N), Q(M);
        REP(i, N)
            cin >> P[i].first >> P[i].second;
        REP(i, M)
            cin >> Q[i].first >> Q[i].second;
        vector<long double> ret = solve(P, Q);
        cout << "Case #" << _t+1 << ":";
//        cout.precision(10);
        REP(i, M)
            printf(" %.8Lf", ret[i]);
//            cout << " " << ret[i];
        cout << endl;
    }
    return 0;
}

