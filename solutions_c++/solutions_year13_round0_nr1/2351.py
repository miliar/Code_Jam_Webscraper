#include <iostream>
#include <assert.h>
#include <stdio.h>
#include <string>

using namespace std;

#define N 4

typedef char position_t[N][N];

char judge_dir(position_t pos,int x, int y, int vx, int vy, int n);

/* return the judgement given a position:
    X: X wins
    O: O wins
    D: Draw
    N: Not complete
*/
char judge(position_t pos) {
  
  bool not_complete = false;

  struct Dir {
    int x;
    int y;
    int vx;
    int vy;
    Dir() { }
    Dir(int xx, int yy, int vxx, int vyy):
        x(xx),y(yy),vx(vxx),vy(vyy) { }
  } dirs[N*N+2];
  
  int i = 0;
  int j;
  
  for(j = 0; j < N; j++) {
    dirs[i++] = Dir(0,j,1,0); // row j
    dirs[i++] = Dir(j,0,0,1); // col j
  }
  dirs[i++] = Dir(0,0,1,1);
  dirs[i++] = Dir(N-1,0,-1,1);
        
  for(j = 0; j < i; j++) {
    const Dir& d = dirs[j];
    int rc = judge_dir(pos,d.x,d.y,d.vx,d.vy,N);
    if (rc == 'X' || rc == 'O') {
      return rc;
    }
    else if (rc == 'N')
      not_complete = true;
  }

  if (not_complete)
    return 'N';
  else
    return 'D';
}

void print_position(position_t pos)
{
  for(int i = 0; i < N; i++) {
    for(int j = 0; j < N; j++)
      printf("%c",pos[i][j]);
    printf("\n");
  }
}

char judge_dir(position_t pos,int x, int y, int vx, int vy, int n)
{
  char p = 0;
  bool blank = false;
  bool mismatch = false;

  while(n-- > 0) {
    char pp = pos[y][x];
    if (pp == 'T') {
      ;
    } else if (pp == '.') {
      blank = true;
    } else if (pp == 'X' || pp == 'O') {
      if (!p) {
        p = pp;
      } else if (pp != p) {
        mismatch = true;
      }
    } else {
      assert(0);
    }

    x += vx;
    y += vy;
  }

  if (!mismatch && !blank) {
    assert(p);
    return p; // match
  } else if (blank) {
    return 'N';
  } else {
    return 'D';
  }
}

int main()
{
  int n;
  cin >> n;

  for(int i = 1; i <= n; i++) {
    position_t pos;
    for(int j = 0; j < N; j++) {
      for(int k = 0; k < N; k++) {
        char c;
        cin >> c;
        pos[j][k] = c;
      }
    }
    char rc = judge(pos);

    printf("Case #%d: ",i);
    if (rc == 'X' || rc == 'O')
      printf("%c won",rc);
    else if (rc == 'D')
      printf("Draw");
    else if (rc == 'N')
      printf("Game has not completed");
    else
      assert(0);
    printf("\n");
    //    string line;
    //    getline(cin,line);
  }
  return 0;
}
      
        
        
        
    
    
    
