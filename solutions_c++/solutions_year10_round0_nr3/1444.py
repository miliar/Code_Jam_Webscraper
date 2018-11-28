#include <iostream>
#include <string.h>
using namespace std;

const int max_k = 10000000;
int follower[max_k];
int size[max_k];
int costs[max_k];

int main()
{
 
  memset(follower,0,max_k);
  memset(size,0,max_k);
  memset(costs,0,max_k);

  int  R, T, k, N;
  fscanf(stdin, "%d", &T);
  for (int t = 1; t <= T; t++) {
    fscanf(stdin, "%d %d %d", &R, &k, &N); 
    for (int i = 0; i < N; i++)
      fscanf(stdin, "%d", &size[i]);

    for (int i = 0; i < N; i++) {
      int in_group = size[i];
      for(int j = 1; j <= N; j++) {
	if(in_group + size[(i+j)%N] > k || j == N) {
	  follower[i] = (i+j)%N;
	  costs[i] = in_group;
	  break;
	}
	in_group += size[(i+j)%N];
      }
    }
    
    int next = 0;
    unsigned long profit = 0;
    for(int i = 0; i < R; i++) {
      profit += costs[next];
      next = follower[next];
    }
    printf("Case #%d: %ld\n", t, profit);

    memset(follower,0,N);
    memset(size,0,N);
    memset(costs,0,N);

  }
  return 0;
}
