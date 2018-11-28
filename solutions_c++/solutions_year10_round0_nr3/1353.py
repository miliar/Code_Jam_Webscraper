#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAM 1024

long long int peso[TAM];
long long int next[TAM],com[TAM];
int main(){
  int nt;
  int R,k,n;
  

  scanf("%d",&nt);
  for(int t = 1 ; t <= nt;t++){
    scanf("%d %d %d",&R,&k,&n);

    for(int i = 0 ; i < n;i++)
      scanf("%lld",&peso[i]);

    int j = 0;
    for(int i = 0 ; i < n ;i++){
      int parcial = peso[i];
      int j = 1;     
      while(j<n && parcial + peso[(j+i)%n] <= k){
	parcial += peso[(j+i)%n];
	j++;
      }
      next[i] = (j+i)%n;
      com[i] = parcial;
    }

    printf("Case #%d: ",t);
    
    long long int ans = 0;
    int id = 0;
    for(int i = 0 ; i < R;i++){
      // printf("%d\n",com[id]);
      ans += com[id];
      id = next[id];
      
    }
    printf("%lld\n",ans);
  }
  return 0;
}
