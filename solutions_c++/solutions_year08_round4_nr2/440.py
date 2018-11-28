#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>

#define f(x,y) for(int x=0; x<(y); ++x)
using namespace std;
int C, N, M, A;
int main(){
  scanf("%d", &C);
  f(t, C){
    scanf("%d%d%d", &N, &M, &A);
    int found=0;
    printf("Case #%d: ", t+1);
    for(int i=0; i<=N && !found; ++i) 
      for(int j=0; j<=M && !found; ++j)
	for(int k=0; k<=N && !found; ++k)
	  for(int l=0; l<=M && !found; ++l)
	    if(i*l-j*k==A){
	      found=1;
	      printf("%d %d %d %d %d %d\n", 0, 0, i, j, k, l);
	    }
    if(!found)
      printf("IMPOSSIBLE\n");
  }      
  return 0;
}
