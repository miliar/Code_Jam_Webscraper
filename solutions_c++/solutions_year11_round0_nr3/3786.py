#include<stdio.h>
#include<memory.h>

int main(){
  freopen("input.txt","r",stdin);
  freopen("output.txt","w+",stdout);
  int T,N,Nm,elem;
  int allsum,allsumxor,minelem;
  scanf("%d",&T);
  for(int i=0;i<T;i++){
    scanf("%d",&N);
    allsumxor=0;
    allsum=0;
    minelem=-1;
    for(int j=0;j<N;j++){
      scanf("%d",&Nm);
      allsumxor^=Nm;
      allsum+=Nm;
      if(minelem==-1||minelem>Nm) minelem=Nm;
    }
    if(allsumxor) printf("Case #%d: NO\n",i+1);
    else printf("Case #%d: %d\n",i+1,allsum-minelem);
  }
}
