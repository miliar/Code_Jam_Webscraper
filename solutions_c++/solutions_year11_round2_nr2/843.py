#include "local.h" // Pre-compiled header file for VC++, which includes below headers...
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <limits>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cstdarg>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstring>

#pragma region Utility
#define LEN(O)                  int((O).size())
#define FOR(I, M, N)            for(int I = int(M), CNT_##I = int(N); I < CNT_##I; ++I)
#define REP(I, N)               FOR(I, 0, N)
#define REV(I, N)               for(int I = int(N) - 1; I >= 0; --I)
#define EACH(T, IT, O)          for(T::iterator IT = (O).begin(); IT != (O).end(); ++IT)
#define ELEM(XS)                (XS).begin(), (XS).end()
#define MP                      make_pair
#define ___y                    first
#define ___x                    second

using namespace std;	
template <typename S, typename T> void fill_(S& buf, const T& x){fill_n(reinterpret_cast<T*>(&buf), sizeof(buf) / sizeof(T), x);}
template <typename T, int N> inline int countof(const T (&)[N]){return N;}
template <typename T> inline vector<T>& operator +=(vector<T>& ret, const T& x){ret.push_back(x);return ret;}
#pragma endregion

typedef long long ll_t;

int T, D, C;
int ps[210];
int vs[210];

bool ok(double t)
{
    double l = -1.0e13;
    REP(i, C){
        l = max(l, double(ps[i]) - t);
        const double r = double(ps[i]) + t;
        const double eps = 1e-9; // ???
        REP(v, vs[i] - 1)
            l += D;

        if(l >= r - eps)
            return false;

        if(i != C - 1)
            l += D;
    }

    return true;
}

int main(int argc, char* argv[])
{
    freopen("input.txt" , "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> T;

    FOR(caseNo, 1, T + 1){
        cin >> C >> D;
        REP(i, C) cin >> ps[i] >> vs[i];
        const int V = accumulate(vs, vs + C, 0);

        double l = 0.0, r = double(D) * V / 2.0 +1.0;
        REP(dummy, 256){
            double m = (l + r) / 2.0;
            if(ok(m))
                r = m;
            else
                l = m;
        }

        printf("Case #%d: %0.16f\n", caseNo, l);
    }

    return 0;
}
