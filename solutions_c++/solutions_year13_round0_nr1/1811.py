#include <stdio.h>
#include <string.h>

char S[10][10];

bool check(char x) {
  for(int i=0;i<4;++i) {
    int ct = 0;
    for(int j=0;j<4;++j)
      if(S[i][j] == x || S[i][j] == 'T')
        ++ct;
    if(ct >= 4) return true;
    ct = 0;
    for(int j=0;j<4;++j)
      if(S[j][i] == x || S[j][i] == 'T')
        ++ct;
    if(ct >= 4) return true;
  }

  int ct = 0;
  for(int i=0;i<4;++i)
    if(S[i][i] == x || S[i][i] == 'T')
      ++ct;
  if(ct >= 4) return true;
  ct = 0;
  for(int i=0;i<4;++i)
    if(S[i][3-i] == x || S[i][3-i] == 'T')
      ++ct;
  if(ct >= 4) return true;
  return false;
}

bool fill() {
  for(int i=0;i<4;++i)
    for(int j=0;j<4;++j)
      if(S[i][j] == '.')
        return false;
  return true;
}

int main() {
  int t, kas=0;
  int winner;

  scanf("%d",&t);
  while(t--) {
    for(int i=0;i<4;++i)
      scanf("%s", S[i]);
    winner = -1;
    if( check('X') )
      winner = 0;
    else if( check('O') )
      winner = 1;
    else if( fill() )
      winner = 2;
    
    if(winner == 0)
      printf("Case #%d: X won\n", ++kas);
    else if(winner == 1)
      printf("Case #%d: O won\n", ++kas);
    else if(winner == 2)
      printf("Case #%d: Draw\n", ++kas);
    else
      printf("Case #%d: Game has not completed\n", ++kas);
  }

  return 0;
}

