#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int T,C,D,N;
char comb[27][27];
char opp[100][2];
int app[27];
char res[1000];
char nres;

void oppose(){
     for(int i=0;i<D;i++)
             if(app[opp[i][0]-'A']&&app[opp[i][1]-'A']) {
                      memset(app,0,sizeof(app));
                      nres=0;
             }
}

void combine(){
     if(nres>1&&comb[res[nres-1]-'A'][res[nres-2]-'A']!=0) {
             app[res[nres-1]-'A']--;
             app[res[nres-2]-'A']--;
             res[nres-2] = comb[res[nres-1]-'A'][res[nres-2]-'A'];
             nres--;
             app[res[nres-1]-'A']++;
             combine();
     }
}

void invoke(char e){
     res[nres++] = e;
     app[e-'A']++;
     combine();
     oppose();
}

main() {
       
       
       FILE *in = fopen("B-large.in","r");
       FILE *out = fopen("b-large.out","w");
       fscanf(in,"%d",&T);
       char buff[10000];
       for(int t=1;t<=T;t++) {
               nres=0;
               memset(app,0,sizeof(app));
               memset(comb,0,sizeof(comb));
               fscanf(in,"%d",&C);
               for(int i=0;i<C;i++) {
                       fscanf(in,"%s",buff);
                       comb[buff[0]-'A'][buff[1]-'A'] = buff[2];
                       comb[buff[1]-'A'][buff[0]-'A'] = buff[2];
               }
               fscanf(in,"%d",&D);
               for(int i=0;i<D;i++) {
                       fscanf(in,"%s",buff);
                       opp[i][0]=buff[0];
                       opp[i][1]=buff[1];
               }
               fscanf(in,"%d",&N);
               fscanf(in,"%s",buff);
               for(int i=0;i<N;i++) {
                       invoke(buff[i]);
               }
               fprintf(out,"Case #%d: [",t);
               fprintf(stdout,"Case #%d: [",t);
               for(int i=0;i<nres;i++){
                       fprintf(out,"%c%s",res[i],i!=nres-1?", ":"");
                       fprintf(stdout,"%c%s",res[i],i!=nres-1?", ":"");
               }
               fprintf(out,"]\n",t);
               fprintf(stdout,"]\n",t);
               //fprintf(stdout,"Case #%d: %d %d\n",t,sum,xr);
       }
       fclose(out);
       system("PAUSE");
}
