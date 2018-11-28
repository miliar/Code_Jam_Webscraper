#include <iomanip>
#include <stdio.h>
#include <map>
#include <set>

using namespace std;
int main(){
  FILE *in = fopen("B-small-0.in","r");
  FILE *out = fopen("small.out","w");
  int T;
  fscanf(in,"%d", &T);
  for (int t = 0; t < T; t++){
   int table[1010]={}, din[1010][1010]={}, tb[1010];
    int L,N,C; char tmpc; int t1;
    fscanf(in,"%d %d %d %d", &L,&t1,&N, &C);
    N++;
    for (int i = 0; i < C; i++){
      fscanf(in,"%d",&table[i]);
    }
    for (int i = 0; i < N; i++){
      tb[i]= table[i%C]*2;
    }
    t1=t1;
    din[0][0]=0;
    for(int i = 1; i < N; i++){
      din[0][i]=din[0][i-1]+tb[i-1];
      din[i][0]=0;
    }
    
    for(int i = 1; i < N; i++){
     for(int j = 1; j < N; j++){
        int tmp=din[i][j-1]+tb[j-1];
        if (tmp > t1){
            int tmp1= din[i-1][j-1];
            int toflight = tb[j-1];
            if (tmp1 < t1) {toflight -= t1-tmp1; tmp1 = t1;}
            if(toflight % 2 == 1) fprintf(stderr,"Error");
            tmp1 += toflight/2;
            if (tmp1< tmp) tmp = tmp1;
        }
        din[i][j]=tmp;
     }
    }
    

    printf("Case #%d: %d\n",t+1, din[L][N-1]);
/*    for (int i = 0; i < N+1; i++){
        for (int j = 0; j< N+1; j++){
        printf("%d ",din[i][j]);
        }
        printf("\n");
    }
*/
  }
    
}
