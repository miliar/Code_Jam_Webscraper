#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
using namespace std;
#define N 500000
#define M 1000000007
/*
ax*by - ay*bx == A = kn+r  A=(k+1)*n-1*(n-r) n, (n, 1) (n-r, k+1),

max(ax,bx,0) - min(ax,bx,0) <= n
max(ay,by,0) - min(ay,by,0) <= m
*/

int main()
{
  int t, index;
  int n, m, A;
  
  scanf("%d", &t);
  for(index = 1; index <= t; index++) {
    scanf("%d%d%d", &n, &m, &A);
    if(A <=0 || A > n*m)
    	printf("Case #%d: IMPOSSIBLE\n", index);
 	else if(A % n == 0)
		printf("Case #%d: %d %d %d %d %d %d\n", index, 0, 0, n, 0, 0, A/n);
	else
		printf("Case #%d: %d %d %d %d %d %d\n", index, 0, 0, n, 1, n-A%n, A/n+1);
  }
}
