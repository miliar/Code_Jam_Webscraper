#include <iostream>
#include <cstdio>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <stack>
#include <queue>
#include <map>
#include <sstream>
#include <ctime>
#include <numeric>
#include <cstring>
#include <functional>

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<PII> VPII;
typedef vector<string> VS;
typedef map<string, int> MSI;

#define REP(i, n) for (int i = 0; i < n; ++i)
#define FOR(i, a, b) for (int i = a; i < b; ++i)
#define FORD(i, a, b) for (int i = a-1; i >= b; --i)
#define ALL(x) x.begin(), x.end()
#define SIZE(x) (int)x.size()
#define FOREACH(it, c) for (__typeof(c.begin()) it = c.begin(); it != c.end(); ++it)
#define INF 987654321
#define PB push_back
#define MP make_pair
#define DEBUG(x) cerr<<#x<<": "<<x<<endl;
#define ERR(...) fprintf(stderr, __VA_ARGS__);
#define EPS 1e-9
#define INIT { REP(i,0);FOR(i,0,0);FORD(i,0,0);DEBUG("");ERR("\n");PII b=MP(SIZE(VI()), int(INF+EPS));VPII a;a.PB(b);VS s;}
#define ACC accumulate

class dir {
    public:
        dir() {};
        map<string, dir> files;
};

string isolate(string s) {
    if (s == "") return "";
    //if (s[0] == '/') s = s.substr(1);
    string ret;
    for (int i = 0; i < SIZE(s) && s[i] != '/'; ++i) 
        ret += s[i];
    return ret;
}

int add(string f, dir & d) {
    string next = isolate(f);
    if (next == "") return 0;
    //DEBUG(next);
    int ret = 0;
    if (d.files.count(next) == 0) {
        ++ret;
        d.files[next] = dir();
    }    
    ret += add(f.substr(SIZE(next)+1), d.files[next]);
    return ret;
}

int main(void) {
    int t;
    cin >> t;
    FOR(i, 1, t+1) {
        int n, m, res = 0;;
        cin >> n >> m;
        dir root;
        
        REP(k, n) {
            string nam;
            cin >> nam;
            nam += "/";
            int h = add(nam.substr(1), root);
            //DEBUG(h);
        }
        REP(k, m) {
            string nam;
            cin >> nam;
            nam += "/";
            int h;
            res += h = (add(nam.substr(1), root));
            //DEBUG(h);
        }
        cout << "Case #" << i << ": " << res << endl;
    }
    return 0;
}





