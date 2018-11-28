#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>

using namespace std;

int g[1024];

unsigned long long count(int s, int R, int K, int N)
{
  unsigned long sum = 0;
  int c = 0;
  for (int i = 0; i < R; ++i){
	c = 0;
	for (int j = 0; j < N; ++j){
	  c += g[(s+j)%N];
	  if (c > K){
		c -= g[(s+j)%N];
		s = (s+j)%N;
		break;
	  }
	} 
	sum += c;
  }
  return sum;
}

unsigned long long solve(int R, int K, int N)
{
  unsigned long long sum = 0, rsum = 0;
  int c = 0;
  int s = 0;
  int r = 0, r0 = 0;
  char pos[N];
  int rpos[N];
  memset(pos, 0, N);
  memset(rpos, 0, N*sizeof(int));
  if (R <= N){
	return count(0, R, K, N);
  }else {
	for (int i = 0; i < N+1; ++i){
	  c = 0;
	  pos[s] = 1;
	  rpos[s] = i;
	  for (int j = 0; j < N; ++j){
		c += g[(s+j)%N];
		if (c > K){
		  c -= g[(s+j)%N];
		  s = (s+j)%N;
		  break;
		}
	  } 
	  if (pos[s] == 1){
		r0 = rpos[s];
		r = i + 1 - r0;
		break;
	  }
	}
	
	sum = count(0, r0, K, N);
	rsum = count(s, r, K, N);
	sum += (R-r0)/r*rsum;
	sum += count(s, (R-r0)%r, K, N);
  }
  
  return sum;
}

int main()
{
  int T, R, K, N;
  unsigned long long sum = 0;

  scanf("%d", &T);
  for (int k = 0; k < T; ++k){
	scanf("%d %d %d", &R, &K, &N);
	for (int j = 0; j < N; ++j){
	  scanf("%d", g+j);
	}
	sum = solve(R, K, N);
	printf("Case #%d: %llu\n",k+1,sum);
  }
}

