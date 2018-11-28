#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std; typedef unsigned long ul; typedef long long ll;
typedef unsigned long long ull;

char board[60][60];
int n,k;

int run(int x,int y, int dx, int dy, int c)
{
  int r=0,m=0;
  for(; x>=0 && x<n && y>=0 && y<n; x+=dx, y+=dy)
  {
    if (board[x][y] == c) r++; else { m >?= r; r=0; }
  }
  m >?= r; return m;
}

int main()
{
int cases;

cin >> cases; getchar();

for(int loop=1;loop<=cases;loop++)
{
  int len[60];

  cin >> n >> k; getchar();
  memset(len,0,sizeof(len));
  memset(board,0,sizeof(board));

  for(int i=0;i<n;i++)
  {
    char line[80];
    scanf("%s",line);
    for(int j=n-1;j>=0;j--)
     if (line[j]=='R') board[i][len[i]++] = 1;
     else if (line[j]=='B') board[i][len[i]++] = 2;

    //for(int j=0;j<len[i];j++) printf("%d",board[i][j]); putchar(10);
  }

  int R=0, B=0;
  // vert
  for(int i=0;i<n;i++) { R >?= run(0,i,1,0,1); B >?= run(0,i,1,0,2); }
  // hor
  for(int i=0;i<n;i++) { R >?= run(i,0,0,1,1); B >?= run(i,0,0,1,2); }
  for(int i=0;i<n;i++)
  { 
    R >?= run(i,0,1,1,1); R >?= run(0,i,1,1,1);
    B >?= run(i,0,1,1,2); B >?= run(0,i,1,1,2);
  }
  for(int i=0;i<n;i++)
  {
    R >?= run(i,0,-1,1,1); R >?= run(n-1,i,-1,1,1);
    B >?= run(i,0,-1,1,2); B >?= run(n-1,i,-1,1,2);
  }

  fprintf(stderr,"%d %d\n", R, B);

  printf("Case #%d: %s",loop,
    (R < k) ? ( (B<k?"Neither":"Blue") )
            : ( (B<k?"Red":"Both") ) );

  puts("");
  fflush(stdout);
}

}
