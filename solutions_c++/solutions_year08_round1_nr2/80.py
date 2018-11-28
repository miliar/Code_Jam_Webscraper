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

int N, P;
VVB shakes;
VI pref, cnt;

void ff() {
    VI data(N, 0);
    while (true) {
        bool ok = true;
        FOR(i, P) {
            if (cnt[i] > 0)
                continue;
            int v = pref[i];
            if (v == -1) {
                cout << "IMPOSSIBLE";
                return;
            }
            if (data[v] == 1)
                continue;
            data[v] = 1;
            ok = false;
            FOR(j, P)
                if (shakes[j][v])
                    cnt[j]--;
        }
        if (ok)
            break;
    }
    FOR(i, N)
        cout << data[i] << " ";
}

void main() {
    string sname = "B-large";
    FILE* in = freopen(("d:\\down\\" + sname + ".in").c_str(), "r", stdin);
    FILE* out = freopen(("d:\\contests\\usaco\\" + sname + ".out").c_str(), "w+", stdout);


    int N1;
    cin >> N1;
    FOR(q, N1) {
        cin >> N >> P;
        shakes = VVB(P, VB(N));
        pref = VI(P, -1);
        cnt = VI(P, 0);
        FOR(i, P) {
            int T;
            cin >> T;
            FOR(j, T) {
                int r1, r2;
                cin >> r1 >> r2;
                r1--;
                if (r2 == 1)
                    pref[i] = r1;
                else {
                    cnt[i]++;
                    shakes[i][r1] = true;
                }
            }
        }
        cout << "Case #" << (q + 1) << ": ";
        ff();
        cout << endl;
    }
    fclose(in);
    fclose(out);

}
