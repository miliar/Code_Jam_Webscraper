#include <iostream>
#include <complex>
#include <vector>
#include <algorithm>
#include <cstdio>

#define REP(i,n) for (int i = 0; i < (int)n; ++i)
#define FOR(i,c) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)

using namespace std;

const double EPS = 1e-8;
const double INF = 1e12;

typedef complex<double> Point;

struct L: public vector<Point> 
{
    L(const Point &a, const Point &b) {
        push_back(a); push_back(b);
    }
};

double cross(const Point &a, const Point &b)
{
    return imag(conj(a) * b);
}

double dot(const Point &a, const Point &b) 
{
    return real(conj(a) * b);
}

int ccw(Point a, Point b, Point c)
{
    b -= a; c -= a;
    if (cross(b, c) > 0) return 1;
    if (cross(b, c) < 0) return -1;
    if (dot(b, c) < 0) return 2;
    if (norm(b) < norm(c)) return -2;
    return 0;
}

bool intersectSS(const L &s, const L &t) 
{
    return ccw(s[0], s[1], t[0]) * ccw(s[0], s[1], t[1]) <= 0 &&
           ccw(t[0], t[1], s[0]) * ccw(t[0], t[1], s[1]) <= 0;
}

int main(void)
{
    int nCase;
    int N, A, B;

    cin >> nCase;
    for (int c = 1; c <= nCase; c++) {
        cin >> N;

        vector<L> lines;
        REP(i, N) {
            cin >> A >> B;
            lines.push_back(L(Point(0, A), Point(10, B)));
        }

        int cnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = i+1; j < N; j++) {
                cnt += intersectSS(lines[i], lines[j]);
            }
        }

        cout << "Case #" << c << ": " << cnt << endl;
    }

    return 0;
}
