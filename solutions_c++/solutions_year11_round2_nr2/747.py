#include<cstdio>
#include<vector>
#include<algorithm>
#define infile "b.in"
#define outfile "b.out"
#define sMax 1000013
#define eps 0.0000001
#define ll long long

using namespace std;

vector < pair <int, int> > v;
int n, d;
double s;

void read() {
  scanf("%d %d\n", &n, &d);
  for(int i = 1; i <= n; ++i) {
    int x, y;
    scanf("%d %d\n", &x, &y);
    v.push_back(make_pair(x, y));
  }
}

bool valid(double t) {
  double left = (double)d * sMax * (-1);
  for(unsigned i = 0; i < v.size(); ++i) {
    ll dist = d * (v[i].second - 1);
    double le = max(left, v[i].first - t);
    double ri = le + dist;
    //printf("%d %lf %lf\n", i, le, ri);
    if(ri - v[i].first > t) return false;
    left = ri + d;
  }
  return true;
}

void solve() {

  sort(v.begin(), v.end());

  double le = 0, ri = (double)d * sMax, mi;
  while(ri - le >= eps) {
    mi = (le+ri) / 2;
    //printf("%lf %d\n", mi, valid(mi));
    if(valid(mi)) ri = mi - eps, s = mi;
    else le = mi + eps;
  }
}

void write(int t) {
  printf("Case #%d: %lf\n", t, s);
}

void clear() {
  v.clear();
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
