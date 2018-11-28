#include <cstdio>

char game[100][105];
int allGames[100];
int wonGames[100];
long double wp[100];
long double owp[100];
long double oowp[100];

void solve() {
  int n;
  
  scanf("%d\n", &n);
  for (int i=0; i<n; i++) {
    fgets(game[i], 105, stdin);
    allGames[i] = wonGames[i] = 0;
    for (int j=0; j<n; j++) {
      if (game[i][j] == '.') continue;
      allGames[i]++;
      if (game[i][j] == '1') wonGames[i]++;
    }
    wp[i] = 1.0L * wonGames[i] / allGames[i];
  }
  
  for (int i=0; i<n; i++) {
    int cnt = 0;
    owp[i] = 0;
    for (int j=0; j<n; j++) {
      if (j == i || game[i][j] == '.') continue;
      owp[i] += 1.0L * (wonGames[j] - ((game[j][i]=='1')?1:0)) / (allGames[j]-1);
      cnt++;
    } 
    owp[i] /= cnt;
  }
  
  for (int i=0; i<n; i++) {
    int cnt = 0;
    oowp[i] = 0;
    for (int j=0; j<n; j++) {
      if (j == i || game[i][j] == '.') continue;
      oowp[i] += owp[j];
      cnt++;
    }
    oowp[i] /= cnt;
  }
  
  for (int i=0; i<n; i++) {
    printf("%.12Lg\n", 0.25L * wp[i] + 0.50L * owp[i] + 0.25L * oowp[i]);
  }
  
}

int main() {
  int t;
  
  scanf("%d\n", &t);
  for (int i=1; i<=t; i++) {
    printf("Case #%d:\n", i);
    solve();
  }
  return 0;
}
