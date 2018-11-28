#include<cstdio>
#include<math.h>
using namespace std;

int main(){
int T, N,K, List[10000], i,g;
scanf("%d", &T);
for(i=0;i<T;i++)
{
  scanf("%d%d", &N, &K);
  g=pow(2,N);
  if(K%g==g-1){
   List[i]=1;
  }
  else{
  List[i]=0;
  }
}

for(i=0;i<T;i++){
  printf("Case #%d: ", i+1);
  if(List[i]==1)
  printf("ON\n");
  else
  printf("OFF\n");
}

return 0;
}