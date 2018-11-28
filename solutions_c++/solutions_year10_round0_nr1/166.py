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

  rep (t, T) {
    int N, K;
    scanf("%d%d", &N, &K);

    int x = 1;
    rep (i, N - 1) x = x * 2 + 1;

    printf("Case #%d: ", t + 1);
    if (K % (x + 1) == x) puts("ON");
    else puts("OFF");
  }

  return 0;
}
