#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int abs(int a){return a<0?-a:a;}
int max(int a, int b){return a<b?b:a;}

main() {
       int T,N,t,n,p,pos[2],tot,tm,s[2];
       char r;
       FILE *in = fopen("a-large.in","r");
       FILE *out = fopen("a-large.out","w");
       fscanf(in,"%d",&T);
       for(int t=1;t<=T;t++) {
               fscanf(in,"%d",&N);
               pos[0]=pos[1]=1;
               s[0]=s[1]=0;
               tot=0;
               for(int i=0;i<N;i++) {
                       fscanf(in," %c %d",&r,&p);
                       tm = max(abs(pos[r=='O']-p)-s[r=='O'],0)+1;
                       pos[r=='O'] = p;
                       tot+=tm;
                       s[r=='O']=0;
                       s[r!='O']+=tm;
               }
               fprintf(out,"Case #%d: %d\n",t,tot);
               fprintf(stdout,"Case #%d: %d\n",t,tot);
       }
       fclose(out);
       system("PAUSE");
}
