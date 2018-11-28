#include <stdio.h>

#define CODEJAMJUDGE

  #ifdef CODEJAMJUDGE
     FILE * Input = fopen("Input.in","r");
     FILE * Output = fopen("Output.out","w");
  #endif

  #ifndef CODEJAMJUDGE
     #define Input stdin
     #define Output stdout
  #endif


main(){
    int T,N,K,C;
    fscanf(Input,"%d",&T);
    C^=C;
    while(C<T){
        fscanf(Input,"%d%d",&N,&K);
        fprintf(Output,"Case #%d: ",++C);
        if((1<<N)-1 == K%(1<<N))
          fprintf(Output,"ON\n");
        else
          fprintf(Output,"OFF\n");
    }
    fclose(Input);
    fclose(Output);
    return 0;
}
