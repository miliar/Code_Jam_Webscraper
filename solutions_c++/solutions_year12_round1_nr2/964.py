#include <cstdio>
#include <iostream>
using namespace std;
int main (){
    bool b[1000][2],YN;
    int T,N,lev[1000][2],star,tot,max,temp,i,j;
    scanf("%d",&T);
    for (i=1;i<=T;i++){
        scanf("%d",&N);
        for (j=0;j<N;j++){
            scanf("%d %d",&lev[j][0],&lev[j][1]);
            b[j][0]=0;
            b[j][1]=0;
        }
        star=0;
        tot=0;
        while (star!=2*N){
              YN=0;
              for (j=0;j<N;j++){
                  if (b[j][1]==0 && star>=lev[j][1]){
                                  if (b[j][0]==1){
                                                  star++;
                                  } else {
                                         star+=2;
                                  }
                                  b[j][0]=1;
                                  b[j][1]=1;
                                  YN=1;
                                  tot++;
                  }
              }
              if (YN==0){
                         max=-1;
                         for (j=0;j<N;j++){
                             if (b[j][0]==0 && star>=lev[j][0]){
                                            if (lev[j][1]>max){
                                                                 max=lev[j][1];
                                                                 temp=j;
                                            }
                                            YN=1;
                             }
                         }
                         if (YN==1){
                                    star++;
                                    tot++;
                                    b[temp][0]=1;
                         }
              }
              if (YN==0){
                         tot=-1;
                         star=2*N;
              }
        }
        if (tot==-1){
                       printf("Case #%d: Too Bad\n",i);
        } else {
               printf("Case #%d: %d\n",i,tot);
        }
    }
    //system("pause");
    return 0;
}
