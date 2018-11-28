# include <cstdio>
# include <string>

using namespace std;

const string ans[31] = {
  "", "",
  "027", "143", "751", "935", "607", "903", "991",
  "335", "047", "943", "471", "055", "447", "463",
  "991", "095", "607", "263", "151", "855", "527",
  "743", "351", "135", "407", "903", "791", "135", "647"};


int n;

void init() {
  scanf("%d", &n);
}

void solve() {
  printf("%s\n", ans[n].c_str());
}

int main() {
  int n, i;
  for (scanf("%d", &n), i = 1; i <= n; ++i) {
    init();
    printf("Case #%d: ", i);
    solve();
  }
}
