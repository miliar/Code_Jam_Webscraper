# include <cstdio>
# include <vector>
# include <map>
# include <algorithm>

using namespace std;

const int maxn = 200;

map<int, int> a, b;
pair<int, int> la[maxn], lb[maxn];
int na, nb, t;

void Insert(map<int, int>&s, int k) {
  map<int, int>::iterator it = s.find(k);
  if (it == s.end()) s[k] = 1;
  else s[k]++;
}

void Remove(map<int, int>&s, int k) {
  map<int, int>::iterator it = s.find(k);
  if (it->second == 1) s.erase(k);
  else s[k]--;
}

void init() {
  scanf("%d%d%d", &t, &na, &nb);
  for (int i = 0; i < na; ++i) {
    int a, b, c, d;
    scanf(" %d:%d %d:%d", &a, &b, &c, &d);
    la[i] = make_pair(a * 60 + b, c * 60 + d + t);
  }
  for (int i = 0; i < nb; ++i) {
    int a, b, c, d;
    scanf(" %d:%d %d:%d", &a, &b, &c, &d);
    lb[i] = make_pair(a * 60 + b, c * 60 + d + t);
  }
  sort(la, la + na);
  sort(lb, lb + nb);
}

void solve() {
  int res_a = 0, res_b = 0, stay_a = 0, stay_b = 0;
  a.clear(); b.clear();
  for (int i = 0, j = 0; i < na || j < nb; ) 
    if (j == nb || (i < na && la[i].first < lb[j].first)) {
      //      while (!a.empty() && *a.begin() <= la[i].first) a.erase(*a.begin()), stay_a++;
      while (!a.empty() && (a.begin()->first) <= la[i].first) Remove(a, a.begin()->first), stay_a++;

      if (stay_a == 0) res_a++;
      else stay_a--;
      //      b.insert(la[i].second);
      Insert(b, la[i].second);
      i++;
    }
    else {
      //      while (!b.empty() && *b.begin() <= lb[j].first) b.erase(*b.begin()), stay_b++;
      while (!b.empty() && b.begin()->first <= lb[j].first) Remove(b, b.begin()->first), stay_b++;
      if (stay_b == 0) res_b++;
      else stay_b--;
      //      a.insert(lb[j].second);
      Insert(a, lb[j].second);
      j++;
    }

  printf("%d %d\n", res_a, res_b);
}

int main() {
  int tt, i;
  for (scanf("%d", &tt), i = 1; i <= tt; ++i) {
    printf("Case #%d: ", i);
    init();
    solve();
  }
}
