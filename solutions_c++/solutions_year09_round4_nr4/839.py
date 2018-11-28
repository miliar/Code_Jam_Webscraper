#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <stack>
using namespace std;


typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<ll> VL;
typedef vector<VL> VVL;
typedef vector<char> VC;
typedef vector<VC> VVC;
typedef vector<string> VS;
typedef vector<VS> VVS;
typedef pair<int, int> PII;
const double INF = 1000000000;
double sol;

struct Planta{
    int x, y, r;
};

double dist(int x, int y, int a, int b) {
    return sqrt(double((x-a)*(x-a)+(y-b)*(y-b)));
}

int main() {
    cout.setf(ios::fixed);
    cout.precision(6);
    int k;
    cin >> k;
    int caso = 1;
    while (k--) {
        int n;
        cin >> n;
        vector<Planta> v(n);
        for (int i = 0; i < n; ++i) cin >> v[i].x >> v[i].y >> v[i].r;
        sol = INF;
        if (n == 3) {
            sol = min(max(dist(v[0].x, v[0].y, v[1].x, v[1].y) +v[0].r + v[1].r, double(2*v[2].r)), sol);
            sol = min(max(dist(v[0].x, v[0].y, v[2].x, v[2].y) +v[0].r + v[2].r, double(2*v[1].r)), sol);
            sol = min(max(dist(v[2].x, v[2].y, v[1].x, v[1].y) +v[2].r + v[1].r, double(2*v[0].r)), sol);
        }
        else if (n == 2) sol = max(v[0].r*2, v[1].r*2);
        else sol = v[0].r*2;
        cout << "Case #" << caso++ << ": " << sol/2.0 << endl;
    }
}

