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
#define EPS 1e-9
#define FREACH(it,v) for( typeof(v.end()) it = v.begin(); it != v.end(); it ++ )

using namespace std;

typedef long long ll;
typedef long double ld;


ll grp[1000];
ll money[1010]; // money strictly before this time
int vis[1010]; // time at which it was visited

int main() {
    int T;
    scanf("%d",&T);
    FR(i,T) {
        printf("Case #%d: ",i+1);
        ll R,k,N;
        scanf("%lld %lld %lld",&R,&k,&N);
        FR(j,N) scanf("%lld",&grp[j]);
        memset(vis,-1,sizeof(vis));
        vis[0]=0;
        money[0]=0;
        int cpos=0;
        int tm=0;
    
        
        ll bcy,ecy;
        for(;;) {
       //     cout << "cpos: " << cpos << endl;
            int pbeg=cpos;
            ll acum=0;
            while(acum<=k&&!(cpos==pbeg&&acum>0)) {
                if(acum+grp[cpos]>k) break;
                acum+=grp[cpos];
                cpos++;
                if(cpos==N) cpos=0;
            }
            
         //   cout << "pcpos: " << cpos << endl;
         //   cout << vis[cpos] << endl;
            
            tm++;
            money[tm]=money[tm-1]+acum;
            if(vis[cpos]!=-1) {
                bcy=vis[cpos];
                ecy=tm;
                break;
            } else vis[cpos]=tm;

        }
        
   //     cout << "bcy: " << bcy << " ecy: " << ecy << endl;
        
        assert(ecy>bcy);
        // we finish at time R
        
        if(bcy >= R) {
   //         cerr << "fsdf " << endl;
            cout << money[R] << endl;
        } else {
            ll res=money[bcy];
            res+= (money[ecy]-money[bcy])*( (R-bcy)/(ecy-bcy));
            res+=money[bcy+ ( (R-bcy)%( ecy-bcy) )] - money[bcy];
            cout << res << endl;
        }
        
    }
}