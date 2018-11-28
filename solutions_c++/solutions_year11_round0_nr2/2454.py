#include <cstdio>
#include <cstring>

using namespace std;

char rep[37][4];
int oppose[29];
char str[1001];

int main() {
  int T; scanf("%d", &T);
  for(int t=1; t<=T; ++t) {
    int c, d, n;
    scanf("%d", &c);
    for(int i=0; i<c; ++i) {
      scanf(" %s", rep[i]);
    }
    scanf("%d", &d);
    for(int i=0; i<d; ++i) {
      char tmp[3]; scanf(" %s", tmp);
      oppose[i] = (1<<(tmp[0]-'A')) | (1<<(tmp[1]-'A'));
    }
    scanf("%d", &n);
    int m = 0, mask = 0, cnt[26] = {0};
    for(int i=0; i<n; ++i) {
      char ch; scanf(" %c", &ch);
      str[m++] = ch; ++cnt[ch-'A']; mask |= 1<<(ch-'A');
      for(int j=0; m >= 2 && j<c; ++j) {
	if ((str[m-2] == rep[j][0] &&
	    str[m-1] == rep[j][1]) ||
	    (str[m-2] == rep[j][1] &&
	     str[m-1] == rep[j][0])) {
	  if (!--cnt[str[m-2]-'A']) {
	    mask ^= 1<<(str[m-2]-'A');
	  }
	  if (!--cnt[str[m-1]-'A']) {
	    mask ^= 1<<(str[m-1]-'A');
	  }
	  ++cnt[rep[j][2]-'A']; mask |= 1<<(rep[j][2]-'A');
	  str[m-2] = rep[j][2]; --m; j = -1;
	}
      }
      for(int j=0; j<d; ++j) {
	if (__builtin_popcount(oppose[j]&mask) == 2) {
	  mask = 0; memset(cnt, 0, sizeof(cnt)); m = 0;
	}
      }
    }

    printf("Case #%d: [", t);
    for(int i=0; i<m; ++i) {
      printf(i?", %c":"%c", str[i]);
    }
    printf("]\n");
  }
}
