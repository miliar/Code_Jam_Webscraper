#include<cstdio>

#define maxN 205

int T,N;
int X;
int J[maxN];
int maxj,maxj2;
double minc,maxc,c,error;
double partc;
double points;

int main(){
 int t,i,j;
 scanf("%d",&T);
 for(t=1;t<=T;t++){
  scanf("%d",&N);
  X = 0;
  for(i=0;i<N;i++){
   scanf("%d",J+i);
   X+=J[i];
  }
  printf("Case #%d: ",t);
  for(i=0;i<N;i++){
   minc = 0.0; maxc = 1.0;
   error = 0.000000001;
   while(maxc>minc+error){
    c = (minc+maxc)/2.0;
    points = J[i]+c*X;
    partc = 0.0;
    for(j=0;j<N;j++){
     if(j==i) continue;
     if(points-J[j]>0) partc += (points-J[j])/(double)X;
    }
    if(partc<1-c) minc = c;
    else maxc = c;
   }
   if(i<N-1) printf("%lf ",100*c);
   else printf("%lf\n",100*c);
  }
 }


 return 0;
}
