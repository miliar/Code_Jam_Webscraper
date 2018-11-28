#include <cstdio>
#include <cstdlib>

const int MAX = 128;

int n,k;
char m[MAX][MAX];
char line[MAX];

const int di[] = { 1, 0, 1,-1};
const int dj[] = { 0, 1, 1, 1};
const int d = sizeof(di) / sizeof(*di);

bool find(int x, int y, int k, char c) {
  if(m[x][y] != c) return false;

  for(int dir=0 ; dir<d ; dir++) {
    int len = 0;
    for(int i=x, j=y ; len<k && i<n && j<n ; i+=di[dir], j+=dj[dir], len++)
      if(m[i][j] != c) break;
    if(len == k) return true;
  }
  return false;
}

int main() {
  int nt0, nt;

  scanf(" %d", &nt0);
  for(nt=1 ; nt<=nt0 ; nt++) {
    scanf(" %d %d", &n, &k);

    for(int i=0 ; i<n ; i++) {
      scanf(" %s", line);
      int q=0;
      for(int j=n-1 ; j>=0 ; j--)
        if(line[j] != '.')
          m[i][q++] = line[j];
      for(; q<n ; q++)
        m[i][q] = '.';
      m[i][n] = '\0';
    }

    bool red = false, blue = false;
    for(int i=0 ; i<n && !blue ; i++)
      for(int j=0 ; j<n && !blue ; j++)
        if(find(i,j,k,'B'))
          blue = true; 
    for(int i=0 ; i<n && !red ; i++)
      for(int j=0 ; j<n && !red ; j++)
        if(find(i,j,k,'R'))
          red = true;

    printf("Case #%d: ", nt);
    if(red && blue) puts("Both");
    else if(red) puts("Red");
    else if(blue) puts("Blue");
    else puts("Neither");
 }

  return 0;
}
