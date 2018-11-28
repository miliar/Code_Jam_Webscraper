#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
using namespace std;

#define For(i,a,b) for (int i = (a),_b = (b); i <= _b; i++)
#define Ford(i,a,b) for (int i = (a),_b = (b); i >= _b; --i)
#define Rep(i,n) for (int i = (0),_n = (n); i < _n; ++i)
#define Repd(i,n) for (int i = ((n)-1); i >= 0; --i)

#define SCAN(t,x) scanf("%" #t,&(x))

#define Fill(a,c) memset(&a, c, sizeof(a))

#define MAX 55

char tab[MAX][MAX];
int N, K;

void left() {
  int i, j, jj;
  for (i = 0; i < N; i++) {
    for (j = jj = 0; j < N; j++) {
      if (tab[i][j]!='.') {
        tab[i][jj] = tab[i][j];
        if (j != jj) {
          tab[i][j] = '.';
        }
        jj++;
      }
    }
  }
}

void right() {
  int i, j, jj;
  for (i = 0; i < N; i++) {
    for (j = jj = N-1; j >= 0; j--) {
      if (tab[i][j]!='.') {
        tab[i][jj] = tab[i][j];
        if (j != jj) {
          tab[i][j] = '.';
        }
        jj--;
      }
    }
  }
}

int dir[][2] = {{1,0}, {0,1}, {1,1}, {1,-1}};

int check() {
  int i, j, k, d, ii, jj;
  int v = 0;
  for (i = 0; i < N; i++) {
    for (j = 0; j < N; j++) {
      if (tab[i][j] != '.')
        for (d = 0; d < 4; d++) { 
          for (k = 1; k < K; k++) {
            ii = i + k*dir[d][0];
            jj = j + k*dir[d][1];
            if (ii >= N || ii < 0 || jj >= N || jj < 0 || tab[ii][jj] != tab[i][j])
              break;
          }
          if (k == K) {
            if (tab[i][j] == 'B')
              v |= 2;
            else
              v |= 1;
          }
        }
    }
  }
  return v;
}



int main() {
  int T;
  int i, j, jj, r;
  scanf("%d",&T);
  For(t,1,T) {
    scanf("%d %d", &N, &K);
    for (i = 0; i < N; i++)
      scanf("%s",tab[i]);
    
//    printf("tab lido (N = %d, K = %d):\n", N, K);
//    for (i = 0; i < N; i++)
//      printf("%s\n",tab[i]);


//    left();
//    r = check();

//    printf("Rodado (esquerda):\n");
//    for (i = 0; i < N; i++)
//      printf("%s\n",tab[i]);
//    printf("Check = %d\n", r);

    right();
    r = check();

//    printf("Rodado (direita):\n");
//    for (i = 0; i < N; i++)
//      printf("%s\n",tab[i]);
//    printf("Check = %d\n", check());

    printf("Case #%d: ",t);
    if (r == 0)
      printf("Neither");
    else if (r == 1)
      printf("Red");
    else if (r == 2)
      printf("Blue");
    else
      printf("Both");
    printf("\n");
  }
  return 0;
}
