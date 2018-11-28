#include<cstdio>
#include<algorithm>

int main()
{
  int T;
  scanf("%d", &T);
  for(int C=1; C<=T; ++C) {
    int n, c[1024];
    scanf("%d", &n);
    for(int i=0; i<n; ++i)
      scanf("%d", &c[i]);
    std::sort(c, c+n);
    int t = 0;
    for(int i=0; i<n; ++i)
      t ^= c[i];
    printf("Case #%d: ", C);
    if(t != 0) puts("NO");
    else {
      for(int i=1; i<n; ++i)
	t += c[i];
      printf("%d\n", t);
    }
  }
  return 0;
}
