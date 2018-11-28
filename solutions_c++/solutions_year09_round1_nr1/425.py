#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <map>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>

using namespace std;

int bases[20], pos[20];
map<int, int> foi;
map<pair<int, int>, int> memo;

int is_happy(int n, int b) {
  long long int m = 0;
  pair<int, int> p = make_pair(n, b);
  if (n == 1)
    return 1;
  if (memo.find(p) != memo.end())
    return memo[p];
  if (foi.find(n) != foi.end())
    return memo[p] = 0;
  foi[n] = 1;
  while (n) {
    m += (n%b) * (n%b);
    n /= b;
  }
  return memo[p] = is_happy(m, b);
}

vector<int> happy[15];
int memo_res[10000];

int main() {
  int nt, cases = 1;
  char line[100];

  memset(memo_res, -1, sizeof(memo_res));
  for (int j = 2; j <= 10; j++) {
    memo.clear();
    for (int i = 2; i < 12000000; i++) {
      foi.clear();
      if (is_happy(i, j))
	happy[j].push_back(i);
    }
  }
      
  scanf(" %d ", &nt);
  while (nt--) {
    gets(line);
    int n = 0, key = 0;
    char *tok = strtok(line, " ");
    while (tok != NULL) {
      bases[n] = atoi(tok);
      pos[n++] = 0;
      key |= 1<<atoi(tok);
      tok = strtok(NULL, " ");
    }

    if (memo_res[key] != -1) {
      printf("Case #%d: %d\n", cases++, memo_res[key]);
      continue;
    }

    int res, menor;
    bool igual;
    do {
      igual = true;
      menor = 0;
      res = happy[bases[0]][pos[0]];
      for (int i = 1; i < n; i++) {
	igual = igual && (happy[bases[i]][pos[i]] == happy[bases[i-1]][pos[i-1]]);
	if (happy[bases[i]][pos[i]] < happy[bases[menor]][pos[menor]])
	  menor = i;
      }
      pos[menor]++;
    } while (!igual);
    memo_res[key] = res;
    printf("Case #%d: %d\n", cases++, res);
  }

  return 0;
}
