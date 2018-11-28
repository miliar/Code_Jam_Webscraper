#include<cstdio>
char m[4][5];
int main() {
  int n;scanf("%d", &n);
  for(int i=1;i<=n;i++) {
    bool draw=true;
    for(int j=0;j<4;j++)
      scanf("%s", m[j]);
    for(int j=0;j<4;j++) {
      char side; int c=0;
      if (m[j][0]=='.'||m[j][1]=='.') {
        continue;
      } else {
        if(m[j][0]=='T') side=m[j][1]; else side=m[j][0];
        c=1;
      }
      for(int k=1;k<4;k++) {
        if (m[j][k]=='T'||m[j][k]==side) {
          c++;
        } else {
          break;
        }
      }
      if (c==4) {
        printf("Case #%d: %c won\n", i, side);
        draw=false; break;
      }
    }
    if (!draw) continue;
    for(int j=0;j<4;j++) {
      char side; int c=0;
      if (m[0][j]=='.'||m[1][j]=='.') {
        continue;
      } else {
        if(m[0][j]=='T')side=m[1][j];else side=m[0][j];
        c=1;
      }
      for(int k=1;k<4;k++) {
        if (side==m[k][j]||m[k][j]=='T') {
          c++;
        } else break;
      }
      if (c==4) {
        printf("Case #%d: %c won\n", i, side);
        draw=false; break;
      }
    }
    if (!draw) continue;
    if(m[0][0]!='.'&&m[1][1]!='.'){
      char side;
      if(m[0][0]=='T') side=m[1][1]; else side=m[0][0];
      if(m[1][1]=='T'||side==m[1][1])
        if(m[2][2]=='T'||side==m[2][2])
          if(m[3][3]=='T'||side==m[3][3])
          { printf("Case #%d: %c won\n", i, side); draw=false; }
    }
    if (!draw) continue;
    if(m[0][3]!='.'&&m[1][2]!='.'){
      char side;
      if(m[0][3]=='T') side=m[1][2]; else side=m[0][3];
      if(m[1][2]=='T'||side==m[1][2])
        if(m[2][1]=='T'||side==m[2][1])
          if(m[3][0]=='T'||side==m[3][0])
          { printf("Case #%d: %c won\n", i, side); draw=false; }
    }
    if (!draw) continue;

    int cc=0;
    for(int j=0;j<4;j++)
      for(int k=0;k<4;k++)
        if(m[j][k]!='.') cc++;
    if (cc==16) {
      printf("Case #%d: Draw\n", i);
      continue;
    }

    printf("Case #%d: Game has not completed\n", i);
    
  }
  return 0;
}
