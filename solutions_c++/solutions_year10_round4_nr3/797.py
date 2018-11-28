#include"iostream"
#include"algorithm"
#include"cstdlib"
using namespace std;
int map[101][101];
int main(){
    freopen("C-small-attempt1.in","r",stdin);
    freopen("Csout.txt","w",stdout);
    int T,R,x1,x2,y1,y2;
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
       scanf("%d",&R);
       int cnt=0;
       while(R--){
          scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
          for(int j=y1;j<=y2;j++){
            for(int k=x1;k<=x2;k++){
               if(!map[j][k]){
               map[j][k]=1;
               cnt++;
               }
            }
          }
       }
      
       
       int res=0;
       while(cnt){
          //born
           res++;
           for(int i=100;i>=1;i--){
              for(int j=100;j>=1;j--){
                  if(map[i][j]==0){
                      if(map[i-1][j]==1 && map[i][j-1]==1){
                           map[i][j]=1;
                           cnt++;
                      }
                  }
              }
           }
           //die
           
           for(int i=100;i>=1;i--){
              for(int j=100;j>=1;j--){
                  if(map[i][j]==1){
                       if(map[i-1][j]==0 && map[i][j-1]==0){
                           map[i][j]=0;
                           cnt--;
                      }
                  }
              }
           }
       }
       printf("Case #%d: %d\n",i,res);
    }
   // system("pause");
    return 0;
}
