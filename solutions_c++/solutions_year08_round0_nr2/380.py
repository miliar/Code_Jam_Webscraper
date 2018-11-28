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

int T, NA, NB;

VI depA, depB, arrA, arrB;

void readTT(int N, VI& dep, VI& arr) {
    string s;
    dep.resize(N);
    arr.resize(N);
    FOR(i, N) {
        getline(cin, s);
        VS dd = Parse(s, ": ");
        dep[i] = atoi(dd[0].c_str()) * 60 + atoi(dd[1].c_str());
        arr[i] = atoi(dd[2].c_str()) * 60 + atoi(dd[3].c_str());
    }
}

void f() {
    int sA = 0;
    int sB = 0;
    int hA = 0;
    int hB = 0;
    FOR(t, 24*60) {
        FOR(i, NA)
            if (t == T + arrA[i])
                hB++;
        FOR(i, NB)
            if (t == T + arrB[i])
                hA++;
        FOR(i, NA)
            if (t == depA[i] && --hA < 0) {
                hA = 0;
                sA++;
            }
        FOR(i, NB)
                if (t == depB[i] && --hB < 0) {
                    hB = 0;
                    sB++;
                }
    }
    cout << sA << " " << sB;
}

void main() {
    FILE* in = freopen("d:\\contests\\usaco\\B-large.in", "r", stdin);
    FILE* out = freopen("d:\\contests\\usaco\\B-large.out", "w+", stdout);

    string s;
    getline(cin, s);
    int N1 = atoi(s.c_str());
    FOR(q, N1) {
        getline(cin, s);
        T = atoi(s.c_str());
        getline(cin, s);
        VS ss = Parse(s);
        NA = atoi(ss[0].c_str());
        NB = atoi(ss[1].c_str());
        readTT(NA, depA, arrA);
        readTT(NB, depB, arrB);
        cout << "Case #" << (q + 1) << ": ";
        f();
        cout << endl;
    }
    fclose(in);
    fclose(out);

}
