#include <cstdio>
#include <algorithm>
using namespace std;

int T,N, a[20];

int main(){
  scanf("%d", &T);
  for (int ttt=1; ttt<=T; ttt++){
    scanf("%d", &N);

    for (int i=0; i<N; i++)
      scanf("%d", a+i);

    int best = -1;
    for (int s=1; s<(1<<N)-1; s++){
      
      int sumd[2]={0,0};
      int xord[2]={0,0};
      for (int i=0; i<N; i++){
	sumd[!!(s&(1<<i))] += a[i];
	xord[!!(s&(1<<i))] ^= a[i];
      }
      if (xord[0]==xord[1])
	best = max(best,max(sumd[0],sumd[1]));
      //fprintf(stderr, "it: %d,   best: %d\n", s, best);
    }
    printf("Case #%d: ", ttt);
    if (best==-1)
      printf("NO\n");
    else
      printf("%d\n", best);
  }
}
