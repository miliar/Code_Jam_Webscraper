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
  int A, B;
  cin >> A >> B;
  vector<double> p(A);
  double pgood = 1.0, mine = 3*B;
  for (int i = 0; i < A; i++) {
    cin >> p[i];
    pgood *= p[i];
    double e = (A-i-1+B-i)*pgood + (A-i-1+B-i+B+1)*(1-pgood);
    //DEBUG(pgood);
    //DEBUG(e);
    //DEBUG(make_pair(A-i-1+B-i, A-i-1+B-i+B+1));
    mine = min(mine, e);
  }
  //DEBUG(mine);
  mine = min(mine, 1.0+B+1.0);
  cout << "Case #" << (tc + 1) << ": ";
  printf("%.7f\n", mine);
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T >> ws; tc < T; tc++) run(tc);
  return 0;
}
