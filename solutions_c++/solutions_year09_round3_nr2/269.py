#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <string.h>
#include <string>
#include <cmath>

#define PI 3.14159265358979
#define PB(x) push_back(x)
#define eps (1e-10)
using namespace std;
typedef long long LL;
void debug_array(int i,int j,int data[]){while (i<j){cout<<"     [ "<<i<<" ] : "<<data[i];i++;}cout<<endl;}


double sumx,sumxv;
double sumy,sumyv;
double sumz,sumzv;
int n;

    void inputing()
    {
        int i;
        scanf("%d",&n);
        double x,y,z,vx,vy,vz;
        sumx = sumxv =sumy = sumyv =sumz = sumzv = 0;
        for ( i=0;i<n;i++ )
        {
            scanf("%lf%lf%lf%lf%lf%lf",&x,&y,&z,&vx,&vy,&vz);
            sumx += x,sumxv += vx;
            sumy += y,sumyv += vy;
            sumz += z,sumzv += vz;
        }
    }

    void cal()
    {
        double t,d;
        double x,y,z;

        double temp =0;
        t = sumx * sumxv + sumy * sumyv + sumz * sumzv;
        temp = sumxv * sumxv + sumyv * sumyv + sumzv * sumzv;
//        printf(" t = %lf / %lf",t,temp);//debug
        if ( temp <= eps )
        t = 0;
        else t = (-t)/temp;
        if (t < 0)
        t = 0;
//        printf("t = %lf\n",t);//debug

        x = sumx + sumxv*t;
        y = sumy + sumyv*t;
        z = sumz + sumzv*t;
//        printf(" ( %lf , %lf , %lf )\n",x,y,z);//debug

        d = sqrt( x*x + y*y + z*z ) / (double)n;
        printf("%.8lf %.8lf\n",d,t);//debug
    }


int main()
{
//    freopen("inputing","r",stdin);
//    freopen("outputing","w",stdout);
    int cas;
    scanf("%d",&cas);
    for (int i=1;i<=cas;i++ )
    {
        inputing();
        printf("Case #%d: ",i);
        cal();
    }
    return 0;
}
