#include <iostream.h>
int main(){
    int T,N,K,i;
    unsigned long mu[31];
    mu[0]=1;
    for ( N=1; N<31 ; N++) mu[N]=2*mu[N-1];
    FILE *f, *fout;
    f = fopen("input.txt","r");
    fout = fopen("output.txt","w");
    fscanf(f,"%d", &T);
    for(i=0;i<T;i++){
                fscanf(f,"%d %d", &N, &K);
                if( K < mu[N]-1 ) fprintf(fout,"Case #%d: OFF\n",i+1);
                else if( K == mu[N]-1 ) fprintf(fout,"Case #%d: ON\n",i+1);
                else if( (K+1)%mu[N] ) fprintf(fout,"Case #%d: OFF\n",i+1);
                else fprintf(fout,"Case #%d: ON\n",i+1);
    }
    fclose(f);
    fclose(fout);
    return 0;
}
