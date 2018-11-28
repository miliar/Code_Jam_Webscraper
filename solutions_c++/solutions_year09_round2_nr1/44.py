#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <functional>
#include <map>
#include <set>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define pb push_back
#define mp make_pair

typedef unsigned long long ll;
typedef vector <int> vi;

const int maxv = 1000;

int vn;
set <string> m;
double w[maxv];
string name[maxv];
int l[maxv], r[maxv];

//char buf[999];

void readTree( int v )
{
//  printf("v=%d\n", v);

  int c = getc(stdin);
  while (c != '(')
    c = getc(stdin);

  l[v] = r[v] = -1;
  scanf("%lf", &w[v]);
//  printf("w=%.7lf\n", w[v]);
  c = getc(stdin);
  while (c <= 32)
    c = getc(stdin);
  if (c == ')')
    return;

  name[v] = "";
  while (isalpha(c))
    name[v] += c, c = getc(stdin);
//  printf("w=%.7lf name=%s\n", w[v], name[v].c_str());
  if (name[v] != ")")
  {
    l[v] = vn++;
    r[v] = vn++;
    readTree(l[v]);
    readTree(r[v]);
  }
  while (c != ')')
    c = getc(stdin);
}

double go( int v )
{
//  printf("go : v=%d\n", v);

  double p = 1;
  p *= w[v];
  if (l[v] == -1)
    return p;
  if (m.count(name[v]))
    return p * go(l[v]);
  else
    return p * go(r[v]);
}

int main()
{
  int tn;
  scanf("%d", &tn);
  for (int tt = 1; tt <= tn; tt++)
  {
    int k;
    scanf("%*d");
    vn = 1;
//    puts("!");
    readTree(0);
//    puts("!");
    scanf("%d", &k);
//    printf("k=%d\n", k);
    printf("Case #%d:\n", tt);
    while (k--)
    {   
      int n;
      string s;
      m.clear();
      cin >> s;
//      puts("!");
      scanf("%d", &n);
//      printf("n=%d s=%s\n", n, s.c_str());
      while (n--)
      {
        cin >> s;
        m.insert(s);
      }
//      puts("!");
      printf("%.7lf\n", go(0));
    }
  }
  return 0;
}
