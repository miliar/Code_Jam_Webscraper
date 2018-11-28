#include <stdio.h>

int S[101][101];
double WP[101];
double OWP[101];
double OOWP[101];
int N;

void getwp() {
  for (int i=0;i<N;++i) {
    int ops = 0;
    WP[i] = 0;
    for (int j=0;j<N;++j) {
      if (S[i][j] == -1) continue;
      ++ops;
      WP[i] += S[i][j];
    }
    WP[i] /= ops;
  }
}

void getowp() {
  for (int i=0;i<N;++i) {
    int ops = 0;
    OWP[i] = 0;
    for (int j=0;j<N;++j) {
      if (S[i][j] == -1) continue;
      ++ops;
      int cur = 0;
      int played = 0;
      for (int k=0;k<N;++k) {
	if (k == i) continue;
	if (S[j][k] != -1) {
	  cur += S[j][k];
	  ++played;
	}
      }
      OWP[i] += (double)cur/played;
    }
    OWP[i] /= ops;
  }
}

void getoowp() {
  for (int i=0;i<N;++i) {
    int ops = 0;
    OOWP[i] = 0;
    for (int j=0;j<N;++j) {
      if (S[i][j] == -1) continue;
      ++ops;
      OOWP[i] += OWP[j];
    }
    OOWP[i] /= ops;
  }
}

int main() {
  int T;
  scanf("%d", &T);
  for (int TT=1;TT<=T;++TT) {
    scanf("%d\n", &N);
    char str[120];
    for (int i=0;i<N;++i) {
      scanf("%s", str);
      for (int j=0;str[j];++j) {
	if (str[j] == '.') S[i][j] = -1;
	else S[i][j] = str[j] - '0';
      }
    }
    getwp();
    getowp();
    getoowp();
    //    for (int i=0;i<N;++i)
    //      printf("%lf %lf %lf\n", WP[i], OWP[i], OOWP[i]);
    printf("Case #%d:\n", TT);
    for (int i=0;i<N;++i)
      printf("%.8lf\n", .25*WP[i]+.5*OWP[i]+.25*OOWP[i]);
  }
  return 0;
}
