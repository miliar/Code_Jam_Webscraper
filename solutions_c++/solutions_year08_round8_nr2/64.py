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

int N, M, CC;
VI a, b, cols;
int n1, n2, n3;

bool ok(int v) {
    return v == n1 || v == n2 || v == n3;
}

void simple() {
    int res = BIG + 1;
    FOR(i, CC)
        FOR(j, i + 1)
        FOR(k1, j + 1) {
            n1 = i;
            n2 = j;
            n3 = k1;
            VI memo(M + 1, BIG);
            memo[0] = 0;
            queue<int> q;
            q.push(0);
            while (q.size()) {
                int pos = q.front();
                q.pop();
                FOR(k, N)
                    if (ok(cols[k]) && a[k] <= pos && b[k] > pos) {
                        int v1 = b[k];
                        if (memo[v1] > memo[pos] + 1) {
                            q.push(v1);
                            memo[v1] = memo[pos] + 1;
                        }
                    }
            }
            res = min(res, memo[M]);
    }
    if (res >= BIG)
        cout <<  "IMPOSSIBLE" ;
    else
        cout << res;
} 


void ff() {
/*    FOR(i, N)
        FOR(j, i)
        if (20000 * a[i] + b[i] < 20000 * a[j] + b[j]) {
            swap(a[i], a[j]);
            swap(b[i], b[j]);
            swap(cols[i], cols[j]);
        }*/
    simple();
}



void main() {
//-attempt0
    string sname = "B-small-attempt1";
    FILE* in = freopen(("c:\\data\\" + sname + ".in").c_str(), "r", stdin);
//   FILE* in = freopen(("c:\\data\\" + sname + ".txt").c_str(), "r", stdin);
    FILE* out = freopen(("c:\\data\\output\\" + sname + ".out").c_str(), "w+", stdout);

    int T;
    cin >> T;

    FOR(q, T) {
        cin >> N;
        map<string, int> colors;
        a = VI(N);
        b = VI(N);
        cols = VI(N);
        string s;
        FOR(i, N) {
            cin >> s;
            cin >> a[i];
            a[i]--;
            cin >> b[i];
            if (colors.find(s) == colors.end()) {
                int sz = colors.size();
                colors[s] = sz;
            }
            cols[i] = colors[s];
        }


        cout << "Case #" << (q + 1) << ": ";

        CC = colors.size();
        M = 10000;

        ff();
        cout << endl;
    }



    fclose(in);
    fclose(out);
}
