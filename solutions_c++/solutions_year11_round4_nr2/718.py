#include<cstdio>
#include<algorithm>
#define infile "b.in"
#define outfile "b.out"
#define nMax 513
#define ll long long

using namespace std;

char h[nMax][nMax];
int n, m, d;
int res;

void read() {
  scanf("%d %d %d\n", &n, &m, &d);
  for(int i = 1; i <= n; ++i)
    scanf("%s\n", h[i] + 1);
}

bool valid(int x, int y, int k) {
  //printf("valid(%d %d %d) = ", x, y, k);
  ll sumX = 0, sumY = 0;
  ll sum = 0;
  for(int i = 1; i <= k; ++i)
    for(int j = 1; j <= k; ++j) {
      if(i == 1 && (j == 1 || j == k)) continue;
      if(i == k && (j == 1 || j == k)) continue;
      sumX += i*(d + h[x+i-1][y+j-1] - '0');
      sumY += j*(d + h[x+i-1][y+j-1] - '0');
      sum += d + h[x+i-1][y+j-1] - '0';
    }
  //printf("%lld %lld %lld :::: %Lf %Lf :: %lf\n", sumX, sumY, sum, (long double)sumX/sum, (long double)sumY/sum, (double)k/2);
  if((long double)sumX / sum == ((long double)k+1)/2 && (long double)sumY / sum == ((long double)k+1)/2) return true;
  return false;
}

void solve() {
  res = 0;
  for(int i = 1; i <= n; ++i)
    for(int j = 1; j <= m; ++j)
      for(int k = max(res, 3); i + k - 1 <= n && j + k - 1 <= m; ++k)
        if(valid(i, j, k))
          res = max(res, k);
}

void write(int t) {
  printf("Case #%d: ", t);
  if(res != 0) printf("%d", res);
  else printf("IMPOSSIBLE");
  printf("\n");
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
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
