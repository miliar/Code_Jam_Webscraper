#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdlib>
using namespace std;

#define N 1010

int n,w,l;
int r[N],lab[N];
double x[N],y[N];


bool dfs(int p)
{
    if(p==n) return true;
    double x0,y0;
    for(int j=0;j<30;j++)
    {
        int fl=0;
        x0=(rand()*32767+rand())%w;
        x0+=0.1*(rand()%10);
        y0=(rand()*32767+rand())%l;
        y0+=0.1*(rand()%10);
        for(int i=0;i<p;i++)
        {
            if((x0-x[i])*(x0-x[i])+(y0-y[i])*(y0-y[i])<(double)(r[p]+r[i])*(r[p]+r[i]))
            {
                fl=1;
                break;
            }
        }
        if(!fl)
        {
            x[p]=x0;
            y[p]=y0;
            if(dfs(p+1))
                return true;
        }
    }
    return false;
}

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=0;cas<t;cas++)
    {

        scanf("%d%d%d",&n,&w,&l);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&r[i]);
            lab[i]=i;
        }
        for(int i=0;i<n;i++)
            for(int j=i+1;j<n;j++)
                if(r[i]<r[j])
                {
                    swap(r[i],r[j]);
                    swap(lab[i],lab[j]);
                }
        if(!dfs(0)) puts("F");
        for(int i=0;i<n;i++)
            for(int j=i+1;j<n;j++)
            if(lab[i]>lab[j])
            {
                swap(lab[i],lab[j]);
                swap(x[i],x[j]);
                swap(y[i],y[j]);
            }
        printf("Case #%d:",cas+1);
        for(int i=0;i<n;i++)
            printf(" %.1lf %.1lf",x[i],y[i]);
        puts("");

    }
    return 0;

}
