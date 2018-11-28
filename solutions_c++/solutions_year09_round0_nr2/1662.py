#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int R,C;
int grid[105][105];
char l[105][105];
char next;

#define MAX 100000

char label(int r,int c) {
  if (l[r][c]==0) {
    int n[4];
    if (r==0)
      n[0] = MAX;
    else
      n[0] = grid[r-1][c];
    if (c==0)
      n[1] = MAX;
    else
      n[1] = grid[r][c-1];
    n[2] = grid[r][c+1];
    n[3] = grid[r+1][c];
    int m = 0;
    for(int i=1;i<4;i++) {
      if (n[i]<n[m])
        m = i;
    }
    if (n[m]>=grid[r][c]) {
      l[r][c] = next++;
    } else {
      char chr;
      switch(m) {
        case 0: // north
          chr = label(r-1,c); break;
        case 1: // west
          chr = label(r,c-1); break;
        case 2: // east
          chr = label(r,c+1); break;
        case 3: // south
          chr = label(r+1,c); break;
      }
      l[r][c] = chr;
    }
  }
  return l[r][c];
}

int main() {
  int T;
  cin >> T;
  for(int t=1;t<=T;t++) {
    cout << "Case #" << t << ":" << endl;
    cin >> R >> C;
    for(int i=0;i<R;i++)
      for(int k=0;k<C;k++)
        cin >> grid[i][k];
    for(int i=0;i<C;i++)
      grid[R][i] = MAX;
    for(int i=0;i<R;i++)
      grid[i][C] = MAX;
    memset(l,0,sizeof(l));
    next = 'a';
    for(int i=0;i<R;i++) {
      for(int k=0;k<C;k++)
        cout << label(i,k) << (k<C-1?" ":"");
      cout << endl;
    }
  }
  return 0;
}
