#include <cstdio>

using namespace std;

char grid[101][101];
int wins[101], losses[101];
double wp[101], owp[101], oowp[101], rpi[101];

int main() {
  int T; scanf("%d", &T);
  for(int t=1; t<=T; ++t) {
    int n; scanf("%d", &n);
    for(int i=0; i<n; ++i) {
      scanf(" %s", grid[i]);
    }
    for(int i=0; i<n; ++i) {
      wins[i] = losses[i] = 0;
      for(int j=0; j<n; ++j) {
	if (grid[i][j] == '1') ++wins[i];
	else if (grid[i][j] == '0') ++losses[i];
      }
      wp[i] = wins[i]/(wins[i] + losses[i] + 0.);
    }
    for(int i=0; i<n; ++i) {
      owp[i] = 0;
      for(int j=0; j<n; ++j) {
	if (grid[i][j] == '1') owp[i] += wins[j]/(wins[j]+losses[j]-1.);
	else if (grid[i][j] == '0') owp[i] += (wins[j]-1)/(wins[j]+losses[j]-1.);
      }
      owp[i] /= wins[i]+losses[i];
    }
    for(int i=0; i<n; ++i) {
      oowp[i] = 0;
      for(int j=0; j<n; ++j) {
	if (grid[i][j] != '.') oowp[i] += owp[j];
      }
      oowp[i] /= wins[i]+losses[i];
      rpi[i] = .25*wp[i] + .5*owp[i] + .25*oowp[i];
    }
    printf("Case #%d:\n", t);
    for(int i=0; i<n; ++i) {
      printf("%lf\n", rpi[i]);
    }
  }
}
