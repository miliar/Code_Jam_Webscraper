#include<cstdio>
#include<cstring>
#define infile "a.in"
#define outfile "a.out"
#define nMax 131

using namespace std;

char ad[nMax][nMax];
double wp[nMax];
double owp[nMax];
double oowp[nMax];
double rpi[nMax];
int n;

void read() {
  scanf("%d\n", &n);
  for(int i = 1; i <= n; ++i)
    scanf("%s\n", ad[i] + 1);
}

double getWp(int i, int y) {
  int w = 0, l = 0;
  for(int j = 1; j <= n; ++j)
    if(j != y && i != j) {
      if(ad[i][j] == '1') w++;
      else if(ad[i][j] == '0') l++;
    }
  return (double)w / (w + l);
}

void solve() {

  for(int i = 1; i <= n; ++i) {
    wp[i] = getWp(i, 0);
  }

  for(int i = 1; i <= n; ++i) {
    double s = 0;
    int no = 0;
    for(int j = 1; j <= n; ++j)
      if(i != j && ad[i][j] != '.')
        s += getWp(j, i), no++;
    owp[i] = s / no;
  }

  for(int i = 1; i <= n; ++i) {
    double s = 0;
    int no = 0;
    for(int j = 1; j <= n; ++j)
      if(i != j && ad[i][j] != '.')
        s += owp[j], no++;
    oowp[i] = s / no;
  }

  for(int i = 1; i <= n; ++i)
    rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
}

void write(int t) {
  printf("Case #%d:\n", t);
  for(int i = 1; i <= n; ++i)
    printf("%.8lf\n", rpi[i]);
}

void clear() {
  memset(ad, 0, sizeof(ad));
}

int main() {
  freopen(infile, "r", stdin);
  freopen(outfile, "w", stdout);

  int t;
  scanf("%d\n", &t);
  for(int test = 1; test <= t; ++test) {
    read();
    solve();
    write(test);
    clear();
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
