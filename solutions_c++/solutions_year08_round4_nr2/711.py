#include <fstream>
using namespace std;

ifstream in("B.in");
ofstream out("B.out");

long long N, M, A;

#define ll long long

void solve() {
    ll x1, y1, x2, y2, x3, y3;
    x1 = 0;
    y1 = 0;
    for(x2 = 0; x2 <= M; ++x2)
        for(y2 = 0; y2 <= N; ++y2)
            for(x3 = 0; x3 <= M; ++x3) {
                y3 = A + x3 * y2;
                if(x2 == 0)
                    if(y3 == 0) {                    out << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3;
                    return;

                }
                    else
                        continue;
                if(y3 % x2 == 0 && y3 / x2 >= 0 && y3 / x2 <= N) {
                    y3 /= x2;
                    out << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3;
                    return;
                 }
            }
    y2 = 0;
    for(y1 = 0; y1 <= N; ++y1)
        for(x2 = 0; x2 <= M; ++x2)
            for(x3 = 0; x3 <= M; ++x3) {
                y3 = A + x2 * y1 - x3 * y1;
                if(x2 == 0)
                   if(y3 == 0) {
                                    out << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3;
                    return;
}
                    else
                    continue;
                if(y3 % x2 == 0 && y3 / x2 >= 0 && y3 / x2 <= N) {
                    y3 /= x2;
                    out << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3;
                    return;
                }
            }
    y3 = 0;
    for(y1 = 0; y1 <= N; ++y1)
        for(x2 = 0; x2 <= M; ++x2)
            for(x3 = 0; x3 <= M; ++x3) {
                y2 = -(A + x2 * y1 - x3 * y1);
                if(x3 == 0)
                   if(y2 == 0) {
                                    out << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3;
                    return;
}
                    else
                        continue;
                if(y2 % x3 == 0 && y2 / x3 >= 0 && y2 / x3 <= N) {
                    y2 /= x3;
                    out << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3;
                    return;
                }
            }

    /*
    for(ll x1 = 0; x1 <= 0; ++x1)
        for(ll y1 = 0; y1 <= 0; ++y1)
            for(ll x2 = 0; x2 <= M; ++x2)
                for(ll y2 = 0; y2 <= N; ++y2)
                    for(ll x3 = x2; x3 <= M; ++x3)
                        for(ll y3 = 0; y3 <= N; ++y3)
                            if(llabs(x1 * (y2 - y2) - x2 * (y1 - y3) + x3 * (y1 - y2)) == A) {
                                out << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3;
//                                return;
                            }
    for(ll x1 = 0; x1 <= 0; ++x1)
        for(ll y1 = 0; y1 <= N; ++y1)
            for(ll x2 = 0; x2 <= M; ++x2)
                for(ll y2 = 0; y2 <= 0; ++y2)
                    for(ll x3 = x2; x3 <= M; ++x3)
                        for(ll y3 = 0; y3 <= N; ++y3)
                            if(llabs(x1 * (y2 - y2) - x2 * (y1 - y3) + x3 * (y1 - y2)) == A) {
                                out << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3;
//                                return;
                            }
    for(ll x1 = 0; x1 <= 0; ++x1)
        for(ll y1 = 0; y1 <= N; ++y1)
            for(ll x2 = 0; x2 <= M; ++x2)
                for(ll y2 = 0; y2 <= N; ++y2)
                    for(ll x3 = x2; x3 <= M; ++x3)
                        for(ll y3 = 0; y3 <= 0; ++y3)
                            if(llabs(x1 * (y2 - y2) - x2 * (y1 - y3) + x3 * (y1 - y2)) == A) {
                                out << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3;
//                                return;
                            }
*/
    out << "IMPOSSIBLE";
}


int main() {
    int T;
    in >> T;
    for(int i = 1; i <= T; ++i) {
        in >> M >> N >> A;
        out << "Case #" << i << ": ";
        solve();
        if(i < T)
            out << "\n";
    }
    return 0;
}
