#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#define infile "b.in"
#define outfile "b.out"
#define sigma 131
#define nMax 1013

using namespace std;

bool a[sigma][sigma];
char b[sigma][sigma];
vector <char> v;
char w[nMax];
int n;

void init() {
  memset(a, 0, sizeof(a));
  memset(b, 0, sizeof(b));
  v.clear();
}

void read() {

  scanf("%d ", &n);
  for(int i = 1; i <= n; ++i) {
    char x, y, z;
    scanf("%c%c%c ", &x, &y, &z);
    b[x][y] = b[y][x] = z;
  }

  scanf("%d ", &n);
  for(int i = 1; i <= n; ++i) {
    char x, y;
    scanf("%c%c ", &x, &y);
    a[x][y] = a[y][x] = true;
  }

  scanf("%d ", &n);
  scanf("%s\n", w+1);
}

bool verif(char x) {
  for(unsigned i = 0; i < v.size(); ++i)
    if(a[v[i]][x])
      return true;
  return false;
}

void solve() {
  for(int i = 1; i <= n; ++i) {
    v.push_back(w[i]);
    if(v.size() > 1) {
      char x = v[v.size()-1];
      char y = v[v.size()-2];
      if(b[x][y]) {
        v.pop_back();
        v.pop_back();
        v.push_back(b[x][y]);
      }
      else if(verif(x))
        v.clear();
    }
  }
}

void write(int t) {
  printf("Case #%d: [", t);
  for(unsigned i = 0; i+1 < v.size(); ++i)
    printf("%c, ", v[i]);
  if(!v.empty()) printf("%c", v.back());
  printf("]\n");
}

int main() {
  freopen(infile, "r", stdin);
  freopen(outfile, "w", stdout);

  int t;
  scanf("%d\n", &t);
  for(int i = 1; i <= t; ++i) {
    init();
    read();
    solve();
    write(i);
  }

  fclose(stdin);
  fclose(stdout);
}
