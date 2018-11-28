#include <cstdio>
using namespace std;

int main()
{
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; ++t) {
    printf("Case #%d: ", t+1);
    int N, K;
    scanf("%d%d", &N, &K);
    if (K % (1 << N) == (1 << N) - 1)
      puts("ON");
    else
      puts("OFF");
  }
}
