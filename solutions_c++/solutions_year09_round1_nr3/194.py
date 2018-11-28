#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <list>
#include <cstdio>
#include <complex>
#include <stack>
#include <cctype>
#include <cstdlib>
#include <iostream>
#include <cstring>

#define X real()
#define Y imag()
#define PB push_back
#define MP make_pair
#define FR(i,n) for( long long i = 0; i < n; i ++ )
#define FOR(i,a,n) for(long long i = a; i < n; i ++)
#define FREACH(it,v) for( typeof(v.end()) it = v.begin(); it != v.end(); it ++ )
#define EPS 1e-9
using namespace std;

typedef long double ld;
typedef long long ll;



ld dp[41];

ll cmb[41][41];
int C,N;

ld chan;
ld res(int rem)
{
//    cout << "rem: " << rem << endl;
    if(rem==C) return 0.0;
    if(dp[rem]>-0.5) return dp[rem];
    ld ress=1.0;
    
    
    for(int nw=min(N,C-rem);nw>=max(1,N-rem);nw--)
    {
        int notnw=N-nw;        

    //    cout << "nw: " << nw << " prob: " << ((ld)(cmb[rem][notnw]*cmb[C-rem][nw])/(ld)chan) << endl;
        ress+=  ((ld)(cmb[rem][notnw]*cmb[C-rem][nw])/(ld)chan)*(res(rem+nw));        
    }
    
    if(rem>=N)
    {
     //   cout << "rdasd " << endl;
        ld pp=(ld)cmb[rem][N]/chan;
        ress=ress/(1.0-pp);
    }
 //   cout << "rem: " << rem << "res: " << ress << endl;
    
    dp[rem]=ress;
    return ress;

}

int main()
{
    int n;
    cin >> n;
    FR(i,n)
    {
        cmb[0][0]=1;
        cmb[1][0]=1;
        cmb[1][1]=1;
        FOR(j,2,41)
            FR(k,j+1)
        {
            if(k==0||k==j) cmb[j][k]=1;
            else cmb[j][k]=cmb[j-1][k-1]+cmb[j-1][k];
        }
        cin >> C >> N;
        chan = (ld) cmb[C][N];
//        cout << chan << endl;
        FR(i,C) dp[i]=-1.0;
        
        printf("Case #%d: ",i+1);   
   //     ld cc=res(0);
   //     cout << cc << endl;
        cout.precision(8);
        cout << res(0) << endl;
    }
}