#include<cstdio>
#include<cstring>
#define infile "a.in"
#define outfile "a.out"
#define nMax 131

using namespace std;

char a[nMax][nMax];
char b[nMax][nMax];
bool vz[nMax][nMax];
int n, m;
bool ok;

void read() {
  scanf("%d %d\n", &n, &m);
  for(int i = 1; i <= n; ++i)
    scanf("%s\n", a[i] + 1);
}

void solve() {
  ok = true;

  for(int i = 1; i <= n; ++i)
    for(int j = 1; j <= m; ++j)
      b[i][j] = '.';

  for(int i = 1; i <= n; ++i)
    for(int j = 1; j <= m; ++j) {
      if(a[i][j] == '#' && !vz[i][j]) {
        if(i == n || j == m || vz[i][j+1] || a[i][j+1] != '#' || a[i+1][j] != '#' || a[i+1][j+1] != '#') ok = false;
        else {
          vz[i][j] = vz[i][j+1] = vz[i+1][j] = vz[i+1][j+1] = true;
          b[i][j] = '/', b[i][j+1] = '\\';
          b[i+1][j] = '\\', b[i+1][j+1] = '/';
        }
      }
    }
}

void write(int t) {
  printf("Case #%d:\n", t);
  if(ok == false) printf("Impossible\n");
  else
    for(int i = 1; i <= n; ++i)
      printf("%s\n", b[i] + 1);
}

void clear() {
  memset(a, 0, sizeof(a));
  memset(b, 0, sizeof(b));
  memset(vz, 0, sizeof(vz));
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
