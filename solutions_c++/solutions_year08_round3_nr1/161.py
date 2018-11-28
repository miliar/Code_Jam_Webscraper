#include <algorithm>
#include <string>
#include <cstdio>
#include <map>
#include <vector>
#define X first
#define Y second
#define PII pair<int, int>
#define PB push_back
#define FOREACH(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); ++it)

using namespace std;

struct Comparator {
  bool operator()(const long long a, const long long b) const {
   return a > b;
  }
};

int main() {
    int ncase;
    scanf("%d", &ncase);
    for (int icase = 0; icase < ncase; ++icase) {
        int p, k, l;
        scanf("%d %d %d", &p, &k, &l);
        vector<int> freq(l);
        for (int i = 0; i < l; ++i)
            scanf("%d", &freq[i]);

        long long sol = 0;            
        sort(freq.begin(), freq.end(), Comparator());
        int n = (int) freq.size();
        for (int i = 0; i < n; ++i)
            sol += freq[i] * (i / k + 1);

        printf("Case #%d: %lld\n", icase+1, sol);
    }
    return 0;
}
