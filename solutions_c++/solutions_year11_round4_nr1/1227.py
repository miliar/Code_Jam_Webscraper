#include <stdio.h>
#include <algorithm>

int T;
int X,S,R,N;
double Ans,maxt;

FILE *in = fopen("input.txt","r");
FILE *out = fopen("output.txt","w");

struct OTL{
       int a,b,v;
       bool operator()(OTL A,OTL B){
              if(A.a<B.a)return true;
              return false;
       }
};
OTL P[10000];
struct OTZ{
       bool operator()(OTL A,OTL B){
              if(A.v<B.v)return true;
              return false;
       }
};

int main(void){
       int i,t,j;
       fscanf(in,"%d",&T);
       for(t=1;t<=T;t++){
              bool flag=false;
              fscanf(in,"%d%d%d%d%d",&X,&S,&R,&j,&N);
              maxt=j;
              for(i=0;i<N;i++){
                     fscanf(in,"%d%d%d",&P[i].a,&P[i].b,&P[i].v);
              }
              std::sort(P,P+N,OTL());
              j=N;
              if(P[0].a!=0){
                     P[j].a=0;
                     P[j].b=P[0].a;
                     P[j].v=0;
                     j++;
              }
              if(P[N-1].b!=N){
                     P[j].a=P[N-1].b;
                     P[j].b=X;
                     P[j].v=0;
                     j++;
              }
              for(i=0;i<N-1;i++){
                     if(P[i].b!=P[i+1].a){
                           P[j].a=P[i].b;
                           P[j].b=P[i+1].a;
                           P[j++].v=0;
                     }
              }
              N=j;
              std::sort(P,P+N,OTZ());
              for(i=0;i<N;i++){
                     if(flag){
                           Ans+=(P[i].b-P[i].a)/(double)(S+P[i].v);
                           continue;
                     }
                     if((P[i].b-P[i].a)/ (double)(R+P[i].v)>=maxt){
                           flag=true;
                            Ans+=maxt+(P[i].b-P[i].a-maxt*(R+P[i].v))/(S+P[i].v);
                     }
                     else {
                           Ans+=(P[i].b-P[i].a)/(double)(R+P[i].v);
                           maxt-=(P[i].b-P[i].a)/(double)(R+P[i].v);
                     }
              }
              fprintf(out,"Case #%d: %.6lf\n",t,Ans);
              Ans=0;
       }
       return 0;
}
