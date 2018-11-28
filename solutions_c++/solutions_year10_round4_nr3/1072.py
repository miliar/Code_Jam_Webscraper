#include "stdio.h"
#include "math.h"
#include "string.h"

bool table[2][101][101];

int main(void){
   freopen("bacteria.in","r",stdin);
   freopen("bacteria.out","w",stdout);
   int T,r;
   scanf("%d",&T);
   for(int t=0;t<T;t++){
      int xmax=0,ymax=0;
      int stable=1;
      scanf("%d",&r);
      int x1[r],x2[r],y1[r],y2[r];

      for(int i=0;i<r;i++){
         scanf("%d%d%d%d",&x1[i],&y1[i],&x2[i],&y2[i]);
         if(x1[i]+1>xmax)xmax=x1[i]+1;
         if(x2[i]+1>xmax)xmax=x2[i]+1;
         if(y1[i]+1>ymax)ymax=y1[i]+1;
         if(y2[i]+1>ymax)ymax=y2[i]+1;
      }
      for(int i=0;i<ymax;i++){
         for(int j=0;j<xmax;j++){
            table[0][i][j]=false;
            table[1][i][j]=false;
         }
      }
      for(int q=0;q<r;q++){
         for(int i=y1[q];i<=y2[q];i++){
            for(int j=x1[q];j<=x2[q];j++){
               table[0][i][j]=true;
            }
         }
      }
      bool flg=true;
      int count=0;
      while(flg){
         flg=false;
         int dtable=(stable+1)%2;

         /*
         for(int i=1;i<ymax;i++){
            for(int j=1;j<xmax;j++){
               printf("%d",table[dtable][i][j]);
            }
            printf("\n");
         }
         printf("\n");
         //*/

         for(int i=0;i<ymax;i++)
            for(int j=0;j<xmax;j++)
               table[stable][i][j]=false;

         for(int i=0;i<ymax;i++){
            for(int j=0;j<xmax;j++){
               if(i>0&&table[dtable][i-1][j]){
                  if(j>0&&table[dtable][i][j-1]){
                     table[stable][i][j]=true;
                     flg=true;
                  }
               }
               if(table[dtable][i][j]){
                  if(i>0&&table[dtable][i-1][j]||j>0&&table[dtable][i][j-1]){
                     table[stable][i][j]=true;
                     flg=true;
                  }
               }
            }
         }

         stable++;
         stable%=2;
         count++;
      }
      printf("Case #%d: %d\n",t+1,count);
   }

   return 0;
}
