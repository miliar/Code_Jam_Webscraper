#include <cstdio>
#include <cstring>

using namespace std;

int main() {
  int n; scanf("%d", &n);
  for(int i=1; i<=n; ++i) {
    char * needle = "welcome to code jam";
    char haystack[1024]; scanf(" %[^\n]", haystack);
    int p;
    for(p=0; haystack[p]; ++p);
    int ans[19] = {0};
    for(--p; p>=0; --p) {
      for(int q=0; needle[q+1]; ++q) {
	if (haystack[p] == needle[q]) {
	  ans[q] = (ans[q] + ans[q+1])%1000;
	}
      }
      if (haystack[p] == 'm') {
	ans[18] = (ans[18]+1)%1000;
      }
    }
    printf("Case #%d: %04d\n", i, ans[0]);
  }
}
