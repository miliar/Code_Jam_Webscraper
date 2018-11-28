#include <cstdio>
#define R 4

using namespace std;

int main() {
  int n;
  scanf("%d\n", &n);
  char p[4][6];
  for (int i=1; i<=n; ++i) {
    scanf("%s\n", p[0]);
    scanf("%s\n", p[1]);
    scanf("%s\n", p[2]);
    scanf("%s\n\n", p[3]);
    //printf("%s\n", p[0]);
    
    bool draw = false, end=false;
    int xs, os;
    for (int j=0; j<R; ++j) {
      xs=0;
      os=0;
      for (int k=0; k<R; ++k) {
        if (p[j][k]=='.') {
          draw = true;
          break;
        }
        else if (p[j][k]=='X') {
          ++xs;
        }
        else if (p[j][k]=='O') {
          ++os;
        }
        else {
          ++xs;
          ++os;
        }
      }
      if (xs==4) {
        printf("Case #%d: X won\n", i);
        end=true;
        break;
      }
      else if (os==4) {
        printf("Case #%d: O won\n", i);
        end=true;
        break;
      }
    }
    
    if (end) continue;
    for (int j=0; j<R; ++j) {
      xs=0;
      os=0;
      for (int k=0; k<R; ++k) {
        if (p[k][j]=='.') {
          draw = true;
          break;
        }
        else if (p[k][j]=='X') {
          ++xs;
        }
        else if (p[k][j]=='O') {
          ++os;
        }
        else {
          ++xs;
          ++os;
        }
      }
      if (xs==4) {
        printf("Case #%d: X won\n", i);
        end=true;
        break;
      }
      else if (os==4) {
        printf("Case #%d: O won\n", i);
        end=true;
        break;
      }
    }
    
    if (end) continue;
    xs=0;
    os=0;
    for (int j=0; j<R; ++j) {
      if (p[j][j]=='.') {
        draw = true;
        break;
      }
      else if (p[j][j]=='X') {
        ++xs;
      }
      else if (p[j][j]=='O') {
        ++os;
      }
      else {
        ++xs;
        ++os;
      }
    }
    if (xs==4) {
      printf("Case #%d: X won\n", i);
      end=true;
    }
    else if (os==4) {
      printf("Case #%d: O won\n", i);
      end=true;
    }
    
    if (end) continue;
    xs=0;
    os=0;
    for (int j=0; j<R; ++j) {
      //printf("%d %c\n", p[j][R-1-j], p[j][R-1-j]);
      if (p[j][R-1-j]=='.') {
        draw = true;
        break;
      }
      else if (p[j][R-1-j]=='X') {
        ++xs;
      }
      else if (p[j][R-1-j]=='O') {
        ++os;
      }
      else {
        ++xs;
        ++os;
      }
    }
    //printf("%d %d\n", xs, os);
    if (xs==4) {
      printf("Case #%d: X won\n", i);
      end=true;
    }
    else if (os==4) {
      printf("Case #%d: O won\n", i);
      end=true;
    }
    if (end) continue;
    
    if (draw) {
      printf("Case #%d: Game has not completed\n", i);
    }
    else {
      printf("Case #%d: Draw\n", i);
    }
  }
  
}