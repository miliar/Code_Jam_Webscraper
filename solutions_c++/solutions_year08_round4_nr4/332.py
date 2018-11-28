#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)

typedef long long ll;
typedef pair <int, int> pii;
typedef vector <int> vi;

#define mlen 50013
#define maxk 100
#define inf (int)1e9

char s[mlen], s2[mlen];
int n, k, p[maxk];

int main()
{
  freopen("c.in", "r", stdin);
  freopen("c.out", "w", stdout);
  
  int tn;
  scanf("%d", &tn);
  forn(tt, tn)
  {
    int res = inf;
    scanf("%d%s", &k, s);
    n = strlen(s);
    forn(i, k)
      p[i] = i;
    do
    {
      for (int i = 0; i < n; i += k)
        forn(j, k)
          s2[i + j] = s[i + p[j]]; 
      int x = 0;
      forn(i, n)
        if (i == 0 || s2[i - 1] != s2[i])
          x++;
      if (x < res)
        res = x;
    } while (next_permutation(p, p + k));
    
    printf("Case #%d: ", tt + 1);
    printf("%d", res);
    puts("");
  }
  
  return 0;
}
