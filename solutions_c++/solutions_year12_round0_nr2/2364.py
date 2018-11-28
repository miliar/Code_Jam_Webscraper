#include<cstdio>
#include<algorithm>
using namespace std;

int T,N,S,p;
int edge1,edge2;
int enough;
int star_enough;

int main(){
 FILE *fin,*fout;
 fin = fopen("B-large.in","r");
 fout = fopen("googlers.out","w");
 fscanf(fin,"%d",&T);
 int k,i,x;
 for(k=0;k<T;k++){
  enough = star_enough = 0;
  fscanf(fin,"%d%d%d",&N,&S,&p);
  if(p==0) edge1=0;
  else edge1 = 3*p-2;
  if(p==0) edge2=0;
  if(p==1) edge2=1;
  if(p==2) edge2=2;
  if(p>=3) edge2=3*p-4;
  for(i=0;i<N;i++){
   fscanf(fin,"%d",&x);
   if(x>=edge1){
    enough++;
   }
   else if(x>=edge2){
    star_enough++;
   }
  }
  fprintf(fout,"Case #%d: %d\n",k+1,enough+min(star_enough,S));
 }

 return 0;
}
