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

#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define TR(i, a) for(__typeof(a.B) i = a.B; i != a.E; i++)

#define DEBUG(a) cout << #a << ": " << (a) << endl;
#define DEBUG1D(a, x1, x2) { for(int _i = (x1); _i < (x2); _i++){ cout << a[_i] << " "; } cout << endl; }
#define DEBUG2D(a, x1, x2, y1, y2) { for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << a[_i][_j] << " "; } cout << endl; } }

string toString(int x)
{
	stringstream ss;
	ss << x;
	return ss.str();
}

#define MAXN 100

int pos[MAXN], v[MAXN], N, K, B, maxT;
bool can[MAXN];

int res;
void solve()
{
    res = 0;
    if(!K){
        return;
    }
    FOR(i, 0, N){
        can[i] = (maxT * v[i] >= B - pos[i]);
    }
    int bad = 0, k = 0;
    for(int i = N - 1; i >= 0; i--){
        if(!can[i]){
            bad++;
            continue;
        }
        k++;
        res += bad;
        if(k >= K){
            break;
        }
    }
    if(k < K){
        res = -1;
    }
    return;
}

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int _T;
    fin >> _T;
    for(int _t = 1; _t <= _T; _t++){
        // reset
        memset(pos, 0, sizeof(pos));
        memset(v, 0, sizeof(v));
        memset(can, 0, sizeof(can));

        // input
        fin >> N >> K >> B >> maxT;
        FOR(i, 0, N){
            fin >> pos[i];
        }
        FOR(i, 0, N){
            fin >> v[i];
        }

        // output
        solve();
        fout << "Case #" << _t << ": " << (res == -1 ? "IMPOSSIBLE" : toString(res)) << endl;
    }
    return 0;
}
