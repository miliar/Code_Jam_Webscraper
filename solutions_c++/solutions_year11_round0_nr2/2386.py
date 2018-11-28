#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

char comb[100][100];
bool oppo[100][100];

int main() {
  int nt, cases = 1;

  scanf(" %d", &nt);
  while (nt--) {
    int C;
    scanf(" %d", &C);
    memset(comb, -1, sizeof(comb));
    for (int i = 0; i < C; i++) {
      char u, v, t;
      scanf(" %c%c%c", &u, &v, &t);
      comb[u][v] = comb[v][u] = t;
    }

    int D;
    scanf(" %d", &D);
    memset(oppo, 0, sizeof(oppo));
    for (int i = 0; i < D; i++) {
      char u, v;
      scanf(" %c%c", &u, &v);
      oppo[u][v] = oppo[v][u] = true;
    }

    int n;
    scanf(" %d", &n);
    vector<char> seq;
    for (int i  = 0; i < n; i++) {
      char c;

      scanf(" %c", &c);
      if (!seq.empty() && comb[seq.back()][c] != -1) {
	char t = seq.back();
	seq.pop_back();
	seq.push_back(comb[t][c]);
	c = comb[t][c];
      } else
	seq.push_back(c);
      
      for (int j = 0; j < (int)seq.size() - 1; j++)
	if (oppo[seq[j]][c])
	  seq.clear();
    }

    printf("Case #%d: [", cases++);
    for (int i = 0; i < (int)seq.size() - 1; i++)
      printf("%c, ", seq[i]);
    if (!seq.empty()) printf("%c", seq.back());
    printf("]\n");
  }

  return 0;
}
