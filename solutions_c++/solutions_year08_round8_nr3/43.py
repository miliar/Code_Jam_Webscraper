#pragma warning(disable : 4018)
#define _CRT_SECURE_NO_WARNINGS
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
typedef vector<VL> VVL;
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

lint labs(lint v) {
    return v > 0 ? v : -v;
}

int ones(int k) {
    return k ? 1 + ones(k & (k - 1)) : 0;
}

int BIG = 1000000;

int N, K;
lint M = 1000000009;;
VVI conn;
VL fac;
VL memo;
VI father;
VL mult;


void go(int v, int prev) {
    FOR(i, conn[v].size())
        if (conn[v][i] == prev) {
            conn[v].erase(conn[v].begin() + i);
        }
    FOR(i, conn[v].size())
        go(conn[v][i], v);
    father[v] = prev;
}


void fillData()  {
    fac = VL(600);
    fac[0] = 1;
    SFOR(i, 1, fac.size())
        fac[i] = (i * fac[i - 1]) % M;
    mult = VL(600);
    mult[0] = 1;
    SFOR(i, 1, 600) {
        if (i > K)
            break;
        mult[i] = (mult[i - 1] * (K - i)) % M;
    }
    father = VI(N);
}

int computeFather(int v) {
    if (v == 0)
        return 0;
    int fath = father[v];
    int ans = conn[fath].size();
    if (fath != 0)
        ans++;
    return ans;
}

lint MMult(lint total, lint need)  {
    if (total < need)
        return 0;
    lint res = 1;
    FOR(i, need)
        res = (res * (total - i)) % M;
    return res;
}

lint GV(int v) {
    lint& res = memo[v];
    if (res != -1)
        return res;
    int child = conn[v].size();
    int cntF = computeFather(v);
    res = MMult(K - cntF, conn[v].size());
    FOR(i, conn[v].size())
        res = (res * GV(conn[v][i])) % M;
    return res;
}

void ff() {
    fillData();
    go(0, -1);
    memo = VL(N, -1);
    GV(0);
    cout << memo[0];
}



void main() {
//attempt0
    string sname = "C-large";
 FILE* in = freopen(("c:\\data\\" + sname + ".in").c_str(), "r", stdin);
   //FILE* in = freopen(("c:\\data\\" + sname + ".txt").c_str(), "r", stdin);
    FILE* out = freopen(("c:\\data\\output\\" + sname + ".out").c_str(), "w+", stdout);

    int T;
    cin >> T;

    

    FOR(q, T) {
        cin >> N >> K;
        conn= VVI(N, VI(0));
        FOR(i, N - 1) {
            int a, b;
            cin >> a  >> b;
            a--;
            b--;
            conn[a].push_back(b);
            conn[b].push_back(a);
        }
        cout << "Case #" << (q + 1) << ": ";


        ff();
        cout << endl;
    }



    fclose(in);
    fclose(out);
}

