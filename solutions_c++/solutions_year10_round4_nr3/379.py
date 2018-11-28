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

int X1[10],X2[10],Y1[10],Y2[10];

bool alive[102][102][2];
          
bool f(int a, int b, int c){
    if(a>-1&&a<102&&b>-1&&b<102&&alive[a][b][c]) return 1;
    return 0;
}

int main() {
    int T; scanf("%d",&T);
    FR(i,T) {
        memset(alive,false,sizeof(alive));
        printf("Case #%d: ",i+1);
        int R;
        cin >> R;
        FR(i,R) {
               cin >> X1[i] >> Y1[i] >> X2[i] >> Y2[i];
        }
        
        FR(i,R) FOR(j,X1[i],X2[i]+1) FOR(k,Y1[i],Y2[i]+1) alive[j][k][0]=true;
   
        bool ff=false;
        FR(i,102) FR(j,102) if(alive[i][j][0]) ff=true;
        if(!ff) {
            cout << 0 << endl;
            continue;
        }
        
        int cur=1;
        int nit=0;
        
        for(;;) {
            int tcnt=0;
            FR(i,102) FR(j,102) {                
                alive[i][j][cur]= (alive[i][j][1-cur]&&(f(i-1,j,1-cur)||f(i,j-1,1-cur))) ||  (f(i-1,j,1-cur)&&f(i,j-1,1-cur) );
                if(alive[i][j][cur]) tcnt++;
            }                        
            cur=1-cur;
            nit++;
            if(tcnt==0) break;
        }
        
        cout << nit << endl;
    }
           
}