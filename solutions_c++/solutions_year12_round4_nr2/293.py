#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

int T;
int n,a,b;
int r[1024];
int lab[1024];
int x[1024];
int y[1024];
int lx,lr,ly,my;

bool cmp(int x,int y)
{
    return r[x]<r[y];
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for (int w=1;w<=T;w++)
    {
        scanf("%d%d%d",&n,&a,&b);
        for (int i=1;i<=n;i++)
            scanf("%d",r+i),lab[i]=i;
        sort(lab+1,lab+1+n,cmp);
        lx=-1000000000;
        lr=0;
        ly=-1000000000;
        my=0;
        for (int i=n;i>0;i--)
        {
            if (lx+lr+r[lab[i]]<=a)
            {
                x[lab[i]]=max(lx+lr+r[lab[i]],0);
                y[lab[i]]=max(ly+r[lab[i]],0);
                my=max(my,y[lab[i]]+r[lab[i]]);
                lx=x[lab[i]];
                lr=r[lab[i]];
            }
            else
            {
                lx=-1000000000;
                lr=0;
                ly=my;
                x[lab[i]]=max(lx+lr+r[lab[i]],0);
                y[lab[i]]=max(ly+r[lab[i]],0);
                my=max(my,y[lab[i]]+r[lab[i]]);
                lx=x[lab[i]];
                lr=r[lab[i]];
                lr=r[lab[i]];
            }
        }
        printf("Case #%d:",w);
        for (int i=1;i<=n;i++)
        {
            printf(" %.1f %.1f",(double)x[i],(double)y[i]);
           // if (x[i]>a || y[i]>b)
            //    printf("error\n");
        }
        printf("\n");
    }
    return 0;
}
