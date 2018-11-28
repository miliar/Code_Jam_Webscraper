#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <cstring> 
#include <climits> 
#include <cfloat> 
#include <map> 
#include <utility> 
#include <set> 
#include <iostream> 
#include <memory> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <functional> 
#include <sstream> 
#include <complex> 
#include <stack> 
#include <queue> 
#include <numeric>
#include <cassert>

#define FOR(i, min, max) for (int i = (min); i < (max); ++i) 
#define FORE(i, min, max) for (int i = (min); i <= (max); ++i) 
#define REP(i, n) for (int i = 0; i < (n); ++i) 
#define REPV(vec, i) for (int i = 0; i < (int)(vec.size()); ++i) 
#define FOR_EACH(vec, it) for (typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); ++it)

using namespace std; 
static const double EPS = 1e-12; 
typedef long long ll; 

int N, B;
int Ns;  // ºÇÂç·å¿ô

ll MOD=1000000007;
inline ll add_m(ll a, ll b) { return (a + b) % MOD; }
inline ll sub_m(ll a, ll b) { return (a - b + MOD) % MOD; }
inline ll mul_m(ll a, ll b) { return (a * b) % MOD; }

vector<int> getVS(int n) {
    vector<int> ret;
    while(n) {
        ret.push_back(n % B);
        n /= B;
    }
    return ret;
}

bool check(const vector<int> &used, int n) {
    int p = 0;
    while(n) {
        int t = n % B;
        if (used[p] & (1<<t))
            return false;
        n /= B;
        ++p;
    }
    return true;
}

vector<int> setBit(const vector<int> &used, int n) {
    vector<int> ret = used;
    int p = 0;
    while(n) {
        int t = n % B;
        ret[p] = (ret[p] | (1<<t));
        n /= B;
        ++p;
    }
    return ret;
}

map<vector<int>, ll> mem[101][101];

ll solve(int sum, int max, vector<int> used) {
    assert(sum <= N);
    if (sum == N)
        return 1LL;
    if (mem[sum][max].find(used) != mem[sum][max].end())
        return mem[sum][max][used];
    ll ret = 0LL;
    FOR(i, max+1, N-sum+1) if (check(used, i))
        ret = add_m(ret, solve(sum+i, i, setBit(used, i)));
    return mem[sum][max][used] = ret;
}

int main(void)
{
    int T;
    cin >> T;
    REP(_t, T) {
        cin >> N >> B;
        Ns = getVS(N).size();
        REP(i, N+1) REP(j, N+1)
            mem[i][j].clear();
        vector<int> used(Ns, 0);
        ll ret = solve(0, 0, used);
        cerr << _t+1 << endl;
        cout << "Case #" << _t+1 << ": " << ret << endl;
    }
    return 0;
}

