#include <algorithm>
#include <cassert>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
#define For(i, x) for (int i=0; i<(int)(x); i++)
#define prn(a) cout << (a) << '\n'

typedef long long ll;

struct Group {
  int no, size;
};

ll calc(int times, int cap, int n, Group gs[]) {
  For(i, n) assert(gs[i].size <= cap);

  // int memo[1000] = {};
  vector<ll> psum;
  for (int i = 1; i <= times; i++) {
    /*
    if (memo[gs[0].no]++) {
      ll euro = psum.back();
      ll rest = times - i + 1;

      euro += rest / psum.size() * psum.back();
      int m = rest % psum.size();
      if (m > 0)
        euro += psum[m-1];
      return euro;
    }*/

    int p = 0, size = 0;
    while (p < n && size + gs[p].size <= cap)
      size += gs[p++].size;

    if (psum.empty())
      psum.push_back(size);
    else
      psum.push_back(size + psum.back());
    rotate(gs, gs+p, gs+n);
  }

  return psum.back();
}

int main() {
  int ncases;
  scanf("%d", &ncases);

  Group gs[1000];
  For(cc, ncases) {
    int times, cap, n;
    scanf("%d %d %d", &times, &cap, &n);
    For(i, n) {
      gs[i].no = i;
      scanf("%d", &gs[i].size);
    }

    printf("Case #%d: ", cc+1);
    prn(calc(times, cap, n, gs));
  }
}
