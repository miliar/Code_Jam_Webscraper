#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <cstdio>
#include <complex>
#include <stack>
#include <string>
#include <cctype>
#include <cstdlib>
#include <iostream>

#define X real()
#define Y imag()
#define PB push_back
#define MP make_pair
#define FR(i,n) for( long long i = 0; i < n; i ++ )
#define FOR(i,a,n) for(long long i = a; i < n; i ++)
#define EPS 1e-8
#define FREACH(it,v) for( typeof(v.end()) it = v.begin(); it != v.end(); it ++ )

using namespace std;

typedef long long ll;
typedef long double ld;

ll f[501];
ll f2[501][501];

const ll MOD=100003LL;


ll ex(ll n,ll pow)
{
    ll cur=n%MOD;
    ll res=1LL;
    while(pow>0)
    {
        if(pow&1)
        {
            res*=cur;
            res=res%MOD;
            pow--;
            
        }
        else
        {
            cur*=cur;
            cur=cur%MOD;
            pow >>= 1;
            
        }
    }
    return res;
}


ll ch(ll n, ll k) {
    k=min(n,n-k);
    ll res=1;
    for(long long a=1;a<=k;a++) {                    
        res*=(n-k+a);
        res%=MOD;
        res*=(ex(a,MOD-2));
        res%=MOD;
    }
    return res;
}

ll chs[501][501];
int main() {
    int T;
    scanf("%d",&T);
    
    /*
    g[0]=1;
    FOR(i,2,501) {
        g[i]=2*g[0];
        g[i]%=MOD;
    } */
    
    chs[0][0]=1;
    FOR(i,1,501) FOR(j,0,i+1) {
    //    cout << i << " " << j << endl;
        chs[i][j]=ch(i,j);
    }
    
    memset(f2,0,sizeof(f2));
    FOR(i,2,501) {
//        cout << i << endl;
        f[i]=1;
        f2[i][1]=1;
        FOR(le,2,i) {
            f2[i][le]=0;
            
            FOR(le2,1,le) {
                if(i-le-1>=le-le2-1) {
               //     if(i==4&&le==2) cout << "Fsf " << le2<< " " << f2[le][le2] << " " <<i-le-1 << " " <<le-le2-1 << chs[i-le-1][le-le2-1] <<  endl;
                    
                    f2[i][le]+=f2[le][le2]*chs[i-le-1][le-le2-1];      
                    f2[i][le]%=MOD;                    
                }
            }
            
            f[i]+=f2[i][le];
            f[i] %= MOD;
        }
        
        /*
        FOR(j,2,i) {
            f[i]+= (f[j]*g[i-j-1]) %MOD;
            f[i] %= MOD;
        }*/
        
        /*if(i<10) cout << "i: " << f[i] << endl;
        if(i<10)  FR(j,10) cout << "i j: " << j << "::" << f2[i][j] << endl;*/
        
    }
    
    
    FR(i,T) {
        int n;
        scanf("%d",&n);        
        printf("Case #%d: ",i+1);
        cout << f[n] << endl;

    }
}
