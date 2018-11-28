#include <cstdio>

using namespace std;

int c[1123];

int main() {
  int nt, cases = 1;
  scanf(" %d", &nt);
  while (nt--) {
    int n;
    scanf(" %d", &n);
    for (int i = 0; i < n; i++)
      scanf(" %d", &c[i]);
    
    int res = -1;
    for (int i = 0; i < n; i++) {
      int patrick = c[i], sean = 0, sum = 0;
      for (int j = 0; j < n; j++)
	if (i != j) {
	  sean ^= c[j];
	  sum += c[j];
	}
      if (patrick == sean && sum > res)
	res = sum;
    }

    printf("Case #%d: ", cases++);
    if (res == -1)
      printf("NO\n");
    else printf("%d\n", res);
  }

  return 0;
}
