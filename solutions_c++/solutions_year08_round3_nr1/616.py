#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <set>
#include <sstream>
#include <climits>
#include <functional>
using namespace std;
typedef vector<int> vi;
typedef long long li;
typedef pair<int, int> pi;
#define all(c) c.begin(), c.end()
#define fr(i, n) for(i = 0; i < n; ++i)
#define pb push_back
#define mp make_pair
#define INT 2147483647
#define X first
#define Y second




int main() {
    freopen("d:\\A-small-attempt0.in", "r", stdin);
   freopen("d:\\a-small.out", "w", stdout);

     int p, l, i, j, k, t, T, n;
     scanf("%d", &T);
     for (t = 1; t <= T; ++t) {
          scanf("%d %d %d", &p, &k, &l);
          vi em(l);
          fr(i, l) scanf("%d", &em[i]);
          sort(all(em), greater <int> ());
          int col = 1, lim = k;
          li res = 0;
          fr(i, em.size()) {
               if (i == lim) {
                    lim += k;
                    col++;
               }
               res += (li) col * em[i];
          }
          printf("Case #%d: %lld\n", t, res);
	 }     
	 return 0;
}
