#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <string>
#include <set>

using namespace std;

#define MAX 256

int c[MAX][MAX], d[MAX][MAX];

void combine(vector<char> &r)
{
  int n = (int)r.size();

  if (n < 2) return;
  char x = (char)c[(int)r[n-2]][(int)r[n-1]];
  if (x > 0)
  {
    r[n-2] = x;
    r.erase(r.end()-1);
    combine(r);
  }
}

void oppose(vector<char> &r)
{
  int n = (int)r.size();
  for(int i = 0; i < n; i++)
    for(int j = i+1; j < n; j++)
      if (d[(int)r[i]][(int)r[j]] > 0)
      {
        r.clear();
        return;
      }
}

int main(void)
{
  int T,caso;

  for(scanf("%d",&T), caso = 1; caso <= T; caso++)
  {
    int C,D,N;
    char s[MAX];

    memset(c, 0, sizeof(c));
    memset(d, 0, sizeof(d));

    scanf("%d", &C);
    while(C-- > 0)
    {
      scanf("%s", s);
      c[(int)s[0]][(int)s[1]] = c[(int)s[1]][(int)s[0]] = (int)s[2];
    }

    scanf("%d", &D);
    while(D-- > 0)
    {
      scanf("%s", s);
      d[(int)s[0]][(int)s[1]] = d[(int)s[1]][(int)s[0]] = 1;
    }

    vector<char> r;
    scanf("%d %s", &N, s);
    for(int i = 0; i < N; i++)
    {
      r.push_back(s[i]);
      combine(r);
      oppose(r);
    }

    printf("Case #%d: [", caso);
    for(int i = 0; i < (int)r.size(); i++)
    {
      printf("%c", r[i]);
      if (i < (int)r.size()-1) printf(", ");
    }
    printf ("]\n");
  }

  return(0);
}

