#include <iostream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <string.h>
#include <bitset>
#include <cmath>
using namespace std;
/*
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
*/
#define int64 long long
#define real long double
#define xx first
#define yy second
#define ff q.front()
#define rr q.back()
#define all(x) (x).begin(), (x).end()
#define push_pair(x, y) push_back(make_pair(x, y))
#define vci vector <int>
#define vcs vector <string>
#define vcd vector <double>
#define vci64 vector <long long>
#define eps (1e-9L)
#define ifn (1000000000L)
#define maxint (2147483647)
#define pi (3.14159265358979323846264338327950288419716939937510L)
/*

struct hashf {
    size_t operator()(const vci &a) const
    {
        size_t ret;
        .......
        return ret;
    }
};

int64 val(string s)
{
    if (s.empty()) return 0;
    if (s[0] == '+') return val(s.substr(1));
    if (s[0] == '-')  return -val(s.substr(1));
    int64 a = 0;
    for (int i = 0; i < s.size(); ++i)
        a = a * 10 + s[i] - '0';
    return a;
}

string str(int64 x)
{
    char ss[20];
    sprintf(ss, "%lld", x);
    return ss;
}

vci read(string a)
{
    vci ret; int j = -1; a += '.';
    for (int i = 0; i < a.size(); ++i)
        if (a[i] < '0' || a[i] > '9') {
            if (i - j > 1) ret.push_back(val(a.substr(j + 1, i - j - 1)));
            j = i;
        }
    return ret;
}

struct point {
    double x, y;
    point(): x(0), y(0) {}
    point(double a, double b): x(a), y(b) {}
} p[105];

inline point operator+(const point &a, const point &b) {return point(a.x + b.x, a.y + b.y);}
inline point operator-(const point &a, const point &b) {return point(a.x - b.x, a.y - b.y);}
inline point operator*(const point &a, const double &k) {return point(a.x * k, a.y * k);}
inline point operator/(const point &a, const double &k) {return point(a.x / k, a.y / k);}
inline double cross(const point &a, const point &b, const point &c)
{
    return (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y);
}
inline point cpoint(const point &a, const point &b, const point &c, const point &d)
{
    double c1 = cross(a, b, c), c2 = cross(a, b, d);
    return (d * c1 - c * c2) / (c1 - c2);
}

*/

/*-------------------------------------------------------------------------------*/



/*-------------------------------------------------------------------------------*/

int t2, n, m, x, y, a[205];

int main()
{
    freopen("c1.in", "r", stdin);
    freopen("c1.out", "w", stdout);
    
    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        cin >> m;
        n = 0;
        while (m--) {
            cin >> x >> y;
            while (y--) a[++n] = x;
        }
        int ret = 0;
        do {
            bool ok = false;
            for (int i = 1; i < n; ++i)
                if (a[i] == a[i + 1]) {
                    --a[i], ++a[i + 1];
                    ok = true; ++ret;
                }
            if (!ok) break;
            sort(&a[1], &a[1] + n);
        }while (1);
        printf("Case #%d: %d\n", t1, ret);

    }
    
    return 0;
}
