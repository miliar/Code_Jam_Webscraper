#define DEBUG
#ifdef DEBUG
#include<iostream>
using std::cin;
using std::cout;
using std::endl;
#endif
#include <cstdio>
#include <cstring>

const int MAXN = 110;

int a[26][26];
bool b[26][26];
bool chk[26];
int list[MAXN];
int len;

char s[MAXN];

void init()
{
   memset(a, 0xff, sizeof(a));
   memset(b, 0, sizeof(b));
   int n, i;
   char tmp[MAXN];
   scanf("%d", &n);
   while (n--)
   {
      scanf("%s", tmp);
      a[tmp[0]-'A'][tmp[1]-'A'] = tmp[2] - 'A';
      a[tmp[1]-'A'][tmp[0]-'A'] = tmp[2] - 'A';
   }
   scanf("%d", &n);
   while (n--)
   {
      scanf("%s", tmp);
      b[tmp[0]-'A'][tmp[1]-'A'] = true;
      b[tmp[1]-'A'][tmp[0]-'A'] = true;
   }
}

void solve()
{
   len = 0;
   int i, j, n;
   scanf("%d", &n);
   scanf("%s", s);
   for (i=0; i<n; ++i)
   {
      list[++len] = s[i] - 'A';
      while ((len >= 2) && (a[list[len]][list[len-1]] >= 0))
      {
         --len;
         list[len] = a[list[len]][list[len+1]];
      }
      for (j=1; j<len; ++j)
      if (b[list[len]][list[j]]) len = 0;
   }
   if (len == 0) printf("[]\n");
   else
   {
      printf("[%c", list[1]+'A');
      for (i=2; i<=len; ++i)
         printf(", %c", list[i] + 'A');
      printf("]\n");
   }
}

int main()
{
   int TT, CASE;
   scanf("%d", &TT);
   for (CASE=1; CASE<=TT; ++CASE)
   {
      init();
      printf("Case #%d: ", CASE);
      solve();
   }
   return 0;
}