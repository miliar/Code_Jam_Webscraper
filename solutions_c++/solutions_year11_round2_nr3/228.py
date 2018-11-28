#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int sets[100][100];
int nsets, N;
int perm[100];

int color(int v, int max)
{
    int check[100];
    if(v>N){
            for(int i=0;i<nsets;i++) {
                    memset(check,0,sizeof(check));
                    for(int j=1;j<=N;j++)
                            if(sets[i][j])
                                          check[perm[j]]=1;
                    for(int j=1;j<=max;j++)
                            if(!check[j]) return 0;        
            }
            return 1;
    }
    for(int i=1;i<=max;i++){
            perm[v]=i;
            if(color(v+1,max)) return 1;
    }
    return 0;
}

main() {
       int T, M, U[2100], V[2100],max,cnt;
       FILE *in = fopen("C.in","r");
       FILE *out = fopen("c.out","w");
       fscanf(in,"%d",&T);
       for(int t=1;t<=T;t++) {
               fscanf(in,"%d %d",&N,&M);
               for(int i=0;i<M;i++) {
                       fscanf(in,"%d",U+i);
               }
               for(int i=0;i<M;i++) {
                       fscanf(in,"%d",V+i);
               }
               nsets=1;
               memset(sets,0,sizeof(sets));
               for(int i=1;i<=N;i++)
                       sets[0][i]=1;
               for(int i=0;i<M;i++){
                       for(int j=0;j<nsets;j++) {
                               if(sets[j][U[i]]&&sets[j][V[i]]) {
                                       for(int k=U[i];k<=V[i];k++) {
                                           sets[nsets][k] = sets[j][k];
                                           sets[j][k]=0;
                                       }
                                       sets[j][U[i]] = 1;
                                       sets[j][V[i]] = 1;
                                       nsets++;
                                       break;
                               }
                       }
               }
               max = N;
               for(int i=0;i<nsets;i++){
                       cnt=0;
                       for(int j=1;j<=N;j++)
                               if(sets[i][j])
                                     cnt++;
                       max <?= cnt;
               }
               for(;max>0&&!color(1,max);max--);
               printf("Case #%d: %d\n",t,max);
               fprintf(out,"Case #%d: %d\n",t,max);
               for(int i=1;i<=N;i++) {
                       printf("%d%s",perm[i],i!=N?" ":"");
                       fprintf(out,"%d%s",perm[i],i!=N?" ":"");
               }
               printf("\n");
               fprintf(out,"\n");
       }
       fclose(out);
       system("PAUSE");
}
