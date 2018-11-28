#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>
#include <cmath>

#include <algorithm>
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

ll gcd( ll a, ll b )
{
  if (b == 0)
    return a;
  return gcd(b, a % b);
}

ll nok( ll a, ll b )
{
  return a / gcd(a, b) * b;
}

int main()
{
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);

  int T;
  cin >> T;
  REP(ti, T)
  {
    ll n, p, q;
    cin >> n >> p >> q;
    
    if (p == 0 && q == 0)
      printf("Case #%d: %s\n", ti + 1, "Possible");
    else if (p != 0 && q == 0)
      printf("Case #%d: %s\n", ti + 1, "Broken");
    else if (q == 100)
      printf("Case #%d: %s\n", ti + 1, (p == 100) ? "Possible" : "Broken");
    else
    {
      ll u = 100 / gcd(p, 100);
      bool good = (n / u >= 1);
      printf("Case #%d: %s\n", ti + 1, (good ? "Possible" : "Broken"));
    }
  }

  return 0;
}
