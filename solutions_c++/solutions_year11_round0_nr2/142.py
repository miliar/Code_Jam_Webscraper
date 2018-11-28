#include<iostream>
using namespace std;
char a[200];
char p[300][300];
int v[300][300];
int n,m;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tt,cases,ck,x,i,j;
    char ss[200];
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
        memset(p,0,sizeof(p));
        memset(v,0,sizeof(v));
        for (scanf("%d",&x);x;x--)
        {
            scanf("%s",&ss);
            p[ss[0]][ss[1]]=ss[2];
            p[ss[1]][ss[0]]=ss[2];
        }
        for (scanf("%d",&x);x;x--)
        {
            scanf("%s",&ss);
            v[ss[0]][ss[1]]=1;
            v[ss[1]][ss[0]]=1;
        }
        scanf("%d",&n);
        scanf("%s",&ss);
        m=0;
        for (i=0;i<n;i++)
            {
                a[m]=ss[i];
                m++;
                if (m>1&&p[a[m-1]][a[m-2]]!=0)
                {
                   m--;
                   a[m-1]=p[a[m]][a[m-1]];
                }
                ck=0;
                for (j=0;j+1<m;j++)
                if (v[a[m-1]][a[j]])
                {
                   m=0;
                   ck=1;
                   break;
                }
                if (ck) continue;
            }
        printf("Case #%d: [",tt+1);
        if (m>0) putchar(a[0]);
        for (i=1;i<m;i++) printf(", %c",a[i]);
         puts("]");
    }
    return 0;
}
