#include <cstdio>
#include <vector>
using namespace std;

int main(){
     int T,N,K;
     FILE *inp=fopen("snapper.in","r");
     FILE *out=fopen("snapper.out","w");

     fscanf(inp,"%ld",&T);
     for(int t=1;t<=T;t++){
                            fscanf(inp,"%ld %ld",&N,&K);
                            bool ok=true;
                            for(int n=0;n<N;n++){
                                                  if(!(K&1<<n)){ok=false;break;}
                                                 }
                            fprintf(out,"Case #%ld: ",t);
                            if(ok==true)fprintf(out,"ON\n");
                            else fprintf(out,"OFF\n");
                          }





return 0;
}
