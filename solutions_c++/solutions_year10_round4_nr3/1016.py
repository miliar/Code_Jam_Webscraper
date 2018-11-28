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

#define MAX 500
int m[MAX][MAX];

void read() {
  int R;
  int x1, x2, y1, y2, i, j;
  memset(m,0,sizeof(m));
  scanf("%d",&R);
  Rep(k,R) {
    scanf("%d%d%d%d\n",&x1,&y1,&x2,&y2);
    //    printf("%d %d %d %d\n", x1, y1, x2, y2);
    for (i = x1 ; i <= x2; i++)
      for (j = y1 ; j <= y2; j++) {
        //        printf("(%d, %d)\n",i,j);
        m[i+1][j+1] = 1;
      }
  }
}

void prt() {
  int i, j;
  for (i=1;i<100;i++) {
    for(j=1;j<100;j++) {
      printf("%d",m[i][j]);
    }
    printf("\n");
  }
  printf("\n");
}

int step() {
  int i, j;
  int found = 0;
  for (i=MAX-1; i>=0; i--)
    for (j=MAX-1; j>=0; j--)
      if (m[i][j] && !m[i-1][j] && !m[i][j-1]) {
        m[i][j] = 0;
      } else if (!m[i][j] && m[i-1][j] && m[i][j-1]) {
        found = 1;
        m[i][j] = 1;
      } else if (m[i][j]) {
        found = 1;
      }
  return found;
}

int count() {
  int i = 0;
  //  prt();
  while (step()) {
    //       prt();
    i++;
  }
  return i+1;
}


int main() {
  int T;
  scanf("%d",&T);
  For(t,1,T) {
    read();
    //    printf("Read ok\n");
    printf("Case #%d: %d\n",t,count());
  }
  return 0;
}
