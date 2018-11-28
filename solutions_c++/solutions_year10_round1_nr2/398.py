#include <string>
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
int D, I, M,N, a[101];
int inf = 1000000000;
int dfs(int l, int i)
{
  // printf("%d %d\n", l, a[i]);
  if( i >= N)
    return 0;
  int m = 1000000000;
  if(abs(a[i]- l) <= M || l == inf)
    {
      m = min(m, dfs(a[i], i+1));
    }
  //try delete
  m = min(m, D + dfs(l, i+1) );
  //try insert
  if( abs(a[i] -  l) > M && l != inf)
    {
	if( a[i] > l + M && M != 0)
	  m = min( m, I + dfs(l + M, i) );
	else if( a[i] > l){
	  for(int j  = 0; j <=255; j++)
	    if( abs(l-j) <= M && abs(a[i] -j) <= M ){ 
	      m = min(m, I + dfs(j, i) );
	      break;
	    }
	}
	else if( a[i] < l - M && M != 0)
	  m = min( m, I + dfs(l - M, i) );
	else if( a[i] < l){
	  for(int j  = 0; j <=255; j++)
	    if( abs(l-j) <= M && abs(a[i] -j) <= M ){ 
	      m = min(m, I + dfs(j, i) );
	      break;
	    }
	}
	
    }
  //try change the val
  for(int j = 0 ; j <=255; j++)
    if( abs(j - l) <= M && l != inf)
      m = min(m, abs(j - a[i]) + dfs( j, i+1) );
  if( i == 0 )
    for(int j = 0 ; j <=255; j++)
      m = min(m, abs(j - a[i]) + dfs( j, i+1) );
  return m;
}
int main()
{
  int T;
  scanf("%d", &T);
  for(int c = 1; c <=T; c++)
    {
      scanf("%d %d %d %d", &D, &I, &M, &N);
      for(int i = 0 ; i < N; i++)
	scanf("%d", a + i);
      printf("Case #%d: %d\n", c, dfs(inf, 0));
    }
}
