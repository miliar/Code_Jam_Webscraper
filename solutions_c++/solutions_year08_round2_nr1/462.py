#include <iostream>
#include <set>

using namespace std;

struct point {
    int x, y;
    point(int xx, int yy) : x(xx), y(yy) {}
};

bool operator<(const point& a, const point& b) {
    if (a.x < b.x || (a.x == b.x && a.y < b.y)) return true;
    return false;
}

struct prob {
    long n, A, B, C, D, x0, y0, M;
    typedef set<point> points_t;
    points_t pts;

    prob(long N, long a, long b, long c, long d, long X0, long Y0, long m) : n(N), A(a), B(b), C(c), D(d), x0(X0), y0(Y0), M(m) {
        long x = x0, y = y0;
        // cerr << "inserting " << x << " " << y << endl;
        pts.insert(point(x, y));
        for (int i = 1; i<n; ++i) {
            x = (x*A + B)%M;
            y = (y*C + D)%M;
            // cerr << "inserting " << x << " " << y << endl;
            pts.insert(point(x, y));
        }
    }
    
    int solve() {
        typedef points_t::const_iterator pit_t;
        int res = 0;
        for (pit_t i = pts.begin(); i != pts.end(); ++i) {
            pit_t j = i;
            for (++j; j != pts.end(); ++j) {
                pit_t k = j;
                for (++k; k != pts.end(); ++k) {
                    long X3 = i->x + j->x + k->x;
                    if (X3%3) continue;
                    long Y3 = i->y + j->y + k->y;
                    if (Y3%3) continue;
                    ++res;
                }
            }
        }
        return res;
    }
};

int main() {
    int C;
    cin >> C;
    for (int i=1; i<=C; ++i) {
        int n, A, B, C, D, x0, y0, M;
        cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
        prob p(n, A, B, C, D, x0, y0, M);
        int res = p.solve();
        cout << "Case #" << i << ": " << res << endl;
    }
}
