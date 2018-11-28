#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXP = 12;
const int MAXN = 1024;
const int MAXV = 100000;
const int INF = MAXN*MAXV+MAXV;

int mai[1<<MAXP];
int price[1<<MAXP];
int resp[1<<MAXP][MAXP];

int main(){
    int t;
    scanf("%d",&t);
    
    for(int lp=1;lp<=t;++lp){
        int p;
        scanf("%d",&p);
        
        vector<int> m((1<<p));
        for(int i=0;i<(1<<p);++i){
            scanf("%d",&m[i]);
        }
        
        int n = (1<<(p+1)) - 1;
        for(int i=0;i<(1<<p);++i){
            mai[n-i-1] = p-m[i];
        }
        
        for(int i=0;i<(1<<p)-1;++i){
            scanf("%d",&price[(1<<p)-i-2]);
        }
        
        for(int i=0;i<n;++i){
            for(int j=0;j<=p;++j){
                resp[i][j] = INF;
            }
        }
        
        for(int i=0;i<(1<<p);++i){
            for(int j=0;j<=p;++j){
                if(j >= mai[n-i-1]){
                    resp[n-i-1][j] = 0;
                }
            }
        }
        
        for(int i=(1<<p)-2;i>=0;--i){
            mai[i] = max(mai[2*i+1],mai[2*i+2]);
            //printf("%d: %d %d %d\n",i,mai[i],mai[2*i+1],mai[2*i+2]);
            for(int j=0;j<=p;++j){
                //compra
                resp[i][j] = min(resp[i][j],price[i]+resp[2*i+1][j+1]+resp[2*i+2][j+1]);
                
                //nao compra
                resp[i][j] = min(resp[i][j],resp[2*i+1][j]+resp[2*i+2][j]);
            }
        }
        
        printf("Case #%d: %d\n",lp,resp[0][0]);
        
    }
    
    return 0;
}