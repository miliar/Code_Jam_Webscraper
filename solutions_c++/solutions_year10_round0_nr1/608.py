#include <iostream>
using namespace std;
int f[100];
int main(void) {
  int N , K;
  freopen("asmall.in","r",stdin);
  freopen("asmall.out","w",stdout);
  memset(f,sizeof(f),0);
  f[1] = 1;
  
  for (int i = 2;i<=31;++i) {
    f[i] = 2*f[i-1]+1;
  }

  int T;
  cin >> T;
  int times = 0;
  for (int i = 0;i<T;++i) {
    cin >> N >> K;
    ++times;
    int ans;
    for (ans = 1;ans*f[N] + ans - 1 < K;++ans);
    if (ans*f[N] + ans - 1 == K)
      printf("Case #%d: ON\n",times);
    else printf("Case #%d: OFF\n",times);
  }
  return 0;
}