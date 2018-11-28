#include <stdio.h>
#include <string.h>

#define MAX_H 100
#define MAX_W 100

unsigned int alt[MAX_H+2][MAX_W+2];
int ub[MAX_H+2][MAX_W+2];
int u[102*102];

void init_alt() {
  memset(alt,-1,sizeof(alt));
}

void init_u(int h, int w) {
  int a=0;
  for (int i=0; i<h+2; i++)
    for (int j=0; j<w+2; j++)
      ub[i][j] = a++;

  memset(u, -1, sizeof(u));
}

char next='a';
char c[102*102];
char get_col(int a) {
  if (c[a] == 0)
    c[a] = next++;
  return c[a];
}

void reset_col() {
  next='a';
  memset(c,0,sizeof(c));
}

int find(int a) {
  if (u[a] != -1)
    return u[a] = find(u[a]);
  return a;
}
// b -> a
void un(int a, int b) {
  u[b] = find(a);
}

int dir[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int main() {
  int h, w, t;

  scanf("%d", &t);

  for (int cs=1; cs<=t; cs++) {
    scanf("%d %d", &h, &w);
    init_alt();
    init_u(h,w);
    reset_col();
    for (int i=0; i<h; i++)
      for (int j=0; j<w; j++)
        scanf("%d", &alt[i+1][j+1]);

    for (int i=1; i<=h; i++)
      for (int j=1; j<=w; j++) {
        unsigned int bst = alt[i+dir[0][0]][j+dir[0][1]];
        int bstd = 0;
        for (int k=1; k<4; k++)
          if (bst > alt[i+dir[k][0]][j+dir[k][1]]) {
            bst = alt[i+dir[k][0]][j+dir[k][1]];
            bstd = k;
          }

        if (bst < alt[i][j])
          un(ub[i+dir[bstd][0]][j+dir[bstd][1]], ub[i][j]);
      }

    printf("Case #%d:\n", cs);
    for (int i=1; i<=h; i++)
      for (int j=1; j<=w; j++)
        printf("%c%s", get_col(find(ub[i][j])), (j == w ? "\n" : " "));
  }

  return 0;
}
