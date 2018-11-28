#include <cstdio>

char data[4][4];

bool is(int x, int y, char z) {
  return data[x][y]=='T' || data[x][y]==z;
}

bool checkY(int y, char z) {
  for (int x=0; x<4; ++x) {
    if (!is(x,y,z)) return false;
  }
  return true;
}

bool checkX(int x, char z) {
  for (int y=0; y<4; ++y) {
    if (!is(x,y,z)) return false;
  }
  return true;
}

bool check(char z) {
  for (int y=0; y<4; ++y) {
    if (checkY(y,z)) return true;
  }
  for (int x=0; x<4; ++x) {
    if (checkX(x,z)) return true;
  }
  return (is(0,0,z) && is(1,1,z) && is(2,2,z) && is(3,3,z))
      || (is(0,3,z) && is(1,2,z) && is(2,1,z) && is(3,0,z));
}

int main() {
  int N; scanf("%d\n",&N);
  for (int IN=1; IN<=N; ++IN) {
    
    bool completed = true;
    for (int y=0; y<4; ++y) {
      for (int x=0; x<4; ++x) {
        data[x][y] = getchar();
        if (data[x][y] == '.') {
          completed = false;
        }
      }
      getchar();
    }
    getchar();
    
    bool isX = check('X');
    bool isO = check('O');
    const char* msg = "Game has not completed";
    if (isX && isO) {
      msg = "Draw";
    } else if (isX) {
      msg = "X won";
    } else if (isO) {
      msg = "O won";
    } else if (completed) {
      msg = "Draw";
    }
    printf("Case #%d: %s\n", IN, msg);
  }
}
