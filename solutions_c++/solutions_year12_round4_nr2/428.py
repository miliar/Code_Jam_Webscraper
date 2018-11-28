#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
#define pi (2*acos(0))
#define ll long long int
#define pii pair<int,int>

using namespace std;

struct s{
    int r,id,ax,ay;
}cc[1005];

bool mys(s x,s y)
{
    return (x.r> y.r);
}

bool myid(s x,s y)
{
    return (x.id< y.id);
}

int r[1005],n,w,l,ax[1005],ay[1005];

double dist(double x1,double y1,double x2,double y2)
{
    return sqrt( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) );
}

bool check()
{
    int i,j,k;

    for(i=1;i<=n;i++)
    {
        if(cc[i].ax >w || cc[i].ay > l) return 0;
        for(j=i+1;j<=n;j++)
        {
            if(dist(cc[i].ax,cc[i].ay,cc[j].ax,cc[j].ay) < cc[i].r+cc[j].r) return 0;

        }
    }

    return 1;
}

int main()
{
    int i,j,k,t,T,r,nwx,nwr;

    freopen("B-large(2).in","r",stdin);
    freopen("bout.txt","w",stdout);

    scanf("%d",&T);

    for(t=1;t<=T;t++)
    {
        scanf("%d %d %d",&n,&w,&l);

        for(i=1;i<=n;i++)
        {
            scanf("%d",&cc[i].r);

            cc[i].id=i;
        }

        sort(cc+1,cc+1+n,mys);

        for(i=1;i<=n;i++)
        {
            if(i==1)
            {
                nwx=0;
                nwr=cc[i].r;
                cc[i].ax=0;
                cc[i].ay=0;
               // cout<<" -- " << cc[i].ax << " " <<cc[i].ay<<endl;
                continue;
            }

            if(cc[i-1].ay + cc[i-1].r + cc[i].r <=l)
            {
                cc[i].ay=cc[i-1].ay + cc[i-1].r + cc[i].r;
                cc[i].ax=cc[i-1].ax;
            }

            else
            {
                cc[i].ay=0;
                cc[i].ax=nwx+nwr+cc[i].r;
                nwx=cc[i].ax;
                nwr=cc[i].r;
            }

           // cout<<" -- " << cc[i].ax << " " <<cc[i].ay<<endl;
        }

        sort(cc+1,cc+1+n,myid);

        //printf("%s\n",check() ? "YES" : "NO");

        printf("Case #%d:",t);

        for(i=1;i<=n;i++) printf(" %d %d",cc[i].ax,cc[i].ay);

        printf("\n");
    }
    return 0;
}
