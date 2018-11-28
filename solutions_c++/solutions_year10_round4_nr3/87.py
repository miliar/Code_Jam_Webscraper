#include <iostream>
using namespace std;

int C,R;
int grid[101][101];
int t;

int main(int argc, char *argv[]) {
  int x1, y1, x2, y2;
  bool dead;
  cin >> C >> ws;
  for(int c=1; c<=C; c++) {
    for(int i=0; i<=100; i++) {
      for(int j=0; j<=100; j++) {
        grid[i][j] = 0;
      }
    }
    cin >> R >> ws;
    for(int r=0; r<R; r++) {
      cin >> x1 >> y1 >> x2 >> y2 >> ws;
      for(int i=x1; i<=x2; i++) {
        for(int j=y1; j<=y2; j++) {
          grid[i][j] = 1;
        }
      }
    }
    
    t = 0;
    while(true) {
      dead = true;
      for(int i=0; i<=100; i++) {
        for(int j=0; j<=100; j++) {
          if(grid[i][j]) {
            dead = false;
          }
        }
      }
      if(dead) break;
      
      for(int i=0; i<=100; i++) {
        for(int j=0; j<=100; j++) {
          if(grid[i][j] == 0 && grid[i-1][j] == 1 && grid[i][j-1] == 1) grid[i][j] = -1;
        }
      }
      for(int i=0; i<=100; i++) {
        for(int j=0; j<=100; j++) {
          if(grid[i][j] == 1 && grid[i-1][j] <= 0 && grid[i][j-1] <= 0) grid[i][j] = 2;
        }
      }
      for(int i=0; i<=100; i++) {
        for(int j=0; j<=100; j++) {
          if(grid[i][j] == -1) grid[i][j] = 1;
          if(grid[i][j] == 2) grid[i][j] = 0;
        }
      }
      t++;

    }
    
    cout << "Case #" << c << ": " << t << endl;

  }
  
  return 0;
}
