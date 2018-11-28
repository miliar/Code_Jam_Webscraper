#include <vector> 
#include <string> 
#include <set> 
#include <algorithm> 
#include <map> 
#include <iostream> 
#include <sstream> 
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
using namespace std; 
  
#define FOR(it,x) for(it=x.begin();it!=x.end();++it)  
#define SZ(a) int((a).size())  
#define ALL(a) (a).begin(),(a).end()  
#define PB push_back 
#define MP make_pair

int M,N;
int match(int j, int k) {
    int i;
    for (i=1; i<(1<<N); i++) {
        if ((j&(1<<i))&&((k&(1<<(i+1)))||(k&(1<<(i-1)))))return 0;
    }
    return 1;
}
int pcount(int bit) {
    int x;
    for (x=0;bit;bit>>=1)x+=(bit&1);
    return x;
}
int main() {
    int i,j,k,m,t,T,dp[13][(1<<13)];
    char mp[13][13];
    scanf("%d\n", &T);
    for(t=1;t<=T;t++) {
        scanf("%d %d\n",&M,&N);        
        for (i=0;i<M;i++) gets(mp[i]);
        for (i=0;i<(1<<N);i++) {
            for (j=0,m=1;j<N;j++) {
                if (i&(1<<j)) {
                    if (mp[0][j]=='x'||(i&(1<<(j+1)))||(j&&(i&(1<<(j-1))))) {
                        m=0;
                        break;
                    }
                }
            }
            if (m)dp[0][i]=pcount(i);
            else dp[0][i]=0;
        }
        for (i=1;i<M;i++) {
            for (j=0;j<(1<<N);j++) {
                dp[i][j]=0;
                for (k=0,m=1; k<N;k++) {
                    if (j&(1<<k))if (mp[i][k]=='x'||(j&(1<<(k+1)))||(k&&(j&(1<<(k-1))))) {
                        m=0;
                        break;
                    }
                }
                if (!m) continue;
                for (k=0; k<(1<<N);k++) {
                    if (!match(j,k)) continue;
                    int val=dp[i-1][k]+pcount(j);
                    dp[i][j]=max(val,dp[i][j]);
                }
            }
        }
        int mc=0;
        for(i=0;i<(1<<N);i++) mc=max(mc,dp[M-1][i]);        
        printf("Case #%d: %d\n",t,mc);
    }
    return 0;
}
