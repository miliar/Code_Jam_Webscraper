#include<cstdio>

using namespace std;

int main()
{
  int T;
  scanf("%d", &T);
  for(int i=1; i<=T; ++i) {
    int N, K;
    scanf("%d%d", &N, &K);
    printf("Case #%d: ", i);
    puts((K+1) % (1<<N) == 0 ? "ON" : "OFF");
  }
  return 0;
}

