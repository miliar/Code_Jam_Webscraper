#include <cstdio>
#include <vector>
using namespace std;

int com[26][26];
int opp[26][26];
int vstup[200];

int main() {
  int T;
  scanf("%d", &T);
  for(int t = 1; t <= T; t++) {

    for(int a = 0; a < 26; a++) for(int b = 0; b < 26; b++) {
      opp[a][b] = 0;
      com[a][b] = -1;
    }

    int C, D, N;
    scanf("%d", &C);
    for(int i = 0; i < C; i++) {
      char buf[10];
      scanf("%s", buf);
      int a = buf[0]-'A', b = buf[1]-'A', c = buf[2]-'A';
      com[a][b] = c;
      com[b][a] = c;
    }
    scanf("%d", &D);
    for(int i = 0; i < D; i++) {
      char buf[10];
      scanf("%s", buf);
      int a = buf[0]-'A', b = buf[1]-'A';
      opp[a][b] = 1;
      opp[b][a] = 1;
    }
    scanf("%d", &N);
    {
      char buf[200];
      scanf("%s", buf);
      for(int i = 0; i < N; i++) {
        vstup[i] = buf[i]-'A';
      }
    }

    int el[200];
    int ellen = 0;
    int present[26];
    for(int i = 0; i < 26; i++) present[i] = 0;

    for(int i = 0; i < N; i++) {
      int next = vstup[i];
      if(ellen == 0) {
        el[ellen++] = next;
        present[next]++;
      }
      else {
        int top = el[ellen-1];
        if(com[top][next] != -1) {
          ellen--;
          present[top]--;
          next = com[top][next];
        }
        int conflicted = 0;
        for(int uu = 0; uu < 26; uu++) {
          if(present[uu] && opp[uu][next]) conflicted = 1;
        }
        if(conflicted) {
          ellen = 0;
          for(int uu = 0; uu < 26; uu++) present[uu] = 0;
        }
        else {
          el[ellen++] = next;
          present[next]++;
        }
      }
    }

    printf("Case #%d: [", t);
    for(int i = 0; i < ellen; i++) {
      if(i != 0) printf(", ");
      printf("%c", el[i]+'A');
    }
    printf("]\n");

  }
  return 0;
}

