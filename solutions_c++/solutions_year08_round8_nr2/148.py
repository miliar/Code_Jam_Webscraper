#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

typedef long long int64;
typedef double real;

#define maxn (1 << 9)
#define maxs (1 << 11)

#define inf 0x3f3f3f3f
#define pi (2.0 * acos(0.0))

std::map< std::string, int> cnum;

int get_num(const std::string& s) {
  if(cnum.find(s) == cnum.end()) {
    int nx = cnum.size();
    return cnum[s] = nx;
  }
  return cnum[s];
}

std::vector<int> l[maxn], r[maxn];

struct ln {
  int l, r;
  ln(int _l, int _r) : l(_l), r(_r) { }

  bool operator < (const ln& rhs) const {
    if(r != rhs.r) return r < rhs.r;
    return l < rhs.l;
  }
};

char buf[1 << 10];

// std::set<ln> lns;

// void process(int l, int r) {
//   std::set<ln>::iterator it;
//   while((it = lns.find(ln(l, r))) != lns.end()) {
//     ln cur = *it;
//     lns.erase(it);
//     if(cur.l < l)
//       lns.insert(ln(cur.l, l-1));
//     if(cur.r > r)
//       lns.insert(ln(r+1, cur.r));
//   }
// }

int coord[maxs];

struct rmq_t {
  int mas[maxs*2];

  void clear() {
    memset(mas, 0x3f, sizeof(mas));
  }

  void set(int ind, int val) {
    ind += maxs;
    mas[ind] = val;
    for(ind >>= 1; ind > 0; ind >>= 1)
      mas[ind] = std::min(mas[(ind << 1)], mas[(ind << 1) + 1]);
  }

  int find(int l, int r) {
    //fprintf(stderr, "%d, %d\n", l, r);
    //assert(l <= r);
    if(l < 0) return 0;
    if(l > r) return inf;
    l += maxs; r += maxs;
    int ans = std::min(mas[l], mas[r]);
    while(r - l > 1) {
      if((l&1) == 0) ans = std::min(ans, mas[l+1]);
      if((r&1) == 1) ans = std::min(ans, mas[r-1]);
      l >>= 1; r >>= 1;
    }
    return ans;
  }
} rmq;

int main() {
  int t, tc;
  scanf("%d", &tc);
  for(t = 1; t <= tc; t++) {
    printf("Case #%d:", t);
    cnum.clear();
    int i, j, k, n, u, v;
    for(i = 0; i < maxn; i++) {
      l[i].clear(); r[i].clear();
    }

    scanf("%d", &n);
    int cc = 0;
    for(i = 0; i < n; i++) {
      scanf(" %s %d %d", buf, &u, &v);
      int nm = get_num(buf);
      l[nm].push_back(u);
      r[nm].push_back(v);
      if(u > 1) coord[cc++] = u-1;
      coord[cc++] = u;
      if(u < 10000) coord[cc++] = u+1;

      if(v > 1) coord[cc++] = v-1;
      coord[cc++] = v;
      if(v < 10000) coord[cc++] = v+1;
    }
    coord[cc++] = 1;
    coord[cc++] = 10000;
    std::sort(coord, coord+cc);

    cc = std::unique(coord, coord+cc) - coord;
    fprintf(stderr, "\n");
    for(i = 0; i < cc; i++) fprintf(stderr, "%d ", coord[i]);
    fprintf(stderr, "\n");

    for(i = 0; i < cnum.size(); i++, fprintf(stderr, "\n"))
      for(j = 0; j < l[i].size(); j++)
	fprintf(stderr, "!%d %d\n", l[i][j], r[i][j]);
    for(i = 0; i < cnum.size(); i++) {
      for(j = 0; j < l[i].size(); j++) {
	for(k = 0; k < cc; k++)
	  if(coord[k] == l[i][j]) break;
	//	assert(k < cc);
	l[i][j] = k;
      }
      for(j = 0; j < r[i].size(); j++) {
	for(k = 0; k < cc; k++)
	  if(coord[k] == r[i][j]) break;
	//	assert(k < cc);
	r[i][j] = k;
      }
    }
    for(i = 0; i < cnum.size(); i++, fprintf(stderr, "\n"))
      for(j = 0; j < l[i].size(); j++)
	fprintf(stderr, "!%d %d\n", l[i][j], r[i][j]);

    int bans = inf;
    fprintf(stderr, "!@!!!!%d\n", cc);
    for(i = 0; i < cnum.size(); i++)
      for(j = i; j < cnum.size(); j++)
	for(k = j; k < cnum.size(); k++) {
	  rmq.clear();
	  std::vector<ln> bugoga;
	  for(u = 0; u < l[i].size(); u++)
	    bugoga.push_back(ln(l[i][u], r[i][u]));


	  for(u = 0; u < l[j].size(); u++)
	    bugoga.push_back(ln(l[j][u], r[j][u]));

	  for(u = 0; u < l[k].size(); u++)
	    bugoga.push_back(ln(l[k][u], r[k][u]));

	  std::sort(bugoga.begin(), bugoga.end());

	  for(u = 0; u < bugoga.size(); u++) {
	    fprintf(stderr, "!! [%d, %d]\n", bugoga[u].l, bugoga[u].r);
	    int gy = rmq.find(bugoga[u].l-1, bugoga[u].r-1) + 1;
	    int cur = rmq.find(bugoga[u].r, bugoga[u].r);
	    if(gy < cur) rmq.set(bugoga[u].r, gy);
	  }
	  int ans = rmq.find(cc-1, cc-1);
	  fprintf(stderr, "%d\n\n", ans);
	  if(ans < bans) bans = ans;
	}
	  if(bans < inf) printf(" %d\n", bans);
	  else puts(" IMPOSSIBLE");
  }
  return 0;
}
