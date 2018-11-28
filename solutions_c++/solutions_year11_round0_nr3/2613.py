#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>
#include <cmath>

#include <algorithm>
#include <numeric>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>

#define sz(c) ((int)(c).size())
#define pb push_back
#define mp make_pair

#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPC(i, c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define FOR(i, s, n) for (int i = (s); i < (n); ++i)
#define ALL(c) (c).begin(), (c).end()

using namespace std;
typedef long long ll;
typedef double dbl;
typedef pair<int, int> pii;

typedef unsigned int uint;

const int maxx = 1048576;

int main()
{
  freopen("c-large.in", "rt", stdin);
//  freopen("c.in", "rt", stdin);
  freopen("c.out", "wt", stdout);

  long st = clock();

  int Tests;
  scanf("%d", &Tests);
  REP(testIt, Tests)
  {
    cerr << "test #" << (testIt + 1) << "\n";

    int n;
    scanf("%d", &n);

    vector<uint> vals(n);
    REP(i, n)
      scanf("%du", &vals[i]);

    int allSum = accumulate(ALL(vals), 0);

    vector<int> bits(20, 0);
    REP(i, n)
      REP(j, sz(bits))
        if ((vals[i] >> j) & 1)
          bits[j]++;

    bool no = false;
    REP(j, sz(bits))
      if (bits[j] & 1)
        no = true;
    printf("Case #%d: ", testIt + 1);
    if (no)
      printf("NO\n");
    else
      printf("%d\n", allSum - int(*min_element(ALL(vals))));
    cerr << "elapsed: " << 1.0 * (clock() - st) / CLOCKS_PER_SEC << endl;
  }

  return 0;
}
