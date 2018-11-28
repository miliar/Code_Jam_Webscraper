#include <algorithm>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;

typedef vector<int> vi;
typedef vector<string> vs;

#define f(i,a,b) for(int i=(a);i<(b);++i)
#define fd(i,a,b) for(int i=(a);i>=(b);--i)
#define pb(_v,_a) (_v).push_back(_a)
#define sz size()
#define range(_a) (_a).begin(),(_a).end()
#define foreach(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define init(m,v) memset((m), (v), sizeof((m)))
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 

int dp[1001][1001];
int rocks[101][101];
int go(int r, int c) {
    if (r<0 || c<0) return 0;
    if (r == 0 && c == 0) return 1;
    if (rocks[r][c]) return 0;
    int &val = dp[r][c];
    if (val != -1) return val;
    val = (go(r-1, c-2) + go(r-2, c-1) ) % 10007;
    return val;
}
int main() {
    int n;
    cin>>n;
    f(test,1,n+1) {
        ll ans = 0;
        init(dp, -1);
        init(rocks, 0);
        int h, w, r;
        cin>>h>>w>>r;
        f(i,0,r) {
            int a,b;
            cin>>a>>b;
            rocks[a-1][b-1] = 1;
        }
        ans = go(h-1,w-1);
        cout<<"Case #"<<test<<": "<<ans<<endl;
    }
    return 0;
}
