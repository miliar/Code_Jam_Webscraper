#include<cstdio>
#include<vector>
#include<algorithm>
#define infile "c.in"
#define outfile "c.out"
#define ll long long

using namespace std;

vector <ll> v;
ll l, h, sol;
int n;
bool ok;

void read() {
  scanf("%d %lld %lld\n", &n, &l, &h);
  for(int i = 1; i <= n; ++i) {
    ll x;
    scanf("%lld", &x);
    v.push_back(x);
  }
}

bool valid(ll x) {
  for(unsigned i = 0; i < v.size(); ++i)
    if(v[i] != 1 && x != 1 && max(v[i], x) % min(v[i], x) != 0)
      return false;
  return true;
}

void solve() {
  ok = false;

  for(ll i = l; i <= h; ++i)
    if(valid(i)) {
      ok = true, sol = i;
      break;
    }
}

void write(int t) {
  printf("Case #%d: ", t);
  if(ok) printf("%lld\n", sol);
  else printf("NO\n");
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
