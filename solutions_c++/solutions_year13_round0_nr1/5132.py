#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <complex>
#include <numeric>
#include <bitset>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define FOR(i, a, b) for (int i(a), _b(b); i < _b; ++i)
#define REP(i, n) FOR (i, 0, n)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define UN(a) sort(all(a)), (a).erase(unique(all(a)), (a).end())
#define CL(a, v) memset(a, v, sizeof a)
#define pb push_back
#define X first
#define Y second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

const int INF = 1000000000;
const ll INF_LL = 1000000000000000000LL;
const double pi = 2 * acos(0.0);

template<class T> void smin(T& a, T b) { if (a > b) a = b; }
template<class T> void smax(T& a, T b) { if (a < b) a = b; }
template<class T> T gcd(T a, T b) { return b == 0 ? a : gcd(b, a % b); }
template<class T> T sqr(T a) { return a * a; }

template<class T> void outp(const vector<T>& v) {
    REP(i, sz(v)) cout << v[i] << (i + 1 == sz(v) ? '\n' : ' ');
}
template<class T> void outp(T* v, int n) {
    REP(i, n) cout << *v++ << (i + 1 == n ? '\n' : ' ');
}

const int N = 4;
string a[N];
int num[256];

string status(int i, int j, int di, int dj) {
    num['T'] = num['X'] = num['O'] = num['.'] = 0;
    REP(k, N) {
        num[a[i][j]]++;
        i += di;
        j += dj;
    }
    if (num['X'] + num['T'] == N && num['T'] <= 1)
        return "X won";
    if (num['O'] + num['T'] == N && num['T'] <= 1)
        return "O won";
    return "";        
}

string status() {
    string res = "";
    REP(i, N) {
        res = status(i, 0, 0, 1);
        if (res != "") return res;
    }
    REP(i, N) {
        res = status(0, i, 1, 0);
        if (res != "") return res;
    }
    res = status(0, 0, 1, 1);
    if (res != "") return res;
    res = status(0, N - 1, 1, -1);
    if (res != "") return res;
    REP(i, N)
        REP(j, N)
            if (a[i][j] == '.')
                return "Game has not completed";
    return "Draw";
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int test;
    scanf("%d", &test);
    FOR (t, 1, test + 1) {
        REP(i, N)
            cin >> a[i];
        cout << "Case #" << t << ": " << status() << "\n";
    }
    cerr << endl << endl << "TIME: " << clock() << endl;
    return 0;
}
