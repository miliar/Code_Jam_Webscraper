#include <cstdio>
#include <iostream>

using namespace std;

int main() {
  int C, R;

  cin >> C;

for (int case_count = 1; case_count <= C; case_count++) {
  cin >> R;

  int x1[R], x2[R] ,y1[R] ,y2[R];

  int max_x = 0, max_y = 0;
  for (int i = 0; i < R; i++) {
    cin >> x1[i];
    cin >> y1[i];
    cin >> x2[i];
    cin >> y2[i];
    if (x2[i] > max_x)
      max_x = x2[i];
    if (y2[i] > max_y)
      max_y = y2[i];
  }

  bool grids[max_x * 2][max_y * 2];
  bool grids2[max_x * 2][max_y * 2];

  for (int x = 0; x < max_x * 2; x++) {
    for (int y = 0; y < max_y * 2; y++) {
      grids[x][y] = false;
      grids2[x][y] = false;
    }
  }


  for (int i = 0; i < R; i++) {
    for (int x = x1[i] - 1; x <= x2[i] - 1; x++) {
      for (int y = y1[i] - 1; y <= y2[i] - 1; y++) {
        grids[x][y] = true;
      }
    }

  }
       /* debug
        for (int dy = 0; dy < max_y * 2; dy++) {
          for (int dx = 0; dx < max_x * 2; dx++) {
            if (grids[dx][dy] == true)
              cout << "1 ";
            else
              cout << "0 ";
          }
          cout << endl;
        }
        cout << endl;
         debug */



  long long seconds_count = 0;

  while (++seconds_count) {
    bool is_die = true;


    if (seconds_count % 2 == 1) {

      for (int x = 0; x < max_x * 2; x++) {
        for (int y = 0; y < max_x * 2; y++) {
          if (grids[x][y] == true
              && (x - 1 < 0 || grids[x-1][y] == false)
              && (y - 1 < 0 || grids[x][y-1] == false)) {
            grids2[x][y] = false;
          } else if (grids[x][y] == false
              && (x - 1 >= 0 && grids[x-1][y] == true)
              && (y - 1 >= 0 && grids[x][y-1] == true)) {
            grids2[x][y] = true;
            is_die = false;
          } else {

            grids2[x][y] = grids[x][y];
            if (grids2[x][y] == true)
              is_die = false;
          }
        }
     }

       /* debug 
        for (int dy = 0; dy < max_y * 2; dy++) {
          for (int dx = 0; dx < max_x * 2; dx++) {
            if (grids2[dx][dy] == true)
              cout << "1 ";
            else
              cout << "0 ";
          }
          cout << endl;
        }
        cout << endl;
         debug */


    } else {

      for (int x = 0; x < max_x * 2; x++) {
        for (int y = 0; y < max_x * 2; y++) {
          if (grids2[x][y] == true
              && (x - 1 < 0 || grids2[x-1][y] == false)
              && (y - 1 < 0 || grids2[x][y-1] == false)) {
            grids[x][y] = false;
          } else if (grids2[x][y] == false
              && (x - 1 >= 0 && grids2[x-1][y] == true)
              && (y - 1 >= 0 && grids2[x][y-1] == true)) {
            grids[x][y] = true;
            is_die = false;
          } else {
            grids[x][y] = grids2[x][y];
            if (grids[x][y] == true)
              is_die = false;
          }
        }
      }
      /* debug 
        for (int dy = 0; dy < max_y * 2; dy++) {
          for (int dx = 0; dx < max_x * 2; dx++) {
            if (grids[dx][dy] == true)
              cout << "1 ";
            else
              cout << "0 ";
          }
          cout << endl;
        }
        cout << endl;
         debug */


    }


    if (is_die)
      break;
  }
  cout << "Case #" << case_count << ": " << seconds_count << endl;
}

  return 0;
}
