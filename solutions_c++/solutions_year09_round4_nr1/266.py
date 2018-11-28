#include <cstdio>
#include <string.h>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

const int MAXN = 40;

int a[MAXN];
int n;
char buf[MAXN  + 1];

int readdata() {
  int i, j;
  char c;
  scanf("%d\n", &n);
  for (int i = 0; i < n; ++i) {
    a[i] = 0;
    gets(buf);
    for (int j = 0; j < n; ++j)
      if (buf[j] == '1') a[i] = j;
    fprintf(stderr, "a[%d] = %d\n", i, a[i]);
  }
}

int solve() {
  int i, j, res, y, k;

  res = 0;
  
  for (i = 0; i < n; ++i)
    if (a[i] > i) 
      for (j = i + 1; j < n; ++j)
	if (a[j] <= i) {
	  y = a[j];
	  for (k = j; k > i; --k)
	    a[k] = a[k-1];
	  a[i] = y;
	  res += j - i;

	  fprintf(stderr, "\n");
	  for (y = 0; y < n; ++y)
	    fprintf(stderr, "a[%d] = %d\n", y, a[y]);
	  break;
	}

  return res;
}

int main () {
  int t;

  scanf("%d\n", &t);
  for (int i = 1; i <= t; ++i) {
    readdata();
    printf("Case #%d: %d\n", i, solve());
  }
  return 0;
}
