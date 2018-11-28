#include<iostream>
#include<cmath>
using namespace std;
__int64 num[501][7];
int main()
{
    int cases;
    int ca=0;
    scanf("%d",&cases);
    while(cases--)
    {
        ca++;
        int n;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
        for(int j=1;j<=6;j++)
        scanf("%I64d",&num[i][j]);
        __int64 a=0,b=0,c=0,d=0,e=0,f=0;
        for(int i=1;i<=n;i++)
        {
            b+=num[i][4];
            a+=num[i][1];
            c+=num[i][2];
            d+=num[i][5];
            e+=num[i][3];
            f+=num[i][6];
        }
        __int64 x=b*b+d*d+f*f,y=2*(a*b+c*d+e*f),z=a*a+c*c+e*e;
        printf("Case #%d:",ca);
        if(x==0)
        {
             if(y==0)
                     printf(" %.8lf 0.00000000\n",sqrt(((double)z)/(n*n)));
             else if(y>0)
                  printf(" %.8lf 0.00000000\n",sqrt(((double)z)/(n*n)));
             else
             {
                 double p=-1*z/y;
                 printf(" 0.00000000 %.8lf\n",p);
             }
        }
        else
        {
             double mid=-1.0*y/(2*x);
             if(mid<0)
                  printf(" %.8lf 0.00000000\n",sqrt(((double)z)/(n*n)));
             else
             {
                 double judge=y*y-4*x*z;
                 if(judge>0.00000000001||fabs(judge)<0.00000000001)
                 {
                      double x1=(-1*y-sqrt(judge))/(2*x);
                      double x2=(-1*y+sqrt(judge))/(2*x);
                      if(x1>0.00000000001||fabs(x1)<0.00000000001)
                           printf(" 0.00000000 %.8lf\n",x1);
                      else
                           printf(" 0.00000000 %.8lf\n",x2);
                 }
                 else
                 {
                      double low=(x*mid*mid+y*mid+z)/(n*n);
                      printf(" %.8lf %.8lf\n",sqrt(low),mid);
                 }
             }
        }
    }
}
        
