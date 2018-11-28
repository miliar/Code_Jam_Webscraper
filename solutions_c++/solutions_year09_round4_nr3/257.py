#include <iostream>
#include <algorithm>
using namespace std;

struct point
{
    int a[100];
}p[200]={0};
bool g[200][200]={0};
int match[200]={0};
bool viewed[200]={0};
int ncase,i,j,k,t,m,n,sum,x,y;


bool cross(int x, int y)
{
    int i;
    int y1,y2,y3,y4;
    for (i=1; i<k; i++)
    {
        y1 = p[x].a[i];
        y2 = p[x].a[i-1];
        y3 = p[y].a[i];
        y4 = p[y].a[i-1];
        if(y1==y3||y2==y4) return true;
        if(y1<y3&&y2>y4) return true;
        if(y1>y3&&y2<y4) return true;
    }
    return false;
}

bool find(int now)
{
    int i;
    if (now<0)
        return true;
    for (i=0; i<n; i++)
        if (g[now][i] && !viewed[i])
        {
            viewed[i] = true;
            if (find(match[i]))
            {
                match[i] = now;
                return true;
            }
        }
    return false;
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&ncase);
    for (t=1; t<=ncase; t++)
    {
        scanf("%d%d",&n,&k);
        for (i=0; i<n; i++)
            for (j=0; j<k; j++)
                scanf("%d",&p[i].a[j]);
        
        for (i=0; i<n; i++)
            for (j=0; j<n; j++)
                if (!cross(i,j) && p[i].a[0]<p[j].a[0])
                    g[i][j] = true;
                else
                    g[i][j] = false;
        for (i=0; i<=n; i++)
            match[i] = -1;
        sum = n;
        for (i=0; i<n; i++)
        {
            memset(viewed,0,sizeof(viewed));
            if (find(i))
                sum--;
        }
        printf("Case #%d: %d\n",t,sum);
    }
    return 0;
}
