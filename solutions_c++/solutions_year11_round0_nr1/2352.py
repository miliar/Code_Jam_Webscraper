#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;
int main() {
  int T;
  int M;
  scanf("%d",&T);
  for (int case_n = 1 ; case_n <= T ; case_n++) {
    scanf("%d",&M);

    char p_v;
    int u_v;
    int pos[2] = {1, 1};
    int last[2] = {0, 0};
    int tot = M;
    for (int i = 0 ; i < M ; i++) {
      scanf(" %c %d",&p_v, &u_v);
      if (p_v == 'O') {
	
	int andadas = max(-pos[0] - last[0] + u_v, 0);
	if (u_v < pos[0]) {
	  andadas = max(pos[0] -last[0] - u_v, 0);
	}

	last[1] += 1+andadas;
	tot += andadas;
	last[0] = 0;
	pos[0] = u_v;
      }
      else {
	int andadas = max(-pos[1] - last[1] + u_v, 0);
	if (u_v < pos[1]) {
	  andadas = max(pos[1] -last[1] - u_v, 0);
	}
	last[0] += 1+andadas;

	last[1] = 0;
	tot += andadas;
	pos[1] = u_v;
      }
    }
   
    printf("Case #%d: %d\n", case_n, tot);
  }

  return 0;
}
