#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>
#include <complex>
#include <cstdio>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef complex<double> pnt;
typedef pair<int, int> pii;

#define RA(x) (x).begin(), (x).end()
#define FE(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int) (x).size())

template<class T>
void splitstr(const string &s, vector<T> &out)
{
    istringstream in(s);
    out.clear();
    copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
}

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

struct plant
{
    pnt pos;
    ll rad;
};

static vector<plant> plants;
static int N;

static inline double sqr(double x) { return x * x; }

static bool try_it(double R)
{
    vector<ll> masks;
    for (int p1 = 0; p1 < N; p1++)
    {
        const plant &P1 = plants[p1];
        double r1 = P1.rad;

        masks.push_back(1LL << p1);
        for (int p2 = 0; p2 < N; p2++)
        {
            if (p1 == p2) continue;

            const plant &P2 = plants[p2];
            double r2 = P2.rad;

            double d = abs(P1.pos - P2.pos);
            if (2 * R - r1 - r2 < d) continue;
            double xmy = (sqr(R - r1) - sqr(R - r2)) / d;
            double x = (d + xmy) * 0.5;
            double h = sqrt(max(0.0, sqr(R - r1) - sqr(x)));
            pnt vec = (P2.pos - P1.pos) / d;
            pnt c = pnt(x, h) * vec + P1.pos;

            assert(fabs(abs(P1.pos - c) - (R - r1)) <= 1e-7);
            assert(fabs(abs(P2.pos - c) - (R - r2)) <= 1e-7);
            ll mask = (1LL << p1) | (1LL << p2);
            for (int i = 0; i < N; i++)
            {
                if (abs(plants[i].pos - c) <= R - plants[i].rad + 1e-9)
                    mask |= 1LL << i;
            }
            masks.push_back(mask);
        }
    }

    for (int i = 0; i < SZ(masks); i++)
    {
        if (masks[i] == (1LL << N) - 1)
            return true;
        for (int j = i + 1; j < SZ(masks); j++)
            if ((masks[i] | masks[j]) == (1LL << N) - 1)
                return true;
    }
    return false;
}

int main()
{
    int cases;
    cin >> cases;
    for (int cas = 0; cas < cases; cas++)
    {
        cin >> N;
        plants.resize(N);
        double left = 0.0;
        double right = 2000.0;
        for (int i = 0; i < N; i++)
        {
            cin >> plants[i].pos.real() >> plants[i].pos.imag() >> plants[i].rad;
            if (plants[i].rad > left)
                left = plants[i].rad;
        }
        while (right - left > 1e-7)
        {
            double mid = (left + right) * 0.5;
            if (try_it(mid))
                right = mid;
            else
                left = mid;
        }
        printf("Case #%d: %.9f\n", cas + 1, (left + right) * 0.5);
    }
    return 0;
}
