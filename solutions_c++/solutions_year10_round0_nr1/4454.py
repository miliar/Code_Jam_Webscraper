#include <stdio.h>
#include <stdlib.h>
typedef struct Snapper{

    bool power;
    bool Ison;
}Snapper;

#define submit 1

#ifdef submit
FILE * Input = fopen("A-small.in","r");
FILE * Output = fopen("A-small.out","w");
#endif

#ifndef submit

#define Input stdin
#define Output stdout

#endif



int main(){


    int T;
    int N,K;
    int i,j,t;
    fscanf(Input,"%d",&T);
    int cases;
    for(cases=1;cases <= T;cases++){
        fscanf(Input,"%d %d",&N,&K);
        Snapper S[N+1];


        S[0].power = true;
        S[0].Ison = false;

        //for(i=0;i<N;i++){
           //  printf("%d ",S[i].Ison);
             //}getchar();getchar();

        for(i=1;i<N;i++){
            S[i].power = false;
            S[i].Ison = false;
        }

       for(j=0;j<K;j++){

          for(i=0;i<N;i++)
             if(S[i].power == true)
               S[i].Ison = !S[i].Ison;

//           for(i=0;i<N;i++){
//             printf("%d ",S[i].Ison);
//             }system("pause");

          for(i=1;i<N;i++)
              if(S[i-1].Ison&&S[i-1].power)
                S[i].power = 1;
              else
                S[i].power = 0;
//          printf("Power :");
//          for(i=0;i<N;i++){
//             printf("%d ",S[i].power);
//             }system("pause");

         }

        fprintf(Output,"Case #%d: ",cases);
        if(S[N-1].Ison&&S[N-1].power)
          fprintf(Output,"ON\n");
        else
          fprintf(Output,"OFF\n");
    }
}
