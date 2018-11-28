#include<stdio.h>
#include<stdlib.h>

#define MAXN 10000

int T;
int N, M, A;

int gcd(int a, int b){
  int c;
  while(true){
    c = a%b;
    if (!c)
      return b;
    a = b;
    b = c;
  }
}

int main(){
  int i;
  scanf("%d", &T);
  for(int nc = 0; nc < T; nc++){
    printf("Case #%d: ", nc+1);
    scanf("%d %d %d\n", &N, &M, &A);
    for(int x1 = 0; x1 <= N; x1++){
      for(int y1 = x1; y1 <= M; y1++){
	if (!y1)
	  continue;
	int residue2 = A + x1*y1;
	if (residue2 % gcd(x1, y1))
	  continue;
	int diff = 1;
	int bot = A / M;
	for(int x2 = N; x2 >= bot; x2 -= diff){
	  int residue = A + x1*y1 - x2*y1;
	  if (residue && (x1 == 0 || residue % x1))
	    continue;
	  int y2 = x1 ? residue / x1 : 0;
	  if (y2 >= 0 && y2 <= M){
	    printf("%d 0 0 %d %d %d\n", x1, y1, x2, y2);
	    goto done;
	  }
	  if (y2 > M)
	      break;
	  diff = x1 / gcd(x1, y1);
	}
      }
    }
    printf("IMPOSSIBLE\n");
  done:
    fflush(stdout);
  }
}
