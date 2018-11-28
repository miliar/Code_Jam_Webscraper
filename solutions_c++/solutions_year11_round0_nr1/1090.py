#include <cstdio>
#include <algorithm>

using namespace std;

#define maxn 110

int T;

char s[10];

int who[maxn];
int whe[maxn];

int la[2];
int pa[2];



int main() {
  scanf("%d", &T);
  for (int q = 1; q <= T; q++) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      scanf("%s %d", s, &whe[i]);
      who[i] = s[0] == 'O';
    }

    la[0] = la[1] = 0;
    pa[0] = pa[1] = 1;
    int curt = 0;

    for (int i = 0; i < n; i++) {
      int ind = who[i];
      curt = max(curt, la[ind] + abs(pa[ind] - whe[i])) + 1;
      la[ind] = curt;
      pa[ind] = whe[i];
    }

    printf("Case #%d: %d\n", q, curt);
  }

 	return 0;
}               