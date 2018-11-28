#include<cstdio>
#include<cstring>
int tc;
int ar[2][105][105];
int r1,r2,c1,c2,r;

int main(){
 scanf("%d",&tc);
 for (int ti = 1; ti <= tc; ti++){
      bool tr = false;
      scanf("%d",&r);
      memset(ar,0,sizeof(ar));
      for (int i = 1; i <= r; i++){
          scanf("%d %d %d %d",&r1,&c1,&r2,&c2);
          for (int j = r1; j <= r2; j++){
              for (int k = c1; k <= c2; k++){
                  ar[0][j][k] = 1;    
                  tr = true;
              }    
          }
      }            
      int now = 0;
      int res = 0;
      while(tr){
         int next = 1-now;
         res++;
         tr = false;
         for (int i = 1; i <= 101; i++){
             for (int j = 1; j <= 101;j++){
                 if ((ar[now][i][j] == 0) && (ar[now][i-1][j] == 1) && (ar[now][i][j-1] == 1))  {
                    ar[next][i][j] = 1;                   
                 } else if ((ar[now][i][j] == 1) && (ar[now][i-1][j] == 0) && (ar[now][i][j-1] == 0)) {
                    ar[next][i][j] = 0;       
                 } else ar[next][i][j] = ar[now][i][j];
                 if (ar[next][i][j] == 1) tr =true;
             }    
         }   
         now = next;         
      }
      printf("Case #%d: %d\n",ti,res);
 }   
}
