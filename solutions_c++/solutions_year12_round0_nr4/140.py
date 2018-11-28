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

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

void run(int tc)
{
  int H, W, D;
  cin >> H >> W >> D;
  int x0, y0;
  string s;
  for (int i = 0; i < H; i++) {
    cin >> s;
    for (int j = 0; j < W; j++)
      if (s[j] == 'X') {
        x0 = 2*(j - 1) + 1;
        y0 = 2*(H - i - 2) + 1;
      }
  }

  set<pair<int, int>> lines;
  W = 2*(W-2); H = 2*(H-2); D = 2*D;
  int res = 0, blah=0;
  for (int i = -(D+W-1)/W-blah; i <= (D+W-1)/W+blah; i++)
    for (int j = -(D+H-1)/H-blah; j <= (D+H-1)/H+blah; j++) {
      int x = i*W+x0, y = j*H+y0;
      if (abs(i)%2==1) x = (i+1)*W-x0;
      if (abs(j)%2==1) y = (j+1)*H-y0;
      int dx = x-x0, dy = y-y0, dd = dx*dx+dy*dy;
      if (i != 0 || j != 0) {
        int g = gcd(abs(dx), abs(dy));
        dx /= g; dy /= g;
        if (dd <= D*D && lines.count(make_pair(dx, dy)) == 0) {
          res++;
          lines.insert(make_pair(dx, dy));
        }
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
