#include <cstdio>
#include <algorithm>
using namespace std;

const int maxn = 80;

int n;
int mp[maxn];

void init() {
  scanf("%d\n", &n);
  char st[maxn];
  for (int i = 0; i < n; i++) {
    fgets(st, maxn, stdin);
    int min = 0;
    for (int j = 0; j < n; j++)
      if (st[j] == '1') min = j;
    mp[i] = min;
    //printf("%d\n", min);
  }  
}

int work() {
  int res = 0;
  for (int i = 0; i < n; i++) {
    if (mp[i] <= i) continue;
    int pos = 0;
    for (int j = i; j < n; j++) {
      if (mp[j] <= i) {
	pos = j;
	break;
      }
    }
    for (int j = pos; j > i; j--) {
      swap(mp[j-1], mp[j]);
      res++;
    }
    //printf("%d %d\n", i, pos);
    //for (int j = 0; j < n; j++) printf("%d ", mp[j]);
    //printf("\n");
  }
  return res;
}


int main() {
  int t;
  scanf("%d\n", &t);
  for (int i = 1; i <= t; i++) {
    init();
    printf("Case #%d: %d\n", i, work());
  }
}
