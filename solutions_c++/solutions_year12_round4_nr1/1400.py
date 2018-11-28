
#include <algorithm>
#include <cfloat>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;
#define FOR(i,a,b) for(int i=a; i<(int)b; i++)
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef pair <ll, ll> pll;
#define debug(x) cerr << #x << " = " << (x) << \
" (L" << __LINE__ << ")" << " " << __FILE__ << endl;
template <class T> void debugall(T a, T b) { cerr << " (L" << __LINE__ << ") "; for(T i = a; i != b; i++) cerr << *i << ", "; cerr << endl; }

int dp[10001][10001];
vector <pll> tsuta;
int d;
int n;

bool rec(int prev, int cur){
    if(dp[prev][cur] != -1) return dp[prev][cur];
    ll dist = min(tsuta[cur].second, tsuta[cur].first - tsuta[prev].first);
    ll right = tsuta[cur].first + dist;
    if(d <= right) return true;
    bool flg = false;
    FOR(i,cur+1,n){
        if(tsuta[i].first > right) break;
        if(rec(cur, i)){
            flg = true;
            break;
        }
    }
    return (dp[prev][cur] = flg);
}

int main() {
	int zz;
	cin >> zz;
	FOR(z, 0, zz){
        cin >> n;
        memset(dp, -1, sizeof(dp));
        tsuta.clear();
        FOR(i,0,n){
            int a,b;
            cin >> a >> b;
            tsuta.pb(mp(a,b));
        }
        cin >> d;

        bool res = false;
        int dist = tsuta[0].first * 2;
        if(d <= dist) res = true;
        FOR(i,1,n){
            if(tsuta[i].first > dist) break;
            if(rec(0,i)){
                res = true;
                break;
            }
        }
        
        cout << "Case #" << z+1 << ": ";
        cout << (res ? "YES" : "NO") << endl;
	}
}
