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

int main() {
    int t,T,H,W,R,dp[101][101];
    char ar[101][101];
    scanf("%d",&T);
	for(t=1;t<=T;t++) {
        scanf("%d %d %d",&H,&W,&R);
        for (int i=1;i<=H;i++) {
            for (int j=1;j<=W;j++) {
                ar[i][j]=0;
            }
        }
        for (int i=1,x,y;i<=R;i++) {
            scanf("%d %d",&x,&y);
            ar[x][y]=1;
        }
        dp[1][1]=1;
        for (int i=1;i<=H;i++) {
            for (int j=1;j<=W;j++) {
				if(i*j==1)continue;
				dp[i][j]=0;
                if(!ar[i][j]&&i*j>1) {
	                if(i>2&&j>1)dp[i][j]=(dp[i][j]+dp[i-2][j-1])%10007;
	                if(i>1&&j>2)dp[i][j]=(dp[i][j]+dp[i-1][j-2])%10007;
				}
            }
        }
        printf("Case #%d: %d\n",t,dp[H][W]);
    }
}
