#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<iostream>
#include<algorithm>
#include<list>

using namespace std;

int main(void)
{
    int T;
    freopen("A-small.in","r",stdin);
    freopen("A-small.out","w",stdout);
    scanf("%d",&T);
    for(int t = 0; t<T; t++)
    {
        int n,pd,pg;
        scanf("%d%d%d",&n,&pd,&pg);
        if(pd > 0 && pg == 0)
        {
            printf("Case #%d: Broken\n",t+1);
        }
        else if(pd < 100 && pg == 100)
        {
            printf("Case #%d: Broken\n",t+1);
        }
        else
        {
            bool pospd = false;
            int todpl = 0,todw = 0;
            for(int i = 1; i<=n; i++)
            {
                int a = i*pd / 100;
                if(a*100 / i == pd)
                {
                    pospd = true;
                    todpl = i;
                    todw = a;
                    break;
                }
            }
            bool pospg = false;
            if(pospd)
            {
                printf("Case #%d: Possible\n",t+1);
            }
            else
            {
                printf("Case #%d: Broken\n",t+1);
            }
            /*for(int i = 1; i<=10000; i++)
            {
                for(int j = 1; j<=10000; j++)
                {
                    int tp = i + todpl;
                    int tw = j + todw;
                    
                    if(tw * 100 / tp == pg && tw*100 % tp == 0)
                    {
                        pospg = true;
                        break;
                    }
                }
                if(pospg)
                    break;
            }
            if(pospg && pospd)
            {
                printf("Case #%d: Possible\n",t+1);
            }
            else
            {
                printf("Case #%d: Broken\n",t+1);
            }*/
        }
    }
    return 0;
}
