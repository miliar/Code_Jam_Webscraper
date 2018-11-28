
#include <stdio.h>

#include<string>
#include<map>
#include <math.h>


using namespace std;

int release[1000];

int cost[120][120];

int Q;

int pd(int first, int last) {

  // fill in cost, based on release;

  // printf("comp pd %d %d\n",first,last);
  fflush(stdout);
  if (cost[first][last] == -1) {
    
    int prev = prev = release[first-1];
    int next = release[last+1];

    int mycost = next - prev - 2;
    
    // printf("mycost = %d\n",mycost);

    int mincost = 0;
    if (first != last) {
      mincost = pd(first+1,last);
      
      int lastcost = pd(first,last-1);
      if (lastcost < mincost)
	mincost = lastcost;

      for (int p = first+1; p < last; p++) {
	int c = pd(first,p-1) + pd(p+1,last);
	if (c < mincost) mincost = c;
      }
      
    }
      
    cost[first][last] = mincost + mycost;
    
  }
  return cost[first][last];
  
}

main() {

  
  int N;

  
  scanf("%d",&N);
  
  
  
  for (int n = 1; n <= N; n++) {

    int coins = 0;
    int P;

    scanf("%d %d",&P,&Q);

    release[0] = 0;
    for (int q=0; q < Q; q++) {      
      scanf("%d",&release[q+1]);
    }
    release[Q+1] = P+1;

    // now compute;
        
    for (int q = 0; q < Q+2; q++) {
      for (int z = 0; z < Q+2; z++)
	cost[q][z] = -1;
    }
    
    
    printf("Case #%d: %d\n",n,pd(1,Q));

  }





}
