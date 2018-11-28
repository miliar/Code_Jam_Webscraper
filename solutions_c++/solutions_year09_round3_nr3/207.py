#include <iostream>
using namespace std;
int dp[111][111];
int x[1000];
int n,q;

int wow(int s,int e){
     if (dp[s][e]!=-1) return dp[s][e];
     dp[s][e]=0;
     if (e-s>1){
                dp[s][e]=x[e]-x[s]-2;
     
                int tmp=999999;
                for (int i=s+1;i<e;i++)
                tmp=min(tmp,wow(s,i)+wow(i,e));
                
                dp[s][e]+=tmp;
                }
          //      cout<<s<<" "<<e<<" "<<dp[s][e]<<endl;
     return dp[s][e];
     }

int main(){
    freopen("C.txt","r",stdin);
    freopen("C.out","w",stdout);
    int T;
    scanf("%d",&T);
    
    for (int j=1;j<=T;j++){
        
    scanf("%d%d",&n,&q);
    for (int i=1;i<=q;i++){
        scanf("%d",&x[i]);
        }
    x[0]=0;
    x[q+1]=n+1;
    for (int i=0;i<=q+1;i++)
    for (int j=0;j<=q+1;j++)
        dp[i][j]=-1;
        
    sort(x+1,x+1+q);
    printf("Case #%d: %d\n",j,wow(0,q+1));
    }
    //system("pause");
    }
