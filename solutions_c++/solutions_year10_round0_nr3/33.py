#include <iostream>
#include <map>
using namespace std;

long long g[1010], amt[1010];
int nxt[1010];

int main() {
  int t; cin >> t;
  for(int c = 1; c <= t; c++) {
    long long R, k;
    int N;
    cin >> R >> k >> N;
    for(int i = 0; i < N; i++)
      cin >> g[i];

    for(int i = 0; i < N; i++) {
      amt[i] = 0;
      int j = i;
      do {
        if(amt[i] + g[j] > k) break;
        amt[i] += g[j];
        j++; j %= N;
      } while(j != i);
      nxt[i] = j;
    }

    int cur = 0;
    long long res = 0, rd = 0;
    map<int, long long> vis, visrd;
    vis[0] = 0; visrd[0] = 0;
    while(rd < R) {
      res += amt[cur];
      cur = nxt[cur];
      if(vis.find(cur) != vis.end()) { rd++; break; }
      vis[cur] = res;
      visrd[cur] = rd + 1;
      rd++;
    }

    if(rd < R) {
      long long cyclen = rd - visrd[cur], cycamt = res - vis[cur];
      long long cycleft = (R - rd) / cyclen;
      // cout << "cyc: " << cyclen << " " << cycamt << " " << cycleft << endl;
      res += cycamt * cycleft; rd += cyclen * cycleft;

      while(rd < R) {
        res += amt[cur];
        cur = nxt[cur];
        rd++;
      }
    }

    cout << "Case #" << c << ": " << res << endl;
  }
  return 0;
}
