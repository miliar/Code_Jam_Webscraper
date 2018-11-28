#include<cstdio>
#include<algorithm>
#define infile "a.in"
#define outfile "a.out"
#define nMax 131

using namespace std;

pair <int, int> v[nMax];
pair <int, int> x[2];
int n;

void read() {
  scanf("%d ", &n);
  for(int i = 1; i <= n; ++i) {
    char t; int x;
    scanf("%c %d ", &t, &x);
    //printf("%c %d\n", t, x);
    v[i] = make_pair(t == 'B' ? 0 : 1, x);
  }
}

void solve() {
  x[0].first = 0, x[0].second = 1;
  x[1].first = 0, x[1].second = 1;

  for(int i = 1; i <= n; ++i) {
    //printf("%d %d\n", v[i].first, v[i].second);
    int t = v[i].first;
    if(i == 1 || v[i].first == v[i-1].first)
      x[t].first = x[t].first + abs(x[t].second - v[i].second) + 1, x[t].second = v[i].second;
    else x[t].first = max(x[t].first + abs(x[t].second - v[i].second), x[1-t].first) + 1, x[t].second = v[i].second;
  }
}

void write(int t) {
  printf("Case #%d: %d\n", t, max(x[0].first, x[1].first));
}

int main() {
  freopen(infile, "r", stdin);
  freopen(outfile, "w", stdout);

  int t;
  scanf("%d", &t);
  for(int i = 1; i <= t; ++i) {
    read();
    solve();
    write(i);
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
