#include <algorithm>
#include <cmath>
#include <climits>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <queue>
using namespace std;

typedef long long int64;
//typedef __int128_t int128;
typedef vector<int> veci;
typedef vector<string> vecs;

#define VAR(a, b) __typeof(b) a=(b)
#define FOREACH(it, c) for (VAR(it, (c).begin()); it != (c).end(); ++it)
#define TRACE(x) cout << #x << endl
#define DEBUG(x) cout << #x " = " << (x) << endl
#define DEBUGA(a, n) VAR(__p, a); cout << #a " = {"; for (int __i = 0; __i < n; ++__i, ++__p) cout << (__i == 0 ? "" : ", ") << *(__p); cout << "}" << endl
#define CLR(a, val) memset(a, val, sizeof(a))

template<class T1, class T2> ostream& operator << (ostream &o, const pair<T1, T2> &p)
{
  return o << "(" << p.first << ", " << p.second << ")";
}

template<class T> ostream& operator << (ostream &o, const vector<T> &v)
{
  o << '{';
  FOREACH(it, v) o << (it == v.begin() ? "" : ", ") << *it;
  return o << '}';
}

void run(int tc)
{
  int N;
  cin >> N;
  vector<pair<int, int>> levels(N);
  for (int i = 0; i < N; i++)
    cin >> levels[i].first >> levels[i].second;
  vector<int> played(N);

  int nplayed = 0, stars = 0, games = 0;
  do {
    nplayed = 0;
    for (int i = 0; i < N; i++)
      if (stars >= levels[i].second && played[i] < 2) {
        games++; nplayed++;
        if (played[i] == 1) stars++;
        else stars += 2;
        played[i] = 2;
      }
    if (nplayed == 0) {
      int maxs = -1, maxp = -1;
      for (int i = 0; i < N; i++)
        if (stars >= levels[i].first && played[i] == 0 && levels[i].second > maxs) {
          maxs = levels[i].second;
          maxp = i;
        }
      if (maxs >= 0) {
        nplayed++;
        stars++;
        games++;
        played[maxp] = 1;
      }
    }
  }
  while (nplayed > 0);


  if (stars == 2*N)
    cout << "Case #" << (tc + 1) << ": " << games << endl;
  else
    cout << "Case #" << (tc + 1) << ": Too Bad" << endl;
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T >> ws; tc < T; tc++) run(tc);
  return 0;
}
