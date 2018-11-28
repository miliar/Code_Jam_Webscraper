#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <cassert>
#include <ctime>
#include <cstdlib>
#include <cmath>

#define eps 1e-9

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define sz(v)((v).size())

#define task_name "a"
typedef long long ll;


using namespace std;

vector <long long> read() {
  string s;
  cin >> s;
  s += "/";
  long long h = 0;
  vector <long long> res;
  for (int i = 0; i < (int)s.size(); i++) {
    h = h * 999983 + s[i];
    if (s[i] == '/') {
      res.push_back(h);
    }
  }
  return res;
}

int main( void )
{
  freopen(task_name ".in", "r", stdin);
  freopen(task_name ".out", "w", stdout);

  int tn;
  scanf("%d", &tn);

  
  for (int tt = 1; tt <= tn; tt++)
  {
    printf("Case #%d: ", tt);
    int n1, n2;
    scanf("%d%d", &n1, &n2);
    set <ll> s;
    s.insert('/');
    for (int i = 0; i < n1; i++) {
      vector <long long> t = read();
      for (int j = 0; j < (int)t.size(); j++) {
        s.insert(t[j]);
      }
    }
    int res = 0;
    for (int i = 0; i < n2; i++) {
      vector <long long> t = read();
      for (int j = 0; j < (int)t.size(); j++) {
        res += !s.count(t[j]);
        s.insert(t[j]);
      }
    }
    printf("%d\n", res);
  }

   
  
  return 0;
}