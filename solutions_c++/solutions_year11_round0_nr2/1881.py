
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

char g[300][300];
bool c[300][300];
char s[201] , ans[200];

int main()
{
    freopen("C:\\Users\\刘奚睿\\Desktop\\code jam\\B-small-attempt3.in","r",stdin);
    freopen("C:\\Users\\刘奚睿\\Desktop\\code jam\\B-small-attempt3.out","w",stdout);
    int C , D ;
    int i,j,k,len,ncase;scanf("%d",&ncase);
    for(int cas=1;cas<=ncase;++cas)
    {
        memset(g,0,sizeof(g));
        memset(c,0,sizeof(c));
        scanf("%d",&C);
        for(i=0;i<C;++i)
        {
            scanf("%s",s);
            g[s[0]][s[1]]=g[s[1]][s[0]] = s[2];
        }
        scanf("%d",&D);
        for(i=0;i<D;++i)
        {
            scanf("%s",s);
            c[s[0]][s[1]]=c[s[1]][s[0]]=1;
        }
        scanf("%d",&len);
        scanf("%s",s);
        int cnt = 0 ;
        for(i=0;i<len;++i)
        {
            if(cnt == 0)
            {
                ans[cnt++] = s[i];
            }
            else
            {
                if(g[s[i]][ans[cnt-1]])
                {
                    ans[cnt-1]=g[s[i]][ans[cnt-1]];
                }
                else
                {
                    for(j=0;j<cnt;++j)
                    {
                        if(c[ans[j]][s[i]])break;
                    }
                    if(j!=cnt)
                    {
                        cnt = 0;
                    }
                    else ans[cnt++] = s[i];
                }
            }
        }
        printf("Case #%d: [",cas);
        for(i=0;i<cnt-1;++i)printf("%c, ",ans[i]);
        if(cnt)printf("%c]\n",ans[i]);
        else printf("]\n");
    }
    return 0;
}
