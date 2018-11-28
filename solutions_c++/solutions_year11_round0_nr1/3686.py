#include<cstdio>
#include<algorithm>
using namespace std;

int main(){

  int T;
  scanf("%d", &T);

  for(int t = 1; t <= T; t++){

    int N;
    scanf("%d", &N);

    int step[2] = {0}, pos[2] = {1, 1};

    for(int i = 0; i < N; i++){
      char c; int d;
      scanf(" %c %d", &c, &d);
      int x = (int)(c == 'O');
      step[x] = max(step[x] + abs(pos[x] - d), step[1 - x]) + 1;
      pos[x] = d;
    }

    printf("Case #%d: %d\n", t, max(step[0], step[1]));
  }

  return 0;
}
