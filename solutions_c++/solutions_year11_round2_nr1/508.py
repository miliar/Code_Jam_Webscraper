#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char buff[110][110];
int played[110];
int won[110];

main() {
       int T, N, den;
       double OWP[110], OOWP[110],WP[110];
       FILE *in = fopen("A-large.in","r");
       FILE *out = fopen("a-large.out","w");
       fscanf(in,"%d",&T);
       for(int t=1;t<=T;t++) {
               fscanf(in,"%d",&N);
               for(int i=0;i<N;i++) {
                       fscanf(in,"%s",buff[i]);
                       played[i]=0;
                       won[i]=0;
                       for(int j=0;j<N;j++) {
                               played[i]+=(buff[i][j]!='.'?1:0);
                               won[i]+=(buff[i][j]=='1'?1:0);
                       }
                       WP[i] = (double)won[i]/(double)played[i];
               }
               for(int i=0;i<N;i++) {
                       den=0;
                       OWP[i]=0;
                       for(int j=0;j<N;j++) {
                               if(j!=i&&buff[i][j]!='.'&&(played[j]-(buff[i][j]!='.'?1:0))) {
                                        OWP[i]+=(double)(won[j]-(buff[i][j]=='0'))/(double)(played[j]-(buff[i][j]!='.'));
                                        den++;
                               }
                       }
                       if(den) OWP[i] /= (double)(den);
               }
               fprintf(out,"Case #%d:\n",t);
               fprintf(stdout,"Case #%d:\n",t);
               for(int i=0;i<N;i++) {
                       den=0;
                       OOWP[i]=0;
                       for(int j=0;j<N;j++) {
                               if(j!=i&&buff[i][j]!='.') {
                                        OOWP[i]+=OWP[j];
                                        den++;
                               }
                       }
                       if(den) OOWP[i] /= (double)(den);
                       printf("%.12lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
                       fprintf(out,"%.12lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
               }
       }
       fclose(out);
       system("PAUSE");
}
