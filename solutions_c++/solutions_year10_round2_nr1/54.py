#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>

#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define mp make_pair

typedef long long ll;

const int mlen = (int)1e6 + 10;

char s[mlen];
int res, vn;
map <pair<int, string>, int> next;

void Add( char *s, int add )
{
  int v = 0;
  while (*s == '/')
  {
    int len = (int)strchr(s + 1, '/');
    if (!len)
      len = strlen(s);
    else
      len -= (int)s;
//    printf("len = %d\n", len);
    string word = "";
    while (len--)
      word += *s++;
//    printf("word = %s\n", word.c_str());
    if (!next[mp(v, word)])
      res += add, next[mp(v, word)] = vn++;
    v = next[mp(v, word)];
  }
}

int main()
{
  int tn;
  scanf("%d", &tn);
  for (int tt = 1; tt <= tn; tt++)
  {  
    int n, k;
    scanf("%d%d", &n, &k);
//    printf("n=%d k=%d\n", n, k);
    res = 0, vn = 1;
    next.clear();
    gets(s);
    forn(i, n + k)
    {
      gets(s);
//      puts(s);
      Add(s, i >= n);
    }
    printf("Case #%d: %d\n", tt, res);
  }
  return 0;
}
