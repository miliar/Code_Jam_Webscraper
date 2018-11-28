//**** HEADER ****

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
  int N, S, p;
  cin >> N >> S >> p;
  vector<int> scores(N), maxs(N), maxss(N);
  for (int i = 0; i < N; i++) {
    cin >> scores[i];
    maxs[i] = (scores[i]-1)/3 + 1;
    maxss[i] = (scores[i]-2)/3 + 2;
    if (scores[i] == 0)  maxs[i] = maxss[i] = 0;
    if (scores[i] == 1)  maxss[i] = 1;
    if (scores[i] >= 29) maxss[i] = 10;
  }
  
  int res = 0;
  for (int i = 0; i < N; i++)
    if (maxs[i] >= p)
      res++;
  for (int i = 0, s = 0; i < N; i++)
    if (maxs[i] < p && maxss[i] >= p && s < S) {
      res++;
      s++;
    }

  cout << "Case #" << (tc + 1) << ": " << res << endl;
}

int main()
{
  int T = 0;

  cin >> T;
  for (int t = 0; t < T; t++)
    run(t);

  return 0;
}
