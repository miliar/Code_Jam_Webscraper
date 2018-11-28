#include <iostream>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cassert>
using namespace std;
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz(x) ((int)((x).size()))
#define rep(i, N) for (int i = 0; i < N; ++i)
#define foreach(it,v) for(__typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define print(x) cerr<<#x<<" = ";pr(x);cerr<<endl;
#define PRC(l,r) pr(l);foreach(it,v)pr(it==v.begin()?"":","),pr(*it);pr(r);
template<class T>void pr(T x){cerr<<x;} 
template<class T>void pr(vector<T>v){PRC('[',']');} 
template<class T1,class T2>void pr(pair<T1,T2>x){pr(x.first);pr(':');pr(x.second);} 
template<class T>void pr(set<T>v){PRC('{','}');} 
template<class T1,class T2>void pr(map<T1,T2>v){PRC('{','}');}
typedef long long lint;
typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;

void solveTestCase(int tst) {
    int n;
    scanf("%d", &n);
    int xr = 0, mn = 1 << 30, s = 0;
    for (int i = 0; i < n; ++i) {
        int x;
        scanf("%d", &x);
        s += x;
        mn = min(x, mn);
        xr ^= x;
    }
    cout << "Case #" << tst << ": ";
    if (xr) cout << "NO" << endl;
    else cout << s - mn << endl;
}

int main() {
    int tst;
    cin >> tst;
    for (int i = 1; i <= tst; ++i)
        solveTestCase(i);
    return 0;
}
