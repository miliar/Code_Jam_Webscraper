#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#define maxn 103
using namespace std;

int t[maxn];
int n,s,p,ans;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int i;
    int tt,cas = 1;
    scanf("%d",&tt);
    while (tt--)
    {
        scanf("%d%d%d",&n,&s,&p);
        for (i = 0; i < n; ++i)
        {
            scanf("%d",&t[i]);
        }
        int ctp = 0;
        for (i = 0 ; i < n; ++i)
        {
            if (t[i] < 3)
            {
                if (t[i] == 0) if (0 >= p) ctp++;
                if (t[i] == 1) if (1 >= p) ctp++;
                if (t[i] == 2)
                {
                   if (1 >= p) ctp++;
                   else if (2 >= p && s > 0)
                   {
                       ctp++; s--;
                   }
                }
            }
            else
            {
                int f = t[i]%3;
                int sh = t[i]/3;
                if (f == 0)
                {
                    if (sh >= p) ctp++;
                    else if ((sh + 1 >= p) && s > 0)
                    {
                        ctp++; s--;
                    }
                }
                if (f == 1)
                {
                    if (sh + 1 >= p) ctp++;
                }
                if (f == 2)
                {
                    if ((sh+ 1) >= p) ctp++;
                    else if ((sh + 2) >= p && s > 0)
                    {
                        ctp++; s--;
                    }
                }
            }
        }
      printf("Case #%d: %d\n",cas++,ctp);
    }
   return 0;
}

