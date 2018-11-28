#include <cstdio>

int main()
{
  int m[100][100];
  int N;
  scanf("%d", &N);
  for(int nc=1; nc<=N; ++nc) {
    int H, W, R;
    scanf("%d%d%d", &H, &W, &R);
    for(int i=0; i<100; ++i)
      for(int j=0; j<100; ++j)
	m[i][j] = 0;
    m[0][0] = 1;
    for(int i=0; i<R; ++i) {
      int r, c;
      scanf("%d%d", &r, &c);
      m[r-1][c-1] = -1;
    }
    for(int i=0; i<100; ++i) {
      for(int j=0; j<100; ++j)
	if(m[i][j] == 0) {
	  if(i > 1 && j > 0 && m[i-2][j-1] >= 0)
	    m[i][j] += m[i-2][j-1];
	  if(i > 0 && j > 1 && m[i-1][j-2] >= 0)
	    m[i][j] += m[i-1][j-2];
	  m[i][j] %= 10007;
	}
    }
    /*
    for(int i=0; i<20; ++i) {
      for(int j=0; j<20; ++j)
	printf("%3d ", m[i][j]);
      putchar('\n');
    }
    */
    printf("Case #%d: %d\n", nc, m[H-1][W-1]);
  }
  return 0;
}
