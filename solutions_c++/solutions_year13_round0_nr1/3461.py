#include <iostream> 
#include <sstream> 
#include <cstring>
#include <string> 
#include <vector> 
#include <queue> 
#include <stack>
#include <deque> 
#include <set> 
#include <map> 
#include <algorithm> 
#include <utility> 
#include <functional> 
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <ctime> 

using namespace std; 

const double pi = acos(-1.); 
typedef long long ll;
typedef pair<int,int> pii;
template<typename T> inline string Str(const T &a) {stringstream s;s<<a;return s.str();} 
template<typename T> inline int Int(const T &a) {stringstream s;s<<a;int r;s>>r;return r;} 
template<typename T> inline ll Long(const T &a) {stringstream s;s<<a;ll r;s>>r;return r;} 
template<typename T> inline double Double(const T &a) {stringstream s;s<<a;double r;s>>r;return r;}  

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,a) FOR(i,0,a)
#define all(a) a.begin(),a.end()
#define clr(a) memset(a, 0, sizeof(a))
#define debug(a) cerr << #a << ":" << (a) << endl;
#define len(a) ((int) a.size())
#define foreach(itr,c) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();++itr) 
#define X first
#define Y second
#define PB push_back
#define MP make_pair
inline bool check_dot(string s) {
    rep(i,len(s)) if (s[i] == '.') return true;
    return false;
}
inline char check_same(string s) {
    char vis = 0;
    rep(i,len(s))
        if (s[i] == 'T') continue;
        else if (!vis) vis = s[i];
        else if (vis != s[i]) return 0;
    return vis;
} 
string data[10];
int n;
int main() {
    string res;
    cin >> n;
    rep(z,n) {
        rep(i,4) cin >> data[i];
        FOR(i,4,8) {
            data[i] = "";
            rep(j,4) data[i] += data[j][i-4];
        }
        data[8] = data[9] = "";
        rep(i,4) {
            data[8] += data[i][i];
            data[9] += data[i][3-i];
        }
        // rep(i,10) cerr << data[i] << endl;
        // cerr << endl;
        bool flga = false, ff = false, flag = false;
        rep(i,10) if (!check_dot(data[i])) {
            flga = true;
            char c = check_same(data[i]);
            if (c) {res = c; res += " won"; ff = true; break;}
        } else flag = true;
        if (!ff)
        if (flag)res = "Game has not completed";
        else res = "Draw";
        printf("Case #%d: %s\n", z+1, res.c_str());
    }
	return 0;
}