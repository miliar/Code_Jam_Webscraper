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

int N, S, Q;

void f(const VI& data) {
    VB used(S, false);
    int ans = 0;
    int us = 0;
    FOR(i, data.size()) {
        int v = data[i];
        if (used[v])
            continue;
        if (++us == S) {
            ans++;
            used = VB(S, false);
            us = 1;
        }
        used[v] = true;
    }
    cout << ans << endl;
}


void main() {
    FILE* in = freopen("d:\\contests\\usaco\\A-large.in", "r", stdin);
    FILE* out = freopen("d:\\contests\\usaco\\A-large.out", "w+", stdout);

    string s;
    getline(cin, s);
    int N1 = atoi(s.c_str());
    FOR(q, N1) {
        map<string, int> names;
        getline(cin, s);
        S = atoi(s.c_str());
        FOR(i, S) {
            getline(cin, s);
            names[s] = i;
        }
        getline(cin, s);
        Q = atoi(s.c_str());
        VI quer(Q);
        FOR(i, Q) {
            getline(cin, s);
            quer[i] = names[s];
        }
        cout << "Case #" << (q + 1) << ": ";
        f(quer);
    }
    fclose(in);
    fclose(out);

}
