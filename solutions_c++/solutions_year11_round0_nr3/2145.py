#include <stdio.h>
#include <stdlib.h>
#include <string.h>

main() {
       int T,t,n,v,s,xr,mn;
       FILE *in = fopen("c-large.in","r");
       FILE *out = fopen("c-large.out","w");
       fscanf(in,"%d",&T);
       for(int t=1;t<=T;t++) {
               fscanf(in,"%d",&n);
               xr=s=0;
               mn=10000000;
               for(int i=0;i<n;i++) {
                       fscanf(in,"%d",&v);
                       s+=v;
                       xr^=v;
                       mn<?=v;
               }
               if(xr) {
                       fprintf(out,"Case #%d: NO\n",t);
                       fprintf(stdout,"Case #%d: NO\n",t);
                       }
               else {
                       fprintf(out,"Case #%d: %d\n",t,s-mn);
                       fprintf(stdout,"Case #%d: %d\n",t,s-mn);
                       }
               //fprintf(stdout,"Case #%d: %d %d\n",t,sum,xr);
       }
       fclose(out);
       system("PAUSE");
}
