#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<vector>
#include<string>
#include<string.h>
#include<math.h>
#include<queue>
#define h 1000000000

using namespace std;

int t,n,i,j,k,x[99],y[99],r[99],Q,d;
double rmin,cur;
vector<int> v[2];

double dist(double x1,double y1,double x2,double y2)
{
    return sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
}

main()
{
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    scanf("%d",&t);
    for(Q=1;Q<=t;Q++)
    {
        scanf("%d",&n);
        d=1<<n;
        for(i=0;i<n;i++)
            scanf("%d%d%d",&x[i],&y[i],&r[i]);
        rmin=h;
        for(i=0;i<d;i++)
        {
            v[0].clear(); v[1].clear();
            for(j=0;j<n;j++)
                if((i | (1<<j)) == i)
                    v[0].push_back(j);
                else
                    v[1].push_back(j);
            cur=0;
            for(j=0;j<v[0].size();j++)
                for(k=j;k<v[0].size();k++)
                    if(dist(x[v[0][j]],y[v[0][j]],x[v[0][k]],y[v[0][k]])+r[v[0][j]]+r[v[0][k]]>cur)
                        cur=dist(x[v[0][j]],y[v[0][j]],x[v[0][k]],y[v[0][k]])+r[v[0][j]]+r[v[0][k]];
            for(j=0;j<v[1].size();j++)
                for(k=j;k<v[1].size();k++)
                    if(dist(x[v[1][j]],y[v[1][j]],x[v[1][k]],y[v[1][k]])+r[v[1][j]]+r[v[1][k]]>cur)
                        cur=dist(x[v[1][j]],y[v[1][j]],x[v[1][k]],y[v[1][k]])+r[v[1][j]]+r[v[1][k]];
            cur/=2.0;
            if(cur<rmin) rmin=cur;
        }
        printf("Case #%d: %.6f\n",Q,rmin);
    }
}
