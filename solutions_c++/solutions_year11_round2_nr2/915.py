#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stack>
#include <queue>
#include <cmath>
#include <string>
#include <string.h>
using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<VVI> VVVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<VVB> VVVB;
typedef vector<ll> VL;
typedef vector<VL> VVL;
typedef vector<VVL> VVVL;
typedef vector<char> VC;
typedef vector<VC> VVC;
typedef vector<VVC> VVVC;
typedef vector<string> VS;
typedef vector<VS> VVS;
typedef vector<VVS> VVVS;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
const double INF = 1e15;
const double EPS = 1e-7;

bool can(double m, int d, VI& v) {
    double ant = -INF;
    //cerr << "m :" << m << endl;
    for (int i = 0; i < v.size(); ++i ){
        //cerr << ant << " " << v[i] << endl;
        if (ant + d <= v[i] and v[i] - ant - d <= m) ant = ant + d;
        else if (ant + d >= v[i] and ant + d - v[i] <= m) ant = ant + d;
        else {
            if (ant < v[i] and v[i] - m >= ant + d) ant = v[i] - m;
            else return false;
        }
    }
    return true;
}

int main() {
    cout.setf(ios::fixed);
    cout.precision(10);
    int casos;
    cin >> casos;
    for (int cas = 1; cas <= casos; ++cas) {
        cout << "Case #" << cas << ": ";
        ll c, d;
        cin >> c >> d;
        VI v;
        for (int i = 0; i < c; ++i) {
            int p, n;
            cin >> p >> n;
            for (int j = 0; j < n; ++j) v.push_back(p);
        }
        double ini = 0, fin = INF;
        while (fin - ini > EPS) {
            double m = (ini+fin)/2;
            if (can(m, d, v)) fin = m;
            else ini = m;
        }
        cout << fin << endl;
    }
}
