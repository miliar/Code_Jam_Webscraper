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

char tr[256] = {0};

void run(int tc)
{
  string s;
  getline(cin, s);
  for (int i = 0; i < s.size(); i++)
    s[i] = tr[s[i]];
  cout << "Case #" << (tc + 1) << ": " << s << endl;
}

int main()
{
  for (int i = 0; i < sizeof(tr); i++)
    tr[i] = i;
  tr['y'] = 'a';
  tr['e'] = 'o';
  tr['q'] = 'z';
  tr['z'] = 'q';
  const char to[] = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
  const char fr[] = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
  for (int i = 0; i < sizeof(to); i++)
    tr[to[i]] = fr[i];

  int T = 0;
  cin >> T; cin.getline(0, 0);
  for (int t = 0; t < T; t++)
    run(t);

  return 0;
}
