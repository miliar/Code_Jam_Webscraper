#include <cstdio>
#include <map>
#include <string>

using namespace std;

void solve(int P) {
  int S, Q;
  map<string, int> engine;

  scanf("%d", &S);
  while (getchar() != '\n');
  for (int i = 0; i < S; ++i) {
    char str[200];
    fgets(str, 200, stdin);
    engine[str] = i;
  }

  scanf("%d", &Q);
  while (getchar() != '\n');

  int seen[200], unseen = S, switches = 0;
  memset(seen, 0, sizeof(seen));
  for (int i = 0; i < Q; ++i) {
    char str[200];
    fgets(str, 200, stdin);
    int q = engine[str];
    if (!seen[q]) {
      if (--unseen == 0) {
	++switches;
	memset(seen, 0, sizeof(seen));
	unseen = S-1;
      }
      seen[q] = true;
    }
  }
  printf("Case #%d: %d\n", P, switches);
}

int main(void) {
  int N;
  scanf("%d", &N);
  for (int i = 1; i <= N; ++i) solve(i);
  return 0;
}
