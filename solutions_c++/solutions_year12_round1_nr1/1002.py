#include<stdio.h>
#include<string.h>
#include<fstream>
long long int t,i,j;
double p[200000];
double min1,a,b,m,p1;
using namespace std;
int main()
{
freopen("C:\\Users\\Sameer\\Desktop\\A-large.in","r",stdin);
freopen("C:\\Users\\Sameer\\Desktop\\output.out","w",stdout);
scanf("%lld",&t);
for(j=1;j<=t;j++)
{
    scanf("%lf%lf",&a,&b);
    for(i=1;i<=a;i++)
        scanf("%lf",&p[i]);
    min1=a+b+1;p1=1;
    for(i=1;i<=a;i++)
    {
        p1*=p[i];
        m=( a+b - i -i + 1 )*p1 + ( a+b -i -i +b+2)*(1-p1);
        if(m<min1)
            min1=m;
    }
    if(b+2<min1)
        min1=b+2;
    printf("Case #%lld: %.6lf\n",j,min1);
}
return 0;
}
