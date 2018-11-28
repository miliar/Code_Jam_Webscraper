#include <cstdio>
#include <cassert>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int n, tn, nt;

char s[250][250];

int cmp(char x, char y) {
  return x==' ' || y==' ' || x==y;
}

int main(void)
{
   freopen("A-small-attempt1.in", "r", stdin);
   freopen("A-small-attempt1.out", "w", stdout);
   //freopen("A-large.in", "r", stdin);
   //freopen("A-large.out", "w", stdout);

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      //fprintf(stderr, "Case #%d: \n", tn+1);

      memset(s, 32, sizeof(s));

      scanf("%d", &n);
      while (getchar()!='\n') ;
      for (int i=0; i<2*n-1; i++)
      {
        gets(s[100+i]+100);
        s[100+i][strlen(s[100+i])]=32;
      }

      int ans=100000;

      for (int i=0; i<2*n-1; i++)
        for (int i2=0; i2<2*n-1; i2++)
      {
        int good=1;
        for (int j=0; j<2*n-1; j++)
          for (int k=0; k<2*n-1; k++)
          {
            if (!cmp(s[100+2*i-j][100+k], s[100+j][100+k]))
              good=0;
            if (!cmp(s[100+j][100+2*i2-k], s[100+j][100+k]))
              good=0;
            if (!cmp(s[100+2*i-j][100+2*i2-k], s[100+j][100+k]))
              good=0;
          }
        if (good)
        {
          int b=abs(i-n+1)+abs(i2-n+1);
          ans=min(ans, (2*n+b)*b);
        }
      }
          
      printf("Case #%d: ", tn+1);
      printf("%d\n", ans);
   }
   return 0;
}
