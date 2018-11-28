#include<cstdio>
#include<algorithm>
using namespace std;
int r[10],ra[10],d[10];
int x[10],y[10];
bool cmp(int x,int y)
{
    return r[x]<r[y];
}
int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for (int cas=1;cas<=t;cas++)
    {
        int n,w,l;
        scanf("%d%d%d",&n,&w,&l);
        for (int i=0;i<n;i++)
            ra[i]=i;
        for (int i=0;i<n;i++)
            scanf("%d",&r[i]);
        sort(ra,ra+n,cmp);
        sort(r,r+n);
        for (int i=0;i<n;i++)
            d[ra[i]]=i;
        printf("Case #%d:",cas);
        if (w>l)
            for (int i=n-1,p=-r[i],t=0;i>=0;i--)
            {
                if (!t)
                    p+=r[i];
                else
                    p-=r[i];
                if (p>w)
                {
                    p=w;
                    t=l;
                }
                x[i]=p;
                y[i]=t;
                if (!t)
                    p+=r[i];
                else
                    p-=r[i];
            }
        else
            for (int i=n-1,p=-r[i],t=0;i>=0;i--)
            {
                if (!t)
                    p+=r[i];
                else
                    p-=r[i];
                if (p>l)
                {
                    p=l;
                    t=w;
                }
                x[i]=t;
                y[i]=p;
                if (!t)
                    p+=r[i];
                else
                    p-=r[i];
            }
        for (int i=0;i<n;i++)
            printf(" %d %d",x[d[i]],y[d[i]]);
        puts("");
    }
    return 0;
}
