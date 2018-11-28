#include<stdio.h>
#include<conio.h>
#include <stdlib.h>
main()
{
      FILE *fp_in, *fp_out;
      int T,N,S,P;
      int ti[100];
      int i;
      int cnt_T = 0;
      int cnt_S = 0;
      fp_in = fopen("file_input.txt","r");
      fp_out = fopen("file_out.txt","w");
      printf("1");
      fscanf(fp_in,"%d",&T);
      int j = 1;
      printf("%d", T);
      while(j <= T){
              
              fscanf(fp_in,"%d %d %d",&N,&S,&P);
              for (i=0; i < N; i++) {
                      fscanf(fp_in, "%d",&ti[i]);
              }
              int P1 = (P*3)-3;
              if(P1<0)
                      P1=0;
              int P2 = (P*3)-4;
              if(P2<0)
                      P2=0;
              for (i = 0; i < N; i++) {
                      if(ti[i] != 0){
                               if(ti[i] > P1){
                                        cnt_T++;
                               }
                               else if(ti[i] == P1 || ti[i] == P2){
                                    cnt_S++;
                               }
                      }
                      else{
                           if(P == 0)
                               cnt_T++;
                      }
              }
              if(cnt_S > S)
                        cnt_S = S;
              cnt_T = cnt_T + cnt_S;
              printf("%d completed\n",j);
              fprintf(fp_out, "Case #%d: %d\n",j, cnt_T);
              cnt_T = 0;
              cnt_S = 0;
              j++;
              
      }
      printf("Done\n");
      getch();
      fclose(fp_in);
      fclose(fp_out);
}
