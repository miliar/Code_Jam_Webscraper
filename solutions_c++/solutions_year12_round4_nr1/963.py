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
  int N; cin >> N;
  vector<pair<int64, int64>> lines(N+1);
  for (int i = 0; i < N; i++)
    cin >> lines[i].first >> lines[i].second;
  cin >> lines[N].first;

  vector<int64> can(N+1, -1);
  can[0] = lines[0].first;
  for (int i = 0; i < N; i++) {
    if (can[i] < 0) break;
    for (int j = i+1; j < N+1 && lines[j].first-lines[i].first <= can[i]; j++) {
      can[j] = max(can[j], min(lines[j].first-lines[i].first, lines[j].second));
      if (j == N && can[j] >= 0) {
        cout << "Case #" << (tc + 1) << ": " << "YES" <<  endl;
        return;
      }
    }
  }

  cout << "Case #" << (tc + 1) << ": " << "NO" <<  endl;
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T; tc < T; tc++) run(tc);
  return 0;
}
