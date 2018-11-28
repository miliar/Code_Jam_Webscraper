#include <iostream>
#include <map>
#include <set>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <time.h>
using namespace std;
const int N = 1005,INF = 1<<29;
const double eps = 1e-10;
const double pi = acos(1.);
int n,m;
double x[N],y[N],r[N];
double max(double a,double b){return a>b?a:b;}
double min(double a,double b){return a<b?a:b;}
double dist(int i,int j)
{
    return sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]));
}
int main()
{
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    int i,j,k;
    int T,K=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%lf%lf%lf",x+i,y+i,r+i);
        printf("Case #%d: ",K++);
        if(n==1)
        {
            printf("%lf\n",r[0]*1.);continue;
        }
        if(n==2)
        {
            printf("%lf\n",max(r[0],r[1]));
            continue;
        }
        if(n==3)
        {
            double mn = max((r[0]+r[1]+dist(0,1))/2.,r[2]);
            double tmp = max((r[1]+r[2]+dist(1,2))/2.,r[0]);
            mn = min(mn,tmp);
            tmp = max((r[0]+r[2]+dist(0,2))/2.,r[1]);
            mn = min(mn,tmp);
            printf("%lf\n",mn);
            continue;
        }
        puts("error");
    }
    return 0;
}
