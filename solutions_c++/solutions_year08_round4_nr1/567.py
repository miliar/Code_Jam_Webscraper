#pragma warning(disable : 4018)
#include <map>
#include <assert.h>
#include <set>
#include <sstream>
#include <iostream>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <numeric>

#ifdef __GNUC__
typedef long long lint;
typedef unsigned long long ulint;
#else
typedef __int64 lint;
typedef unsigned __int64 ulint;
#endif

using namespace std;

#define FOR(iter, bound) for(size_t iter=0; iter < (bound); iter++)
#define SFOR(iter, start, bound) for (int iter = (start); iter<(bound); iter++)
#define ALL(C) C.begin(), C.end()
#define VSORT(vec) sort(ALL(vec))
#define MP(a, b) make_pair((a), (b))

typedef vector<string> VS;
typedef vector<VS> VVS;
typedef vector<int> VI;
typedef vector<lint> VL;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<double> VD;
typedef vector<vector<double> > VVD;
typedef pair<int, int> PII;
typedef vector<PII> VP;
typedef vector<VP> VVP;

VS Parse(string str, string look_for = " ", bool i_push_empty = false)
{
    VS ans;
    if (look_for.length() == 0)
    {
        ans.push_back(str);
        return ans;
    };
    string last = "";
    int pos = 0;
    while (true)
    {
        if (pos == str.length())
        {
            if (last.length() != 0)
                ans.push_back(last);
            return ans;
        };
        if (look_for.find(str[pos]) == string::npos)
            last.append(1, str[pos]);
        else
        {
            if (i_push_empty || last.length() != 0)
                ans.push_back(last);
            last = "";
        };
        pos++;
    };
    return ans;
};


template<class C>
void PRV(vector<C> vec)
{
    cout << "{";
    FOR(i, vec.size()) {cout << vec[i] << ",";};
    cout << "}";
};


lint GetLint(string ss)
{
    lint ans = 0;
    int pos = 0;
    while (pos < ss.length() && !isdigit(ss[pos]))
        pos++;
    while (pos < ss.length() && isdigit(ss[pos]))
        ans *= lint(10), ans += lint(ss[pos++] - '0');
    return ans;
}

int N, M;
VB change;
VI val;
int B;

int ch1(int v) {
    return 2 * (v + 1) - 1;
}

int ch2(int v) {
    return 2 * (v + 1);
}

int solve(int v, int need) {
    if (v >= M) {
        assert(ch1(v) >= N);
        return (val[v] == need) ? 0 : B;
    }
    int q1 = solve(ch1(v), need);
    int q2 = solve(ch2(v), need);
    int res = (val[v] == need) ? q1 + q2 : min(q1, q2);
    if (!change[v] || need != val[v])
        return res;
    return min(res, 1 + min(q1, q2));
}

void ff(int need) {
    B = 10000000;
    int x = solve(0, need);
    if (x > 200000)
        cout << "IMPOSSIBLE";
    else
        cout << x;
}

void main() {
    string sname = "A-large";
    FILE* in = freopen(("d:\\down\\" + sname + ".in").c_str(), "r", stdin);
    FILE* out = freopen(("d:\\contests\\usaco\\" + sname + ".out").c_str(), "w+", stdout);

    int T, need;
    cin >> T;
    FOR(q, T) {
        cin >> N >> need;
        change = VB(N);
        val = VI(N);
        M = (N - 1) / 2;
        FOR(i, M) {
            int q;
            cin >> val[i] >> q;
            change[i] = (q == 1);
        }
        FOR(i, (N + 1) / 2)
            cin >> val[M + i];
        cout << "Case #" << (q + 1) << ": ";
        ff(need);
        cout << endl;
    }
    fclose(in);
    fclose(out);
}
