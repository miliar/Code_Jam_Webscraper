#include <stdio.h>
#define FOR(q,n) for(int q=0; q<n; q++)

#define MAX 110
char table[MAX][MAX];
int n;
double wp[MAX][MAX];
double owp[MAX];

void init() {
  scanf("%d", &n);
  FOR(q, n) {
    scanf("%s", table[q]);
  }
}

double get_wp(int team, int discard) {
 int cnt = 0;
 int positive = 0;
 FOR(q, n) {
  if ((table[team][q] != '.') &&
      (q != discard)) {
    cnt++;
    positive += table[team][q] == '1';
  }
 }
 return (double) positive / cnt;
}

double get_owp(int team) {
  int cnt = 0;
  double sum = 0;
  FOR(q, n) {
    if (table[team][q] != '.') {
      cnt++;
 //     printf("wp %d %d %lf\n", q, team, wp[q][team]);
      sum+=wp[q][team];
    }
  }
 // printf("owp %d is %lf/%d\n", team, sum, cnt);
  return sum / cnt;
}

double get_oowp(int team) {
  int cnt = 0;
  double sum = 0;
  FOR(q, n) {
    if (table[team][q] != '.') {
      cnt++;
      sum+=owp[q];
    }
  }
  return sum / cnt;
}

void solve() {
  FOR(q, n)
    FOR(w, n)
      wp[q][w] = get_wp(q, w);
  FOR(q, n)
    owp[q] = get_owp(q);
  FOR(q, n) {
    double result = 0.25 * get_wp(q, -1)
      + 0.5 * owp[q] + 0.25 * get_oowp(q);
    printf("%lf\n", result);


  }
}

int main() {
  int t;
  scanf("%d", &t);
  FOR(q, t) {
    printf("Case #%d:\n", q+1);
    init();
    solve();

  }

}
