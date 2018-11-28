#include <vector>
#include <algorithm>
#include <iostream>
#include <cstring>

using namespace std;

void fill(int ma[400][400], int i, int j, int color)
{
  if (0 <= i && i < 400 && 0 <= j && j < 400) {
    if (ma[i][j] == 0 || ma[i][j] == color) {
      ma[i][j] = color + 4;
      fill(ma, i+1, j, color);
      fill(ma, i, j+1, color);
      fill(ma, i-1, j, color);
      fill(ma, i, j-1, color);
    }
  }
}

int main()
{
  int N;
  cin >> N;

  for (int cas = 1; cas <= N; cas++) {
    int L;
    cin >> L;
    string path;
    for (int j = 0; j < L; j++) {
      string s;
      int t;
      cin >> s;
      cin >> t;
      for (int k = 0; k < t; k++) {
        path += s;
      }
    }
    //cout << path << endl;
    
    int ma[400][400];

    memset(ma, 0, sizeof ma);
    int dir = 1;
    int x = 200;
    int y = 200;

    for (int i = 0; i < path.size(); i++) {
      char act = path[i];
      switch (act) {
      case 'F': {
        switch (dir) {
        case 0:
          ma[x][y] = 1;
          ma[x][y-1] = 2;
          x++;
          break;
        case 1:
          ma[x-1][y] = 1;
          ma[x][y] = 2;
          y++;
          break;
        case 2:
          ma[x-1][y-1] = 1;
          ma[x-1][y] = 2;
          x--;
          break;
        case 3:
          ma[x][y-1] = 1;
          ma[x-1][y-1] = 2;
          y--;
          break;
        }
        break;
      }
      case 'L':
        dir = (dir + 1) & 3;
        break;
      case 'R':
        dir = (dir - 1) & 3;
        break;
      }
    }
    for (int i = 0; i < 400; i++) {
      for (int j = 0; j < 400; j++) {
        if (ma[i][j] == 1) {
          fill(ma, i+1, j, 1);
          fill(ma, i, j+1, 1);
          fill(ma, i-1, j, 1);
          fill(ma, i, j-1, 1);
          break;
        }
      }
    }
    for (int i = 0; i < 400; i++) {
      for (int j = 0; j < 400; j++) {
        if (ma[i][j] == 2) {
          fill(ma, i+1, j, 2);
          fill(ma, i, j+1, 2);
          fill(ma, i-1, j, 2);
          fill(ma, i, j-1, 2);
          break;
        }
      }
    }

    /*
    for (int i = -20; i < 20; i++) {
      for (int j = -20; j < 20; j++) {
        cout << ma[200+i][200+j];
      }
      cout << endl;
    }*/

    int outer = ma[0][0];
    int inner = outer == 5 ? 6 : 5;
    for (int i = 0; i < 400; i++) {
      int j;
      for (j = 0; j < 400; j++) {
        if (ma[i][j] == inner) break;
      }

      while (j < 400) {
        for (; j < 400; j++) {
          if (ma[i][j] != inner) break;
        }
        int k;
        for (k = 0; j + k < 400; k++) {
          if (ma[i][j+k] == inner) break;
        }
        if (j + k < 400) {
          for (int l = 0; l < k; l++) {
            ma[i][j+l] = 3;
          }
        }
        j += k;
      }
    }

    for (int i = 0; i < 400; i++) {
      int j;
      for (j = 0; j < 400; j++) {
        if (ma[j][i] == inner) break;
      }

      while (j < 400) {
        for (; j < 400; j++) {
          if (ma[j][i] != inner) break;
        }
        int k;
        for (k = 0; j + k < 400; k++) {
          if (ma[j+k][i] == inner) break;
        }
        if (j + k < 400) {
          for (int l = 0; l < k; l++) {
            ma[j+l][i] = 3;
          }
        }
        j += k;
      }
    }

    int count = 0;
    for (int i = 0; i < 400; i++) {
      for (int j = 0; j < 400; j++) {
        if (ma[i][j] == 3) count++;
      }
    }

    /*
    for (int i = -20; i < 20; i++) {
      for (int j = -20; j < 20; j++) {
        cout << ma[200+i][200+j];
      }
      cout << endl;
    }*/
    
    cout << "Case #" << cas << ": ";
    cout << count << endl;
  }
  
  return 0;
}

