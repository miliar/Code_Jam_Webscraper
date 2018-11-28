#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

const int maxc = 256;

int used[maxc];
int comb[maxc][maxc];
int clr[maxc][maxc];

int stack[maxc];
int top;

char buffer[1024];

int nchar() {
  int c = getchar();
  while (c > 'Z' || c < 'A') c = getchar();
  return c;
}

void checkclear() {
  for (int i = 0; i < top; ++i)
    for (int j = i+1; j < top; ++j)
      if (clr[stack[i]][stack[j]]) {
	top = 0;
	break;
      }
}

void proc() {
  memset(used, 0, sizeof(used));
  memset(comb, 0, sizeof(comb));
  memset(stack, 0, sizeof(stack));
  memset(clr, 0, sizeof(clr));

  top = 0;
  int t;
  scanf("%d", &t);
  while (t--) {
    scanf("%s", buffer);
    comb[buffer[0]][buffer[1]] = buffer[2];
    comb[buffer[1]][buffer[0]] = buffer[2];
  }
  scanf("%d", &t);
  while (t--) {
    scanf("%s", buffer);
    clr[buffer[0]][buffer[1]] = 1;
    clr[buffer[1]][buffer[0]] = 1;
  }
  scanf("%d", &t);
  while (t--) {
    stack[top++] = nchar();
    while (top >= 2 && comb[stack[top-1]][stack[top-2]]) {
      stack[top-2] = comb[stack[top-1]][stack[top-2]];
      --top;
    }
    checkclear();
  }
  printf("[");
  for (int i = 0; i < top; ++i) {
    if (i) printf(", ");
    printf("%c", (char)stack[i]);
  }
  printf("]");
}

int main() {
  //  freopen("input.txt", "r", stdin);
  int T;
  scanf("%d", &T);
  while (T--) {
    static int id = 0;
    printf("Case #%d: ", ++id);
    proc();
    putchar('\n');
  }
  return 0;
}
