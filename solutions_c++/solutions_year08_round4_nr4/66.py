#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;
 
#define all(c) ((c).begin()), ((c).end()) 
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end()) 
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)
 
typedef long long ll;
 
int main() {
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {
    int K;
    string S;
    cin >> K >> S;

    vector<int> per(K);
    for (int i = 0; i < K; i++) per[i] = i;

    int ans = 999999999;

    do {
      int prv = -1;
      int cnt = 0;
      for (int i = 0; i < S.length(); i++) {
        char c = S[(i / K) * K + per[i % K]];
        if (c != prv) cnt++;
        prv = c;
      }

      ans <?= cnt;

    } while (next_permutation(all(per)));

    printf("Case #%d: %d\n", t, ans);
  }
}
