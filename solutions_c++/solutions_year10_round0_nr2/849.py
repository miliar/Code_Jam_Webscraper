#include <iostream.h>
long long t[1000];
long long t2[500000];
long long T;
long long gdc(long long a, long long b){
     if( a==0 ) return b;
     if( b==0 ) return a;
     if( a>b ) return gdc(a%b, b);
     return gdc(a, b%a);
}
int main(){
    FILE *f, *fout;
    f = fopen("input.txt","r");
    fout = fopen("output.txt","w");
    int C,N,i,j,k,run;
    fscanf(f,"%d", &C);
    for(i=0 ; i<C ; i++){
            fscanf(f,"%d", &N);
            for(j=0 ; j<N ; j++) fscanf(f,"%lld", &t[j]);
            run = 0;
            for(j=0 ; j<N ; j++)
                for(k=j+1 ; k<N ; k++){
                          if( t[j] > t[k] ) t2[run]= t[j]-t[k];
                          else t2[run]= t[k]-t[j];
                          run++;
                } 
            T = t2[0];
            for(j=1 ; j<run ; j++) T = gdc(T,t2[j]);
            if( t[0]%T ) fprintf(fout, "Case #%d: %lld\n", i+1, T-t[0]%T);
            else fprintf(fout, "Case #%d: 0\n", i+1);
    }
    fclose(f);
    fclose(fout);
    return 0;
}
