#include <cstdio>
using namespace std;
int main(){
  int T;
  scanf("%d",&T);
  for(int Case = 1; Case<=T; Case++){
    int R,k,N;
    scanf("%d%d%d",&R,&k,&N);
    int G[N];
    for(int i=0; i<N; i++)
      scanf("%d",&G[i]);
    int T[N][2];
    for(int i=0; i<N; i++){
      int j=i, temp = 0;
      do{
        if(temp+G[j]<=k)
          temp+=G[j];
        else break;
        j=(j+1)%N;
      }while(j!=i);
      T[i][0] = temp;
      T[i][1] = j;
    }
    int result = 0;
    int g = 0;
    for(int i=0; i<R; i++){
      result += T[g][0];
      g = T[g][1];      
    }
    printf("Case #%d: %d\n",Case, result);  
  }
}
