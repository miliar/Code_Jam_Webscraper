#include <iostream>
#include <fstream>
#include <cstdio>
#include <sstream>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <iomanip>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
const double PI = acos(-1.0);

#define SZ size()
#define PB push_back
#define SORT(a) sort((a).begin(), (a).end())
#define REV(a) reverse((a).begin(), (a).end())
#define UNQ(a) (a).resize(unique((a).begin(), (a).end()) - (a).begin())
#define SUM(a) accumulate((a).begin(), (a).end(), 0)
#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define TR(i, a) for(__typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define SQR(x) ((x) * (x))
#define EUCL(x1, y1, x2, y2) (((x1) - (x2)) * ((x1) - (x2)) + ((y1) - (y2)) * ((y1) - (y2)))
#define MANH(x1, y1, x2, y2) (abs((x1) - (x2)) + abs((y1) - (y2)))
#define CROSS(x1, y1, x2, y2) ((x1) * (y2) - (y1) * (x2))
#define CROSS2(x1, y1, x2, y2, x0, y0) (((x1) - (x0)) * ((y2) - (y0)) - ((y1) - (y0)) * ((x2) - (x0)))
#define DOT(x1, y1, x2, y2) ((x1) * (x2) + (y1) * (y2))
#define DOT2(x1, y1, x2, y2, x0, y0) (((x1) - (x0)) * ((x2) - (x0)) + ((y1) - (y0)) * ((y2) - (y0)))
#define DEBUG(a) cout << #a << ": " << (a) << endl;
#define DEBUG1D(a, x1, x2) { cout << #a << ":"; for(int _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define DEBUG2D(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }


ll N, PD, PG;

bool solve()
{
    ll D = 100 / __gcd(PD, 100LL);
    if(D > N) return 0;
    ll WD = PD * D / 100;
    if(WD < D && PG == 100) return 0;
    if(WD > 0 && PG == 0) return 0;
    return 1;
}

int main()
{
    freopen("A.large.in", "r", stdin);
    freopen("A.large.out", "w", stdout);
    int testCnt;
    cin >> testCnt;
    for(int testInd = 1; testInd <= testCnt; testInd++){
        cin >> N >> PD >> PG;
        cout << "Case #" << testInd << ": " << (solve() ? "Possible" : "Broken") << endl;
    }
}










