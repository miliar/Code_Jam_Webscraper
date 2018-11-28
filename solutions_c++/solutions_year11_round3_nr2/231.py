#include<cstdio>
#include<vector>
#include<algorithm>
#define infile "b.in"
#define outfile "b.out"
#define ll long long

using namespace std;

vector <ll> v;
vector <ll> w;
vector <ll> z;
int l, n, m;
ll t;
ll s;

void read() {
  scanf("%d %lld %d %d\n", &l, &t, &n, &m);
  for(int i = 1; i <= m; ++i) {
    ll x;
    scanf("%lld", &x);
    w.push_back(x);
  }
}

void solve() {

  for(unsigned i = 0; i < w.size(); ++i)
    w[i] *= 2;

  for(int i = 0; i < n; ++i)
    v.push_back(w[i % w.size()]);

  for(unsigned i = 1; i < v.size(); ++i)
    v[i] += v[i-1];

  /*
  for(unsigned i = 0; i < v.size(); ++i)
    printf("%lld ", v[i]);
  printf("\n");
  */

  s = v.back();

  for(unsigned i = 0; i < v.size(); ++i)
    if(v[i] > t) {
      ll last = i > 0 ? v[i-1] : 0;
      if(last >= t) z.push_back(w[i % w.size()] / 2);
      else z.push_back((v[i] - t) / 2);
    }

  sort(z.begin(), z.end());
  reverse(z.begin(), z.end());

  /*
  for(unsigned i = 0; i < z.size(); ++i)
    printf("%lld ", z[i]);
  printf("\n");
  */

  for(unsigned i = 0; i < z.size() && (int)i < l; ++i)
    s -= z[i];
}

void write(int t) {
  printf("Case #%d: %lld\n", t, s);
}

void clear() {
  v.clear();
  w.clear();
  z.clear();
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
