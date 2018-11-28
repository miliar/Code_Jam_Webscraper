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
  int A, B, res = 0;
  cin >> A >> B;

  int m = 1, d = 1;
  while (m*10 <= A) m *= 10, d++;

  vector<int> vals(d);
  for (int i = A; i <= B; i++) {
    int v = i;
    memset(&vals[0], 0, d*sizeof(int));
    for (int j = 0; j < d-1; j++) {
      v = m*(v%10) + v/10;

      bool good = true;
      for (int k = 0; k < j; k++)
        if (vals[k] == v)
          good = false;
      vals[j] = v;

      if (i < v && v <= B && good)
        res++;
    }
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
