#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#include <sstream>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <iomanip>

using namespace std;



typedef long long LL;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<string> VS;

const int inf = (1<<30) - 1;
const int nil = -inf;

#define ABS(a) ((a)>0?(a):(-a))

const double eps = 1e-4;




void solve(int T) {
    LL n, k, b, t;
    VLL x;
    VLL v;
    cin >> n >> k >> b >> t;
    x.resize(n);
    v.resize(n);
    for(int i=0; i<n; i++)
        cin >> x[i];
    for(int i=0; i<n; i++)
        cin >> v[i];
    int swaps = 0;
    int count = 0;
    int bad = 0;
    for(int i=n-1; i>=0; i--) {
        if (x[i] + v[i]*t < b)
            bad++;
        else {
            count++;
            swaps += bad;
        }
        if (count == k)
            break;
    }
    if (count != k)
        cout << "Case #" << T+1 << ": " << "IMPOSSIBLE" << endl;
    else
        cout << "Case #" << T+1 << ": " << swaps << endl;
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin.sync_with_stdio(false);
    int N;
    cin >> N;
    for(int i=0; i<N; i++) {
        solve(i);
    }

    return 0;
}
