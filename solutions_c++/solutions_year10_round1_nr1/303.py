
#include <stdio.h>
#include <iostream>

using namespace std;

char d[100][100];
char e[100][100];
int dx[4] = {1, 0, 1, 1};
int dy[4] = {0, 1, -1, 1};

  int n, m;
void Output() {
  for (int i = 0; i < n;++i) {
    for (int j = 0; j < n;++j) {
      cout << e[i][j] << ' ';
    }
    cout << endl;
  }
  cout << endl;
}

void process() { 
  cin >> n >> m;
  for (int i = 0; i < n; ++i) {
    cin >> d[i];
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      e[i][j] = d[n-j-1][i];
    }
  }

  for (int i = n-1; i >= 0; --i) {
    for (int j = 0; j < n; ++j) {
      if (e[i][j] == '.') {
        for (int k = i-1; k >= 0; --k) {
          if (e[k][j] != '.') {
            e[i][j] = e[k][j];
            e[k][j] = '.';
            break;
          }
        }
      }
    }
  }


  bool red, blue;
  red = blue = false;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if (e[i][j] != '.') {
        int cnt[4] = {0};
        for (int k = 0; k < m; ++k) {
          for (int l = 0; l < 4; ++l) {
            int ni = i + k*dx[l];
            int nj = j + k*dy[l];
            if (ni >= 0 && ni < n && nj >= 0 && nj < n && e[ni][nj] == e[i][j]) {
              cnt[l]++;
            }
          }
        }
        for (int k = 0; k < 4; ++k) {
          if (cnt[k] == m) {
            if (e[i][j] == 'R') {
              red = true;
            } else if (e[i][j] == 'B') {
              blue = true;
            }
          }
        }
      }
    }
  }
  if (red && blue) {
    printf ("Both\n");
  } else if (red) {
    printf ("Red\n");
  } else if (blue) {
    printf ("Blue\n");
  } else {
    printf ("Neither\n");
  }
}
int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    printf ("Case #%d: ", i+1);
    process();
  }
  return 0;
}
