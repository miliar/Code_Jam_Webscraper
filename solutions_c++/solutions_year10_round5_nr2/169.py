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

const int len = 1000001;

long long f[len], m;
int n, a[105];

int main()
{
    freopen("b1.in", "r", stdin);
    freopen("b1.out", "w", stdout);
    
    int t2;
    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        cin >> m >> n;
        memset(f, 100, sizeof(f));
        f[0] = 0;
        int am = 0;
        for (int i = 1; i <= n; ++i) {
            cin >> a[i];
            for (int j = a[i]; j < len; ++j)
                f[j] <?= f[j - a[i]] + 1;
            am >?= a[i];
        }
        long long ret = (long long)(1e18);
        for (int j = 0; j < len && j <= m; ++j)
            if (!((m - j) % am)) ret <?= (m - j) / am + f[j];
        printf("Case #%d: ", t1);
        if (ret <= m) cout << ret << endl;
        else cout << "IMPOSSIBLE" << endl;

    }
    
    return 0;
}
