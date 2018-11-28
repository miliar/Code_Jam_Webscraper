#include<vector>
#include<iostream>
#include<map>
#include<set>
#include<algorithm>
#include<stack>
#include<queue>
#include<string>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<list>

using namespace std;

#define Max 100

inline int dis(int x1, int y1, int x2, int y2)
{
    return((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

inline double max1(double x, double y)
{
    return(x > y ? x : y);
}

int main(int argc, char *argv[])
{
    freopen("E:/in.txt","r",stdin);
freopen("E:/out.txt","w",stdout);
    int t,o;
    scanf("%d",&t);
    for(o=1;o<=t;o++)
    {
        printf("Case #%d: ",o);
        int n,i,j,k;
        scanf("%d",&n);
        int x[Max],y[Max],r[Max];
        int maxr=0;
        for(i=1;i<=n;i++) 
        {
            scanf("%d%d%d",&x[i],&y[i],&r[i]);
            if(r[i] > maxr) maxr = r[i];
        }
        if(n==1)  printf("%.6f\n",r[1]*1.0);
        if(n==2)  printf("%.6f\n",1.0*(r[1]<r[2]? r[2] : r[1]));
        if(n==3)
        {
            double max = 108409080.0;
            for(i=1;i<=3;i++)
               for(j=1;j<=3;j++)
               {
                   if(i != j && max > (sqrt(dis(x[i],y[i],x[j],y[j])*1.0)+r[i]*1.0+r[j]*1.0)/2.0)
                      max = (sqrt(dis(x[i],y[i],x[j],y[j])*1.0)+r[i]*1.0+r[j]*1.0)/2.0;
               } 
            printf("%.6f\n",max);
        }
    }
    return EXIT_SUCCESS;
}
