#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>

using namespace std;

FILE *in = fopen("A-large.in","r");
FILE *out = fopen("A-large.out","w");

char T[5][5];

main()
{
       int n, row, col, dot, outc;
       char curc;
       fscanf(in,"%d",&n);
       for(int i=0;i<n;i++){
               dot = 0; outc = -1; row=-1; col=-1;
               for(int j=0;j<4;j++) {
                       fscanf(in,"%s",T[j]);
                       for(int k=0;k<4;k++)
                               if(T[j][k]=='T') {
                                    row = j;
                                    col = k;
                               } else if (T[j][k]=='.')
                                    dot++;
               }
               for(int j=0;j<4;j++)
                       printf("%s\n",T[j]);
                       printf("\n");
               
               if(row!=-1)
                           T[row][col]='X';
               curc='X';
               for(int trn=0;trn<2;trn++){
                       for(int j=0;j<4;j++) {
                               int cr=0, cc=0, cd1=0, cd2=0;
                               for(int k=0;k<4;k++) {
                                       cr+=(curc==T[j][k]);
                                       cc+=(curc==T[k][j]);
                                       cd1+=(curc==T[k][k]);
                                       cd2+=(curc==T[k][3-k]);
                               }
                               if(cr==4||cc==4||cd1==4||cd2==4)
                                       outc = trn;
                       }
                       if(row!=-1)
                                  T[row][col]='O';
                       curc='O';
               }
               if(outc==-1) outc = (dot==0?2:3);
               fprintf(out,"Case #%d: ",i+1);
               fprintf(out,"%s",outc==0?"X won":(outc==1?"O won":(outc==2?"Draw":"Game has not completed")));
               fprintf(out,"\n");
       }
       fclose(in);
       fclose(out);
       system("PAUSE");
}
