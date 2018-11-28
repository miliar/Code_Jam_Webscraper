#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

const double EPS = 1e-10;
const double PI = acos(-1.0);
typedef long long int64;
#define MP(x, y) make_pair(x, y)
#define SZ(x) ((int)(x).size())
#define sqr(x) ((x) * (x))
template<class T> T gcd(T a, T b) { for (T c; b; c = a, a = b, b = c % b); return a; }
template<class T> void out(const vector<T> &a) { for (int i = 0; i < SZ(a); ++i) cout << a[i] << " "; cout << endl; }
int countbit(int n) { return n == 0 ? 0 : 1 + countbit(n & (n - 1)); }
const int d8[8][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {-1, -1}, {1, -1}, {-1, 1}};
const int d4[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
typedef complex<double> point;
inline int dcmp(double x) { return (x > EPS) - (x < -EPS); }
inline double cross(const point &a, const point &b) { return (conj(a) * b).imag(); }
inline double dot(const point &a, const point &b) { return (conj(a) * b).real(); }

typedef pair<int, int> ii;

struct Node
{
    int x, y;
    int w;
    Node() {}
    Node(int x, int y, int w): x(x), y(y), w(w) {}
};

bool operator <(const Node &a, const Node &b)
{
    return a.w < b.w;
}

int main()
{
    freopen("A-small-attempt2.in", "r", stdin); freopen("A.out", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int num = 1; num <= cas; ++num)
    {
        int X, S, R, n;
        double t;
        scanf("%d %d %d %lf %d", &X, &S, &R, &t, &n);
        vector<Node> a(n);
        for (int i = 0; i < n; ++i)
            scanf("%d %d %d", &a[i].x, &a[i].y, &a[i].w);
        vector<Node> b;
        int j = 0;
        for (int i = 0; i < n; ++i)
        {
            if (j < a[i].x)
                b.push_back(Node(j, a[i].x, S));
            b.push_back(Node(a[i].x, a[i].y, a[i].w + S));
            j = a[i].y;
        }
        if (j < X)
            b.push_back(Node(j, X, S));
        sort(b.begin(), b.end());
        double ret = 0;
        for (int i = 0; i < SZ(b); ++i)
        {
            double cost = (double)(b[i].y - b[i].x) / (b[i].w - S + R);
            if (t >= cost)
            {
                t -= cost;
                ret += cost;
            }
            else
            {
                ret += ((b[i].y - b[i].x) - (b[i].w - S + R) * t) / b[i].w + t;
                t = 0;
            }
        }
        printf("Case #%d: %.10f\n", num, ret);
    }
    return 0;
}
