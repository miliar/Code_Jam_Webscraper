#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int MAXN=30;

int c[MAXN][MAXN];
int d[MAXN][MAXN];

char s[110];
int ans[110];
char ch;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j;
    int t,cas,nc,nd,n,l,t1,t2,t3;
    scanf("%d",&t);
    for(cas=1;cas<=t;cas++)
    {
        memset(c,0,sizeof(c));
        memset(d,0,sizeof(d));
        scanf("%d",&nc);
        for(i=0;i<nc;i++)
        {
            scanf("%s",s);
            t1=s[0]-'A'+1;
            t2=s[1]-'A'+1;
            t3=s[2]-'A'+1;
            c[t1][t2]=t3;
            c[t2][t1]=t3;
        }
        scanf("%d",&nd);
        for(i=0;i<nd;i++)
        {
            scanf("%s",s);
            t1=s[0]-'A'+1;
            t2=s[1]-'A'+1;
            d[t1][t2]=1;
            d[t2][t1]=1;
        }
        scanf("%d",&n);
        getchar();
        l=0;
        for(i=0;i<n;i++)
        {
            scanf("%c",&ch);
            t1=ch-'A'+1;
            if (l>0 && c[ans[l-1]][t1]>0)
            {
                ans[l-1]=c[ans[l-1]][t1];
            }
            else
            {
                for(j=0;j<l;j++)
                    if (d[ans[j]][t1]>0) break;
                if (j<l)
                {
                    l=0;
                }
                else
                {
                    ans[l]=t1;
                    l++;
                }
            }
        }
        printf("Case #%d: [",cas);
        if (l>0) printf("%c",ans[0]+'A'-1);
        for(i=1;i<l;i++) printf(", %c",ans[i]+'A'-1);
        printf("]\n");
    }
    return 0;
}
