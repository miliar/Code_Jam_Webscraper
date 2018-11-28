#include <cstdio>
#include <cstring>

double wp[101], owp[101], oowp[101], rpi[101];
double win[101], wwin[101][101], played[101];
char grid[101][101];

int main() {
  int case_no, n, t;

  scanf("%d", &t);
  for (case_no = 1; case_no <= t; case_no++) {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      getchar();
      for (int j = 0; j < n; j++)
        grid[i][j] = getchar();
    }
    
    // calc WP
    for (int i = 0; i < n; i++) {
      win[i] = 0;
      played[i] = 0;
      for (int j = 0; j < n; j++)
        if (grid[i][j] == '1') {
          win[i] += 1.00;
          played[i] += 1.00;
        }
        else if (grid[i][j] == '0')
          played[i] += 1.00;
      wp[i] = win[i] / played[i];
    }
    
    // calc OWP
    for (int i = 0; i < n; i++) {
      double sum = 0;
      double count = 0;
      for (int j = 0; j < n; j++)
        if (grid[j][i] == '1') {
          count += 1.00;
          wwin[i][j] = win[j] - 1.00;
        }
        else if (grid[j][i] == '0') {
          count += 1.00;
          wwin[i][j] = win[j];
        }
        else if (grid[j][i] == '.')
          wwin[i][j] = 0;
      for (int j = 0; j < n; j++)
        if (grid[i][j] != '.')
          sum += (wwin[i][j] + 0.00) / (played[j] - 1.00);
      owp[i] = sum / count;
    }
    
    // calc OOWP
    for (int i = 0; i < n; i++) {
      double sum = 0;
      double count = 0;
      for (int j = 0; j < n; j++)
        if (grid[i][j] != '.') {
          sum += owp[j];
          count += 1.00;
        }
      oowp[i] = sum / count;
    }
    
    
    // calc RPI
    for (int i = 0; i < n; i++)
      rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
    
    printf("Case #%d:\n", case_no);
    for (int i = 0; i < n; i++)
      printf("%.12f\n", rpi[i]);
  }

  return 0;
}
