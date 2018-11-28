#include <fstream>
#include <algorithm>
using namespace std;

typedef long long LL;
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define PRE(c,l,e) (find((c),(c)+(l),(e)) != (c)+(l))
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)

inline int ndi(int a) {
    if (a == 0) return 1;
    int d = 0;
    while (a) { d++; a /= 10; };
    return d;
}

inline int dig(int a, int n) {
    while (n--) a /= 10;
    return a % 10;
}

inline int nrot(int n, int a, int b) {
    int opd = 10, opm = 1, difn[8] = {n}, ndif = 1;
    while (opm < n) opm *= 10;

    REP(i, ndi(n)-1) {
        int cn = (n % opd) * (opm / opd) + (n / opd);
        
        if (cn < n && cn >= a && cn <= b) return 0;
        if (cn < n && (cn < a && cn > b)) continue;

        if (cn >= a && cn <= b && !PRE(difn,8,cn)) {
            difn[ndif++] = cn;
        }
        opd *= 10;
    }
    return ndif*(ndif-1)/2;
}

int main(int argc, char const *argv[]) {
    ifstream in ("C-large.in");
    ofstream out ("C-large.out");

    int t;
    in >> t;
    REP(ca, t) {
        int a, b;
        LL so = 0;
        in >> a >> b;
        FOR(i,a,b) so += nrot(i,a,b);
        out << "Case #" << ca+1 << ": " << so << endl;
    }
    return 0;
}
