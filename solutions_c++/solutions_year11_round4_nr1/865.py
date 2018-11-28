#include<cstdio>
#include<vector>
#include<algorithm>
#define infile "a.in"
#define outfile "a.out"

using namespace std;

double res;

bool cmp(pair < pair <int, int>, int> a, pair < pair <int, int>, int> b) {
  return a.second < b.second;
}

void solve() {
  vector < pair < pair <int, int>, int > > v;
  int x, s, r, t, n;
  int last = 0;
  res = 0;

  scanf("%d %d %d %d %d\n", &x, &s, &r, &t, &n);
  for(int i = 1; i <= n; ++i) {
    int a, b, c;
    scanf("%d %d %d\n", &a, &b, &c);
    if(a != last) v.push_back(make_pair(make_pair(last, a), 0));
    v.push_back(make_pair(make_pair(a, b), c));
    last = b;
  }
  if(last != x) v.push_back(make_pair(make_pair(last, x), 0));

  sort(v.begin(), v.end(), cmp);

  double tt = t;
  for(unsigned i = 0; i < v.size(); ++i) {
    //printf("%d %d %d %lf\n", v[i].first.first, v[i].first.second, v[i].second, tt);
    double dd = v[i].first.second - v[i].first.first;
    double vv = v[i].second;
    if(tt >= (double)dd / (vv + r)) {
      tt -= (double)dd / (vv + r);
      res += (double)dd / (vv + r);
    } else {
      double ddd = (vv + r) * tt;
      //printf("ddd = %lf\n", ddd);
      res += tt, dd -= ddd;
      res += dd / (vv + s);
      tt = 0;
    }
  }
}

void write(int t) {
  printf("Case #%d: %.8lf\n", t, res);
}

int main() {
  freopen(infile, "r", stdin);
  freopen(outfile, "w", stdout);

  int t;
  scanf("%d\n", &t);
  for(int test = 1; test <= t; ++test) {
    solve();
    write(test);
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
