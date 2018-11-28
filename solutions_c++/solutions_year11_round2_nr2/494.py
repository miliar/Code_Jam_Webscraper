#include <algorithm>
#include <cassert>
#include <string>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cctype>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <list>
#include <functional>
#include <numeric>
#include <bitset>
#include <ext/hash_set>
#include <ext/hash_map>
#include <stdexcept>
using namespace std;

const int maxn = 256;
typedef long long ll;
ll pos[maxn], num[maxn];

int main() {
  int cases;
  scanf("%i", &cases);
  for (int numcase = 1; numcase <= cases; ++numcase) {
    printf("Case #%i: ", numcase);
    ll n, mindist;
    scanf("%lli%lli", &n, &mindist);
    for (int i = 0; i < n; ++i)
      scanf("%lli%lli", &pos[i], &num[i]);

    vector<ll> x;
    for (int i = 0; i < n; ++i) 
      for (int j = 0; j < num[i]; ++j)
        x.push_back(pos[i]);
    int total = x.size();

    FILE *warra = fopen("warra", "w");
    fprintf(warra, "min: t;\n");

    for (ll i = 0; i < total; ++i) {
      fprintf(warra, "y_%lli - %lli <= t;\n", i, x[i]);
      fprintf(warra, "%lli - y_%lli <= t;\n", x[i], i);
    }
    for (ll i = 0; i < total - 1; ++i)
      fprintf(warra, "y_%lli - y_%lli >= %lli;\n", i + 1, i, mindist);

    fprintf(warra, "free ");
    for (ll i = 0; i < total; ++i) {
      if (i > 0) fprintf(warra, ",");
      fprintf(warra, "y_%lli", i);
    }
    fprintf(warra, ";");
    fclose(warra);
    system("lp_solve < warra > puta");
    FILE *puta = fopen("puta", "r");
    char line[1000];
        double result;
    do {
      line[0] = 0;
      fgets(line, sizeof(line), puta);
      if (line[0] == 'V' && line[1] == 'a') {
        char *c = strchr(line, ':');
        int feasible = sscanf(c + 1, "%lf", &result);
        if (feasible == 1) {
 //         printf("obtained %lf\n", result);
        }
          break;
      }
    } while (!feof(puta));
    fclose(puta);

    printf("%lf\n", result);
  }
  return 0;
}
