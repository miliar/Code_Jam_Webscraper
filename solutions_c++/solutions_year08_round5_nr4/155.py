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

int H, W, R;
VP rocks;
vector<lint> rev;
lint M = 10007;

lint countFact(int n, lint m) {
    if (m > n)
        return 0;
    return (n / m) + countFact(n, m * M);
}

lint CNK(int n, int k) {
    if (n - k > k)
        return CNK(n, n - k);
    lint CM = countFact(n, M) - countFact(n - k, M) - countFact(k, M);
    if (CM > 0)
        return 0;
    lint ans = 1;
    SFOR(i, k + 1, n + 1) {
        lint v = i;
        while ((v % M) == 0)
            v /= M;
        ans = (ans * (v % M)) % M;
    }
    SFOR(i, 1, n - k + 1) {
        lint v = i;
        while ((v % M) == 0)
            v /= M;
        ans = (ans * rev[(int)(v % M)]) % M;
    }
    return ans;
}

lint count(int x1, int y1, int x2, int y2) {
    int dx = x2 - x1;
    int dy = y2 - y1;
    if (dy <= 0 || dx <= 0)
        return 0;
    int total = dx + dy;
    if ((total % 3) != 0)
        return 0;
    total /= 3;
    int DD = dy - dx;
    int xjump = DD + total;
    int yjump = total - DD;
    if (xjump < 0 || yjump < 0)
        return 0;
    if ((xjump % 2) == 1 || (yjump % 2) == 1)
        return 0;
    xjump /= 2;
    yjump /= 2;
    return CNK(xjump + yjump, xjump);
}

int ones(int n) {return n == 0 ? 0 : 1 + ones(n & (n - 1));}

lint GV(int mask) {
    int px = 0;
    int py = 0;
    lint res = 1;
    FOR(i, R)
        if ((1 << i) & mask)  {
            res *= count(px, py, rocks[i].first, rocks[i].second);
            res %= M;
            px = rocks[i].first;
            py = rocks[i].second;
        }
    res *= count(px, py, H - 1, W - 1);
    return res % M;
}

void ff() {
    if (W == 1 && H == 1) {
        cout << 1;
        return;
    }
    VSORT(rocks);
    lint ans = 0;
    FOR(i, (1 << R)) {
        int mm = ones(i);
        lint rr = GV(i);
        if (mm % 2 == 0)
            ans = (ans + rr) % M;
        else 
            ans = (M * M + ans - rr) % M;
    }
    cout << ans;
}

int gv(int r, int c, const VVI& data) {
    if (r >= H || c >= W)
        return 0;
    return data[r][c];
}

void simple() {
    VVI data(H, VI(W, 0));
    data[H - 1][W - 1] = 1;
    for (int i = H - 2; i >= 0; i--)
        for (int j = W - 2; j >= 0; j--) {
            bool bad = false;
            FOR(k, R)
                bad |= (rocks[k].first == i &&rocks[k].second == j);
            if (bad)
                data[i][j] = 0;
            else 
                data[i][j] = (gv(i + 1, j + 2, data) + gv(i + 2, j + 1, data)) % M;
        }
    cout << data[0][0];
}

void main() {
    rev = vector<lint>((int)M, 0);
    SFOR(j, 1, M) {
        FOR(p, M)
            if ((p * j) % M == 1) {
                rev[j] = p;
                break;
            }
    }
    string sname = "D-small-attempt2";
//    string sname = "D-small";
    FILE* in = freopen(("d:\\down\\" + sname + ".in").c_str(), "r", stdin);
    FILE* out = freopen(("d:\\contests\\usaco\\" + sname + ".out").c_str(), "w+", stdout);

    int T;
    cin >> T;
    FOR(q, T) {
        cin >> H >> W >> R;
        rocks = VP();
        FOR(i, R) {
            int a, b;
            cin >> a >> b;
            rocks.push_back(MP(a - 1, b - 1));
        }
        cout << "Case #" << (q + 1) << ": ";
//        simple();
        ff();
        cout << endl;
    }
    fclose(in);
    fclose(out);
}
