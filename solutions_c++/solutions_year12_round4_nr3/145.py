#include <cstdio>
#include <ctime>
#include <cstdlib>

int heights[10];
int req[10];

int main() {
  int T;
  srand(time(NULL));
  scanf("%d", &T);
  for(int tc = 1; tc <= T; ++tc) {
    int N;
    scanf("%d", &N);
    for(int i = 0; i < N - 1; ++i) {
      scanf("%d", req + i);
      req[i] --;
    }

    int fcnt = 0;
failed:
    if(fcnt++ >= 10000000)
      goto impossible;
    for(int i = 0; i < N; ++i)
      heights[i] = rand()%1001;

    for(int i = 0; i < N - 1; ++i) {
      for(int j = i + 1; j < req[i]; ++j)
        if(heights[j] >= (j - i) * (heights[req[i]] - heights[i])/(req[i] - i) + heights[i])
          goto failed;

      for(int j = req[i] + 1; j < N; ++j)
        if(heights[j] > (j - i) * (heights[req[i]] - heights[i])/(req[i] - i) + heights[i])
          goto failed;
    }

    printf("Case #%d:", tc);
    for(int i = 0; i < N; ++i)
      printf(" %d", heights[i]);
    puts("");
    continue;

impossible:
    printf("Case #%d: Impossible\n", tc);
  }
}
