#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

double p[100000];

int main()
{
    int t,i,j,a,b,c;
    double res,m;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
                    m=1;
                    scanf("%d %d",&a,&b);
                    for(j=0;j<a;j++)
                    {
                                    scanf("%lf",&p[j]);
                                    m*=p[j];
                    }
                    res=m*(b-a+1)+(1-m)*(b-a+1+b+1);
                    c=b-a+1;
                    for(j=a-1;j>=0;j--)
                    {
                                       m/=p[j];
                                       c+=2;
                                    res=min(res,m*c+(1-m)*(c+b+1));
                    }
                    res=min(res,double(b+2));
                    printf("Case #%d: %0.6f\n",i,res);
    }
}
