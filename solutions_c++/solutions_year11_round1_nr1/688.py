#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;

int t;
long long n,d,g;


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("al1.txt","w",stdout);
    int i,j;
    scanf("%d",&t);
    int cnt=1;
    while(t--)
    {
        scanf("%lld %lld %lld",&n,&d,&g);
        printf("Case #%d: ",cnt++);
        if(d!=100&&g==100)
        {
            printf("Broken\n");
            continue;
        }
        if(d!=0&&g==0)
        {
            printf("Broken\n");
            continue;
        }
        if(d==0)
        {
            printf("Possible\n");
            continue;
        }
        long long t1,t2;
        if(d%2!=0)
            t1=1;
        if(d%4==2)
            t1=2;
        if(d%4==0)
            t1=4;
        if(d%5!=0)
            t2=1;
        if(d%5==0&&d%25!=0)
            t2=5;
        if(d%25==0)
            t2=25;
        long long x=t1*t2;
        x=100/x;
        if(n>=x)
            printf("Possible\n");
        else
            printf("Broken\n");
    }
    //system("pause");
    return 0;
}
