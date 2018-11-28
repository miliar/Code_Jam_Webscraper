#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
using namespace std;
int n,w,l;
int r[1111];
int T;
int casno=1;
double x[1111],y[1111];

double rdouble(double _max)
{
    return (rand()%30000/30000.0)*_max;
}
void genans()
{
    for(int i=0;i<n;i++) x[i]=rdouble(w),y[i]=rdouble(l);
}
double dis(double x1,double y1,double x2,double y2)
{
    return sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
}



bool check()
{
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++) if(j!=i)
        {
            if(dis(x[i],y[i],x[j],y[j])<r[i]+r[j]) return false;
        }
        return true;
}

int main()
{
    freopen("out.txt","w",stdout);
    srand(time(0));
    cin>>T;
    while(T--)
    {
        cin>>n>>w>>l;
        for(int i=0;i<n;i++) cin>>r[i];
        genans();
        while(!check()) genans();
        printf("Case #%d:",casno++);
        for(int i=0;i<n;i++) printf(" %lf %lf",x[i],y[i]);
        printf("\n");
    }

}
