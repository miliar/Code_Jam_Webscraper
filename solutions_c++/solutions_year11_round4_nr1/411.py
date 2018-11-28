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
typedef vector<ll> VI;
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
typedef pair<ll, ll> PII;
typedef vector<PII> VPII;
typedef vector<double> VD;
typedef vector<VD> VVD;
const ll INF = 1000000000;
const double EPS = 1e-7;

struct Segment {
    ll a, b;
    ll speed;
};

bool comp(Segment a, Segment b) {
    return a.a < b.a;
}

bool comp2(Segment a, Segment b) {
    return a.speed < b.speed;
}

int main() {
    cout.setf(ios::fixed);
    cout.precision(8);
    ll casos;
    cin >> casos;
    for (ll cas = 1; cas <= casos; ++cas) {
        ll x, s, r, n;
        double t;
        cin >> x >> s >> r >> t >> n;
        vector<Segment> v(n);
        for (ll i = 0; i < n; ++i) {
            cin >> v[i].a >> v[i].b >> v[i].speed;
            v[i].speed += s;
        }
        sort(v.begin(), v.end(), comp);
        ll ini = 0;
        for (ll i = 0; i < n; ++i) {
            if (v[i].a > ini) {
                Segment aux;
                aux.a = ini;
                aux.b = v[i].a;
                aux.speed = s;
                v.push_back(aux);
            }
            ini = v[i].b;
        }
        if (ini < x) {
            Segment aux;
            aux.a = ini;
            aux.b = x;
            aux.speed = s;
            v.push_back(aux);
        }
        sort(v.begin(), v.end(), comp2);
        double res = 0;
        for (ll i = 0; i < v.size(); ++i) {
            if (t > EPS) {
                //cerr << v[i].a << " " << v[i].b << ": 1" << endl;
                double len = v[i].b - v[i].a;
                double time = len/(v[i].speed - s + r);
                if (time < t + EPS) {
                    t -= time;
                    res += time;
                }
                else {
                    double tros = (v[i].speed - s + r)*t;
                    t = 0;
                    res += (tros/(v[i].speed - s + r)) + ((len - tros)/v[i].speed);
                }
                //cerr << res << endl;
            }
            else {
                //cerr << v[i].a << " " << v[i].b << ": 2" << endl;
                double len = v[i].b - v[i].a;
                res += (len/v[i].speed);
                //cerr << res << endl;
            }
        }
        cout << "Case #" << cas << ": ";
        cout << res << endl;
    }
}
