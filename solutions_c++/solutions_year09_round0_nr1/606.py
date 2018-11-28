#include <cstdio>
#include <map>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

#define m 5010
#define ml 16
#define mt (ml * m)
#define ms (ml * 26)

int l, d, n, nv;
map <char, int> to[mt];
char s[ms];

void add( int v, char *s )
{
  if (!*s)
    return;
  if (!to[v].count(*s))
    to[v][*s] = nv++;
  add(to[v][*s], s + 1);
}

int count( int v, char *s )
{
  if (*s == 0)
    return 1;
  if (*s == '(')
  {
    char *ss = s;
    while (*ss != ')')
      ss++;
    int sum = 0;
    for (s++; s != ss; s++)
      sum += to[v].count(*s) ? count(to[v][*s], ss + 1) : 0;
    return sum;
  }
  else
    return to[v].count(*s) ? count(to[v][*s], s + 1) : 0;
}

int main()
{
  scanf("%d%d%d", &l, &d, &n);
  nv = 1;
  forn (i, d)
  {
    scanf("%s", s);
    add(0, s);
  }
  forn (i, n)
  {
    scanf("%s", s);
    printf("Case #%d: %d\n", i + 1, count(0, s));
  }
  return 0;
}
