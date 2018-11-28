using namespace std;
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <sstream>
#include <iostream>
#include <memory.h>
#define FOR(i,n) for(__typeof(n) i=0;i<(n);i++)
#define FORab(i,a,n) for(__typeof(n) i=(a);i<=(n);i++)
#define FOR1(i,n) FORab(i,1,n)
#define pb push_back
#define ms(n,p) memset(n, (p), sizeof(n))
#define ms0(n) ms(n, 0)
#define sz(a) a.size()
#define all(a) a.begin(), a.end()
#define ABS(a) ((a)<0?(-(a)):(a))
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long ll;

int n, ans;
int num[20];
int chose[20];

void solve(int a) {
    if(a == n) {
        int c[2]={0, 0};
        int xr[2]={0, 0};
        FOR(i, n) {
            c[chose[i]] += num[i];
            xr[chose[i]] ^= num[i];
        }
        if(xr[0] != xr[1]) return;
        if(!c[0] || !c[1]) return;
        ans = max(max(c[0], c[1]), ans);
        return;
    }
    chose[a] = 0;
    solve(a+1);
    chose[a] = 1;
    solve(a+1);
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);

    int t;cin>>t;
    FOR1(cno, t) {
        cin>>n;
        FOR(i, n) cin>>num[i];
        ans = 0;
        solve(0);
        cout<<"Case #"<<cno<<": ";
        if(!ans) cout<<"NO"<<endl;
        else cout<<ans<<endl;
    }
    return 0;
}
