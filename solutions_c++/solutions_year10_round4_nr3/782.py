#include<cstdio>
#include<algorithm>
#include<queue>
#include<stack>
#include<vector>
#include<cstring>
using namespace std;
#define INF (1<<29)

int c,r;
bool a[105][105],b[105][105];

int main(){
    scanf("%d",&c);
    for (int t=1;t<=c;++t){
        memset(a,0,sizeof(a));
        
        scanf("%d",&r);
        if (r==0){
           printf("Case #%d: 0\n",t);
           continue;
        }
        while (r--){
              int x1,x2,y1,y2;
              scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
              for (int i=x1;i<=x2;++i){
                  for (int j=y1;j<=y2;++j){
                      a[i][j]=1;
                  }
              }
        }
        
        int ok;
        for (int ans=1;ans<=10005;++ans){
            ok=1;
            
            /*for (int i=1;i<=5;++i){
                for (int j=1;j<=5;++j){
                    printf("%d ",a[i][j]);
                }
                puts("");
            }
            puts("!!!!");*/ 
            for (int i=100;i>=1;--i){
                for (int j=100;j>=1;--j){
                    if (a[i][j]){
                       if ((!a[i-1][j]) && (!a[i][j-1])) a[i][j]=0;
                       else ok=0;
                    }
                    else{
                         if (a[i-1][j] && a[i][j-1]) a[i][j]=1,ok=0;
                    }
                }
            }
            
            if (ok){
               printf("Case #%d: %d\n",t,ans);
               break;
            }
        }
    }
    return 0;
}
