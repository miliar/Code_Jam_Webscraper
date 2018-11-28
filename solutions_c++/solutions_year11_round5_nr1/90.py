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
#include <climits>
#include <fcntl.h>
#include <unistd.h>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef complex<int> pnt;
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

static void redirect(int argc, const char **argv)
{
    if (argc > 1)
    {
        int fd = open(argv[1], O_RDONLY);
        if (fd == -1) { perror(argv[1]); exit(1); }
        if (-1 == dup2(fd, 0)) { perror(argv[1]); exit(1); }
        if (-1 == close(fd)) { perror(argv[1]); exit(1); }
    }

    if (argc > 2)
    {
        int fd = open(argv[2], O_WRONLY | O_CREAT, 0666);
        if (fd == -1) { perror(argv[2]); exit(1); }
        if (-1 == dup2(fd, 1)) { perror(argv[2]); exit(1); }
        if (-1 == close(fd)) { perror(argv[2]); exit(1); }
    }
}

int main(int argc, const char **argv)
{
    redirect(argc, argv);

    int cases;
    cin >> cases;
    for (int cas = 0; cas < cases; cas++)
    {
        int W, L, U, G;
        double area = 0.0;
        cin >> W >> L >> U >> G;
        vector<pnt> lb(L), ub(U);
        for (int i = 0; i < L; i++)
        {
            cin >> lb[i].real() >> lb[i].imag();
        }
        for (int i = 0; i < U; i++)
        {
            cin >> ub[i].real() >> ub[i].imag();
        }
        for (int i = 1; i < U; i++)
            area += (ub[i].real() - ub[i - 1].real()) * (ub[i].imag() + ub[i - 1].imag());
        for (int i = 1; i < L; i++)
            area -= (lb[i].real() - lb[i - 1].real()) * (lb[i].imag() + lb[i - 1].imag());
        area /= G;

        double ap = 0.0;
        int lp = 0;
        int up = 0;
        double x = 0.0;
        vector<double> ans;
        while (x < W)
        {
            double ox = x;
            while (lb[lp].real() <= x)
                lp++;
            while (ub[up].real() <= x)
                up++;
            x = min(lb[lp].real(), ub[up].real());
            double lx0 = lb[lp - 1].real();
            double ly0 = lb[lp - 1].imag();
            double lx1 = lb[lp].real();
            double ly1 = lb[lp].imag();
            double ux0 = ub[up - 1].real();
            double uy0 = ub[up - 1].imag();
            double ux1 = ub[up].real();
            double uy1 = ub[up].imag();

            assert(lx0 <= ox && ox <= x && x <= lx1);
            assert(ux0 <= ox && ox <= x && x <= ux1);
            double oly = ly0 + (ly1 - ly0) * (ox - lx0) / (lx1 - lx0);
            double ouy = uy0 + (uy1 - uy0) * (ox - ux0) / (ux1 - ux0);
            double ly = ly0 + (ly1 - ly0) * (x - lx0) / (lx1 - lx0);
            double uy = uy0 + (uy1 - uy0) * (x - ux0) / (ux1 - ux0);
            double a = (uy + ouy - ly - oly) * (x - ox);
            while (SZ(ans) < G - 1 && ap + a > (SZ(ans) + 1) * area)
            {
                double target = (SZ(ans) + 1) * area;
                double A = (target - ap) / (x - ox);
                double h1 = ouy - oly;
                double h2 = uy - ly;
                double t;
                if (fabs(h2 - h1) < 1e-9)
                    t = (target - ap) / a;
                else
                    t = (-h1 + sqrt(h1 * h1 + A * (h2 - h1))) / (h2 - h1);
                ans.push_back(ox + t * (x - ox));
            }
            ap += a;
        }
        printf("Case #%d:\n", cas + 1);
        assert(SZ(ans) == G - 1);
        for (int i = 0; i < SZ(ans); i++)
            printf("%.9f\n", ans[i]);
    }
    return 0;
}
