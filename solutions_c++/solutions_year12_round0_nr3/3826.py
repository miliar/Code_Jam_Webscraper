#include<stdio.h>
#include<stdlib.h>

int P[8] = {1,10,100,1000,10000,100000,1000000,10000000};

int rev(int num, int d, int n){

    int p = P[d];
    int p2 = P[n-d];

    int a = num/p;
    int b = num%p;


    return b*p2+a;

}




int main(){

  int ncases;
  int A;
  int B;
  scanf("%d ",&ncases);
  int rep[7];
  for(int nc = 0; nc < ncases;++nc){
          scanf("%d %d", &A,&B);
          int count = 0;
          int p = 0;
          while(A/P[p] > 0 || B/P[p]>0)
                  ++p;
          //TODO comprobar q esten en la misma potencia
//          printf("%d\n",p);
          
          for(int i = A; i < B; ++i){
                  for(int n = 1; n < p; ++n){
                          int r = rev(i,n,p);

                          bool repe = false;
                          //Check if repe
                          rep[n-1] = r;
                          for(int j = 0; j < n-1; ++j)
                                  if(rep[j]==r){
                                          repe = true;
                                          break;
                                  }
                          if (!repe &&r > i && r <= B)  {
                                  ++count;
     //                             fprintf(stderr,"%d %d\n",i,r);

                          }

                  }

          }
          printf("Case #%d: %d\n",nc+1,count);
  }

  return EXIT_SUCCESS;
}
