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

int N;

int area(const string& path) {
    int ans = 0;
    int x = 0;
    int y = 0;
    int dx = 0;
    int dy = 1;
    FOR(i, path.size()) {
        switch (path[i]) {
            case 'R': swap(dx, dy); dy *= -1; break;
            case 'L': swap(dx, dy); dx *= -1; break;
            default:
                if (dx != 0)
                    ans += dx * y;
                x += dx;
                y += dy;
        }
    }
    return labs(ans);
}


void ff(const string& path) {
    int x = 3001;
    int y = 3001;
    int dx = 0;
    int dy = 1;
    N = 6005;
    VI mhor(N, N + 1), MHor(N, -1), mver(N, N  + 1), MVer(N, -1);
    FOR(i, path.size()) {
        switch (path[i]) {
            case 'R': swap(dx, dy); dy *= -1; break;
            case 'L': swap(dx, dy); dx *= -1; break;
            default:
                if (dx == 0) {
                    if (dy > 0) {
                        mhor[y] = min(mhor[y], x);
                        MHor[y] = max(MHor[y], x);
                        y += dy;
                    } else {
                        y += dy;
                        mhor[y] = min(mhor[y], x);
                        MHor[y] = max(MHor[y], x);
                    }
                } else {
                    if (dx > 0) {
                        mver[x] = min(mver[x], y);
                        MVer[x] = max(MVer[x], y);
                        x += dx;
                    } else {
                        x += dx;
                        mver[x] = min(mver[x], y);
                        MVer[x] = max(MVer[x], y);
                    }
                }
        }
    }
    int count = 0;
    FOR(i, N)
        FOR(j, N) {
            int add = 0;
            int mv = mver[i];
            int MV = MVer[i];
            int mh = mhor[j];
            int MH = MHor[j];
            if (mver[i] < MVer[i] && mver[i] <= j && MVer[i] > j)
                add = 1;
            if (mhor[j] < MHor[j] && mhor[j] <= i && MHor[j] > i)
                add = 1;
//            if (add == 1)
//                cerr << i <<" " <<  j << endl;
            count += add;
        }
    int rr = area(path);
    cout << (count - rr);
}

void main() {
    string sname = "A-large";
    FILE* in = freopen(("d:\\down\\" + sname + ".in").c_str(), "r", stdin);
    FILE* out = freopen(("d:\\contests\\usaco\\" + sname + ".out").c_str(), "w+", stdout);

    int T, L;
    cin >> T;
    FOR(q, T) {
        cin >> L;
        string path = "";
        FOR(j, L) {
            string r;
            cin >> r;
            int v;
            cin >> v;
            FOR(i, v)
                path += r;
        }
        cout << "Case #" << (q + 1) << ": ";
        ff(path);
        cout << endl;
    }
    fclose(in);
    fclose(out);
}
