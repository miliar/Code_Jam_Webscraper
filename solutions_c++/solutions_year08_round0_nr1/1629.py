#include <algorithm>
#include <string>
#include <cstdio>
#include <map>
#include <vector>
#define PB push_back
#define FOREACH(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); ++it)

using namespace std;

map<string, int> senames;
vector<int> queries;

int main() {
  int n, s, q;
  char str[1000];

  senames.clear();
  fgets(str, 1000, stdin); sscanf(str, "%d", &n);
  for (int casei = 0; casei < n; ++casei) {
    fgets(str, 1000, stdin); sscanf(str, "%d", &s);
    for (int i = 0; i < s; ++i) {
      fgets(str, 1000, stdin);
      string sen(str);
      senames[sen] = i+1;
    }

    queries.clear();
    fgets(str, 1000, stdin); sscanf(str, "%d", &q);
    for (int i = 0; i < q; ++i) {
      fgets(str, 1000, stdin);
      string qn(str);
      queries.PB(senames[qn]);
    }

    int sol = 0;

    vector<bool> found(s);
    int nfound = 0;

    FOREACH(queries, it) {
      if (!found[*it-1]) {
        found[*it-1] = true;
        ++nfound;
      }
      if (nfound == s) {
        for (int i = 0; i < s; ++i)
          found[i] = false;
        found[*it-1] = true;
        nfound = 1;
        ++sol;
      }
    }

    printf("Case #%d: %d\n", casei+1, sol);
  }
  return 0;
}
