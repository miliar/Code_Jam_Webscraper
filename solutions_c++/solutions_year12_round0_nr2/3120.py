#include <cstdio>
#include <cstring>

const int T_MAX = 100;
const int N_MAX = 100, N_DIM = N_MAX + 10;
const int P_MAX = 10, X_MAX = 30;

int T;
int N, S, p;

int main() {
  scanf("%d", &T);

  for(int t = 1; t <= T; t++)
    {
      printf("Case #%d: ", t);

      scanf("%d %d %d", &N, &S, &p);
      
      int r = 0;
      int s = S;

      for(int i = 0; i < N; i++) {
	int x;
	scanf("%d", &x);

	int n = 3*p - 2;
	int m = 3*p - 4;

	if(n < 0)
	  n = 0;
	if(m < 2)
	  m = 2;

	if(x >= n)
	  r++;
	else if(x >= m && s > 0) {
	  r++;
	  s--;
	}
      }

      printf("%d", r);
      printf("\n");
    }
}
