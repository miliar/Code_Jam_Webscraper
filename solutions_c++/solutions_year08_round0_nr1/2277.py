#include <stdio.h>
#include <map>
#include <string>

using namespace std;

string ss;
map <string, int> mm;
char s[150][200],q[1050][200];
int T,Q,S,i,j,k,jum[150],ff[150],res,choice,choice1,a,b;

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&T);
    for (i = 1;i <= T; ++i)
    {
        scanf("%d\n",&S); mm.clear();
        for (j = 0;j < S; ++j)
        {
            gets(s[j]);
            mm[s[j]] = j+1;
            jum[j+1] = 0; ff[j+1] = -1;
        }
        scanf("%d\n",&Q); choice = 0;
        for (j = 0;j < Q; ++j)
        {
            gets(q[j]);
            int idx = mm[q[j]];
            if (ff[idx] == -1) { ff[idx] = j; choice = j; choice1 = idx; }
            ++jum[idx];
        }
        for (j = 1;j <= S; ++j)
            if (jum[j] == 0) break;
        if (j > S)
        {
              res = 0; k = 0;
              do{
                  //puts(s[choice1-1]);
                  a = choice; b = choice1;
                  for (j = 1;j <= S; ++j)
                  {
                      //printf("j : %d, choice1:%d\n",j,choice1);
                      if (j != choice1)
                      {
                          ff[j] = -1;
                          for (k = choice + 1;k < Q; ++k)
                              if (strcmp(q[k],s[j-1]) == 0 && ff[j] == -1)
                              {
                                  ff[j] = k;
                                  if (a < k)
                                  {
                                      a = k;
                                      b = j;
                                  }
                              }
                          //printf("choice : %d, choice1 : %d, j : %d, ff[j] : %d, a : %d, b : %d \n",choice,choice1,j,ff[j],a,b);
                          if (ff[j] == -1) { choice1 = j; break; }
                          //printf("examining j : %d, a : %d, b : %d, ff[j] : %d\n",j,a,b,ff[j]);
                      }
                  }
                  ++res;
                  if (j <= S) break;
                  choice = a; choice1 = b;
              }while (1);
              //puts(s[choice1-1]);
              printf("Case #%d: %d\n",i,res);
        }
        else printf("Case #%d: %d\n",i,0);
    }
    return 0;
}
