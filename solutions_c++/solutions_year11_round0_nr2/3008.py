#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <sstream>
#include <stack>
#include <queue>
#include <numeric>
#include <functional>
using namespace std;
#define pb push_back 
#define mp make_pair
#define sz(v) ((int)(v).size()) 
#define rep(i,n) for(int i=0;i<(n);++i) 
#define all(a) (a).begin(),(a).end()
#define foreach(i, a) for(__typeof((a).begin()) i=(a).begin();i!=(a).end();++i)
#define inf (1LL << 29)
typedef long long ll;
typedef vector<int> vi;

string check_combine(string& invoke, map<string, string>& combine) {
    string ret = invoke;
    while (sz(ret) >= 2) {
        string last_pair;
        last_pair += ret[sz(ret)-1];
        last_pair += ret[sz(ret)-2];
        if (combine.count(last_pair) == true) {
            ret = ret.substr(0, sz(ret)-2);
            ret += combine[last_pair];
        } else {
            break;
        }
    }    
    return ret;
}

string check_opposed(string& invoke, vector<string>& opposed) {
    string ret = invoke;
    for (int i = 0; i < sz(opposed); ++i) {
        string& key = opposed[i];
        int pos1 = ret.find(key[0]);
        int pos2 = ret.find(key[1]);
        if (pos1 != string::npos && pos2 != string::npos) {
            return "";
        }
    }
    return ret;
}

string solve() {
    int C, D, N;
    string com, opp, inv;
    cin >> C; if (C) cin >> com;
    cin >> D; if (D) cin >> opp;
    cin >> N >> inv;

    map<string, string> combine;
    for (int i = 0, j = 0; i < C; ++i, j+=3) {
        string src, dst;
        src += com[j];
        src += com[j+1];
        dst += com[j+2];
        combine[src] = dst;
        swap(src[0], src[1]);
        combine[src] = dst;
    }
    vector<string> opposed;
    for (int i = 0, j = 0; i < D; ++i, j+=2) {
        string o;
        o += opp[j];
        o += opp[j+1];
        opposed.pb(o);
    }
    string invoke;
    for (int i = 0; i < sz(inv); ++i) {
        invoke += inv[i];
        invoke = check_combine(invoke, combine);
        invoke = check_opposed(invoke, opposed);
    }
    string ret;
    ret += "[";
    for (int i = 0; i < sz(invoke); ++i) {
        if (i) ret += ", ";
        ret += invoke[i];
    }
    ret += "]";
    return ret;
}

main() {
    ios_base::sync_with_stdio(false);

    int T; cin >> T;
    for (int testcase = 1; testcase <= T; ++testcase) {
        cout << "Case #" << testcase << ": " << solve() << '\r' << endl;
    }
}
