#include<cstdio>
#include<algorithm>

using namespace std;

struct node
{
    int a,b;
};

bool operator<(node a,node b)
{
    return a.b<b.b;
}

node a[10000];
double level,ans[10000];

int main()
{
    int tst,i,n,j,lp;
    double x,sum;
    
    scanf("%d",&tst);
    for (lp=0;lp<tst;lp++)
    {
        scanf("%d",&n);
        sum=0;
        for (j=0;j<n;j++)
        {
            scanf("%d",&a[j].b);
            sum+=a[j].b;
            a[j].a=j;
        }
        sort(a,a+n);
        a[n].b=100000;
        level=0;
        x=sum;
        for (i=0;i<n;i++)
        {
            if ((i+1)*(a[i+1].b-a[i].b)<x)
            {
                level=a[i+1].b;
                x-=(i+1)*(a[i+1].b-a[i].b);
            } else {
                level=a[i].b+x/(i+1);
                break;
            }
        }
        for (i=0;i<n;i++)
        {
            ans[a[i].a]=(level-a[i].b)/sum;
            if (ans[a[i].a]<0) ans[a[i].a]=0;
        }
        printf("Case #%d:",lp+1);
        for (i=0;i<n;i++)
        {
            printf(" %.6f",ans[i]*100);
        }
        printf("\n");
    }
    return 0;
}
        
