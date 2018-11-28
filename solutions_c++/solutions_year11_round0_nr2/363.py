#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 1010;

int n, m, k;
char com[MAXN][5];
char opp[MAXN][5];
char s[MAXN];

void init()
{
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) scanf("%s", com[i]);
  scanf("%d", &m);
  for (int i = 0; i < m; ++i) scanf("%s", opp[i]);
  scanf("%d", &k);
  scanf("%s", s);
}

bool cmp(char s1, char s2, char c1, char c2) {
  return (s1 == c1 && s2 == c2) || (s1 == c2 && s2 == c1);
}

bool comb(char c, int &top) {
  for (int i = 0; i < n; ++i)
    if (cmp(com[i][0], com[i][1], c, s[top]))  {
      s[top] = com[i][2];
      return 1;
    }

  return 0;
}

bool clear(int c, int &top)
{
  for (int i = 0; i < m; ++i) 
    for (int j = 0; j <= top; ++j) 
      if (cmp(opp[i][0], opp[i][1], c, s[j])) {
	top = -1;
	return 1;  
      }
  return 0;
}


void solve()
{
  int top = 0;
  for (int i = 1; i < k; ++i) {
    if (top < 0) { s[++top] = s[i]; continue; }
    if (comb(s[i], top)) continue;
    if (clear(s[i], top)) continue;
    s[++top] = s[i];
  }
  
  printf("[");
  for (int i = 0; i <= top; ++i) {
    if (0 < i) printf(", ");
    printf("%c", s[i]);
  }
  printf("]\n");
}

int main()
{
  int t;
  scanf("%d", &t);
  for (int l = 1; l <= t; ++l) {
    printf("Case #%d: ", l);
    init();
    solve();
  }
  return 0;
}
