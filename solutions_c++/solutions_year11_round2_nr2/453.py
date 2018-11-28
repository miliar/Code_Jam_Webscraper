#include <stdlib.h>
#include <stdio.h>

const int MAXN = 1024;

int T;
int pos[MAXN];
int count[MAXN];


int main() {

  scanf("%d", &T);
  for(int casen = 0; casen < T; ++casen) {
    int n;
    long long d;
    scanf("%d", &n);
    scanf("%lld", &d);
    for(int i = 0; i < n; ++i) {
      scanf("%d %d", &pos[i], &count[i]);
    }

    long long ans2 = 0;
    for(int i = 0; i < n; ++i) {
      for(int j = 0; j < n; ++j) {
	if(pos[i] > pos[j]) continue;
	int dist = abs(pos[j] - pos[i]);
	int cows = 0;
	for(int k = 0; k < n; ++k) {
	  if(pos[i] <= pos[k] && pos[k] <= pos[j]) {
	    cows += count[k];
	  }
	}
	long long a2 = (cows-1) * d - dist;
	if(ans2 < a2) {
	  ans2 = a2;
	}
      }
    }
    printf("Case #%d: %.1lf\n", 1+casen, ans2/2.0);
  }

  return(0);
}
