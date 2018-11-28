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

int N, M, A;

string imposs = "IMPOSSIBLE";
void ff() {
    FOR(x1, N + 1) SFOR(x2, x1, N + 1) {
        lint c = x2 - x1;
        SFOR(x3, x2, N + 1) {
            if (x3 == x2 && x2 == x1)
                continue;
            lint a = x3 - x2;
            lint b = x3 - x1;
            if (b * M < A)
                continue;
            FOR(y1, M + 1)  {
                lint r = A - a * y1;
                FOR(y3, M + 1) {
                    lint r1 = r - c * y3;
                    r1 *= -1;
                    /*                    lint y2 = 0;
                    if (b != 0)
                    y2 = r / b;
                    if (y2 < 0 || y2 > M)
                    continue;
                    if (y2 * b != r)
                    continue;*/
                    FOR(y2, M + 1) {
                        if (y2 * b == r1) {
                            cout << x1 << " " << y1 << " "<< x2 << " "<< y2 << " "<< x3<< " " << y3;
                            return;
                        }
                    }
                }
            }
        }
    }
    cout << imposs;
}

void main() {
    string sname = "B-small-attempt4";
    FILE* in = freopen(("d:\\down\\" + sname + ".in").c_str(), "r", stdin);
    FILE* out = freopen(("d:\\contests\\usaco\\" + sname + ".out").c_str(), "w+", stdout);

    int T;
    cin >> T;
    FOR(q, T) {
        cin >> N >> M >> A;
        cout << "Case #" << (q + 1) << ": ";
        ff();
        cout << endl;
    }
    fclose(in);
    fclose(out);
}
