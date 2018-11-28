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
#define INF 10000000000LL;
using namespace std;

typedef long long ll;
typedef long double ld;


ll dp[3000][11];

int cont[3000];


int main() {
    int T; scanf("%d",&T);
    FR(i,T) {
        printf("Case #%d: ",i+1);
        int P;
        cin >> P;
        FOR(i,(1<<P)-1,(1<<(P+1))-1) {
            cin >> cont[i];
        }
        
        
        int first=(1<<P)-1;
        int n=(1<<P);
        n>>=1;
   //     cout << "first: " << first << endl;
        first-=n;
   //     cout << "first: " << first << endl;
        FR(i,P) {
            int idx=first;
 //           cout << "idx: " << idx << endl;
            FR(j,n) cin >> cont[idx++];            
            n>>=1;
            first-=n;
        }
        
        assert(first==0);
        
      //  FR(i,(1<<(P+1))-1) cout << cont[i] << endl;
        
        for(int i=(1<<(P+1))-2;i>=0;i--) {
            FR(j,11) {
                if(i>=(1<<P)-1) {
                    if(j<=cont[i]) dp[i][j]=0;
                    else dp[i][j]=INF;
                } else {
                    if(j==10) {
                        dp[i][j]=INF;
                        continue;
                    }
                    ll amt1=cont[i];
            //        cout << "amt1: " << amt1<<endl;
                    amt1+=dp[2*i+1][j];
                    amt1+=dp[2*i+2][j];
                    ll amt2=0;
                    amt2+=dp[2*i+1][j+1];
                    amt2+=dp[2*i+2][j+1];
              //      if(j<=3) cout << amt1 << " " << amt2 << endl;
                    dp[i][j]=min(amt1,amt2);
                }
  //              if(j<=3)
//                cout << "i: " << i << "j: " << j << " " << dp[i][j] << endl;

            }
        }
        
        
        cout << min(dp[0][0],dp[0][1]) << endl;
    }
}