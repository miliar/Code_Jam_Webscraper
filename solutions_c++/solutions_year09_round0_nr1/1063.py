#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cctype>
#include <cmath>

#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <set>
#include <map>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define mp make_pair
#define pb push_back

typedef long long ll;
char w[5004][20];
char pat[2000];
int table[20][26];
int main()
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  int l, d, n;
  scanf("%d%d%d\n", &l, &d, &n);
  forn(i, d)
    gets(w[i]);
  forn(i, n)
  {
    gets(pat);
    memset(table,0 , sizeof(table));
//    printf("%s", pat);
    int j = 0;
    int jj = 0;
    while (j<l)
    {
      if (pat[jj] == '(')
      {
        jj = jj+1;
        while(pat[jj] != ')')
        {
          table[j][pat[jj]-'a'] = 1;
          jj++;
        }
        jj++;
      }
      else
      {
         table[j][pat[jj]-'a'] = 1;
         jj++;        
      }
      j++;
    }
    int ans = 0;
    forn(ii,d)
    {
      int j = 0;
//      printf("%d\n", ii);
      while (j<l)
      {
        if (!(table[j][w[ii][j]-'a']))
          break;
        j++;
      }
      if (j>=l){ 
//        printf("%d\n", ii);
        ans++;
     }
    }
    printf("Case #%d: %d\n", i+1, ans);
  }
  return 0;
}

