#include<stdio.h>
#include<conio.h>
#include <stdlib.h>
main()
{
      FILE *ifp, *ofp;
      int T,N,S,P;
      int ti[100];
      int Tcount = 0;
      int Scount = 0;
      ifp = fopen("B-large.in","r");
      ofp = fopen("output_B_large.txt","w");
      fscanf(ifp,"%d",&T);
      int j = 1;
      printf("%d", T);
      while(j <= T){
              
              fscanf(ifp,"%d %d %d",&N,&S,&P);
              int i = 0;
              while(i < N)
              {
                      fscanf(ifp, "%d",&ti[i]);
                      i++;
              }
              int P1 = (P*3)-3;
              if(P1<0)
                      P1=0;
              int P2 = (P*3)-4;
              if(P2<0)
                      P2=0;
              i = 0;
              while(i < N){
                      if(ti[i] != 0){
                               if(ti[i] > P1){
                                        Tcount++;
                               }
                               else if(ti[i] == P1 || ti[i] == P2){
                                    Scount++;
                               }
                      }
                      else{
                           if(P == 0)
                               Tcount++;
                      }
                      i++;
              }
              if(Scount > S)
                        Scount = S;
              Tcount = Tcount + Scount;
              fprintf(ofp, "Case #%d: %d\n",j, Tcount);
              printf("case %d complete\n",j);
              Tcount = 0;
              Scount = 0;
              j++;
              
      }
      printf(" all cases are done\n");
      getch();
      fclose(ifp);
      fclose(ofp);
}
