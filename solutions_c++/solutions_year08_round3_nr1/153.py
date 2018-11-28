#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>
#include<numeric>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<list>
#include<iterator>
using namespace std;

#define REP(i,n) for(__typeof(n) i=0; i<(n); i++)
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define CLEAR(t) memset((t), 0, sizeof(t))

#define sz size()
#define pb push_back
#define pf push_front

#define VI vector<int>
#define VS vector<string>
#define LL long long

bool comp( LL a , LL b ) { return a > b; } 

int main() {
    int n;
    
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    
    cin >> n;
    REP(ncase, n ) {
        int p,k,l;
        cin >> p >> k >> l;
        vector<LL> f(l);
        REP(i,l) cin >> f[i];
        
        if( p*k < l ) {            
            printf("Case #%d: Impossible\n",ncase+1);
            continue;
        }
        
        LL ans = 0;
        sort( f.begin(), f.end() , comp );
        REP(i,f.sz) {
            ans += f[i]*( i/k + 1 ); 
        }
        
        printf("Case #%d: %lld\n",ncase+1, ans);
    }
    //system("pause");

    return 0;
}
