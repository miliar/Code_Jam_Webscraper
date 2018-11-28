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

int N, W;
VI data, CO;
VVI memo;

int ones(int n) {return n == 0 ? 0 : 1 + ones(n & (n - 1));}

bool ison(int mask, int r) {
    if (r < 0 || r >= W)
        return false;
    return ((mask & (1 << r)) != 0);
}

int GV(int r, int mask) {
    if (r >= N)
        return 0;
    int& res = memo[r][mask];
    if (res != -1)
        return res;
    res = 0;
    FOR(j, (1 << W)) {
        if (j & data[r])
            continue;
        bool bad = false;
        FOR(k, W)
            if (ison(j, k)){
                bad |= (ison(j, k - 1));
                bad |= (ison(j, k + 1));
                bad |= ison(mask, k - 1);
                bad |= ison(mask, k + 1);
            }
        if (bad)
            continue;
        int cnt = CO[j];
        res = max(res, cnt + GV(r + 1, j));
    }
    return res;
}

void ff() {
    memo = VVI(N, VI(1 << W, -1));
    int ans = GV(0, 0);
    cout << ans;
}


void main() {
    CO = VI(1 << 20);
    CO[0] = 0;
    SFOR(i, 1, CO.size())
        CO[i] = 1 + CO[i & (i - 1)];
    string sname = "C-small-attempt0";
//    string sname = "D-small";
    FILE* in = freopen(("d:\\down\\" + sname + ".in").c_str(), "r", stdin);
    FILE* out = freopen(("d:\\contests\\usaco\\" + sname + ".out").c_str(), "w+", stdout);

    int T;
    cin >> T;
    FOR(q, T) {
        cin >> N >> W;
        data = VI(N);
        FOR(i, N) {
            string s;
            cin >> s;
            data[i] = 0;
            FOR(j, s.length())
                if (s[j] == 'x')
                    data[i] |= (1 << j);
        }
        reverse(ALL(data));

        cout << "Case #" << (q + 1) << ": ";
        ff();
        cout << endl;
    }
    fclose(in);
    fclose(out);
}
