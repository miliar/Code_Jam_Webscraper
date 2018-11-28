#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

const int MAXN = 110;
const int MAXM = 1010;
char s[MAXN][110], t[MAXM][110];
int best[2][MAXN];
int N, M;
int ans;

void init();
void work();
int main()
{
  int test;
  scanf("%d", &test);
  for (int i = 0; i < test; ++i) {
    init();
    work();
    
    printf("Case #%d: %d\n", i+1, ans);
  }
  return 0;
}

void init()
{
  scanf("%d\n", &N);
  for (int i = 0; i < N; ++i) gets(s[i]);  
  scanf("%d\n", &M);
  for (int i = 0; i < M; ++i) gets(t[i]);

}

void work()
{
  ans = M;
  int p = 0;

  if (M > 0) {    
    for (int i = 0; i < N; ++i) 
      if (strcmp(s[i], t[0]) == 0) best[p][i] = -1; else best[p][i] = 0;
  }

  for (int i = 1; i < M; ++i) {
    p = 1-p;
    for (int j = 0; j < N; ++j) 
      if (strcmp(s[j], t[i]) == 0) best[p][j] = -1; else {
	best[p][j] = i;
	for (int k = 0; k < N; ++k) if (strcmp(s[k], t[i-1]) != 0)
	  if (k == j) best[p][j] <?= best[1-p][k]; else best[p][j] <?= best[1-p][k]+1;    
      }
  }
  
  for (int i = 0; i < N; ++i) if (best[p][i] != -1) ans <?= best[p][i];
}
