#include <cstdio>
#include <vector>
#include <map>
using namespace std;

int N;
char A[110][110];
double WP[110], WPwi[110][110], OWP[110], OOWP[110];

int main() {
  int T;
  scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    scanf("%d", &N);
    for(int i = 0; i < N; i++)
      scanf("%s", A[i]);
    for(int i = 0; i < N; i++) {
      int won = 0, lost = 0;
      for(int j = 0; j < N; j++) {
        if(A[i][j] == '1') won++;
        if(A[i][j] == '0') lost++;
      }
      WP[i] = 1.0 * won / (won+lost);
      for(int j = 0; j < N; j++) {
        if(A[i][j] == '1') WPwi[i][j] = 1.0 * (won-1) / (won+lost-1);
        if(A[i][j] == '0') WPwi[i][j] = 1.0 * won / (won+lost-1);
      }
    }
    for(int i = 0; i < N; i++) {
      int num = 0;
      double now = 0;
      for(int j = 0; j < N; j++) if(A[i][j] != '.') {
        num++;
        now += WPwi[j][i];
      }
      OWP[i] = now / num;
    }
    for(int i = 0; i < N; i++) {
      int num = 0;
      double now = 0;
      for(int j = 0; j < N; j++) if(A[i][j] != '.') {
        num++;
        now += OWP[j];
      }
      OOWP[i] = now / num;
    }
    printf("Case #%d:\n", t);
    for(int i = 0; i < N; i++)
      printf("%.10lf\n", 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i]);
  }
  return 0;
}

