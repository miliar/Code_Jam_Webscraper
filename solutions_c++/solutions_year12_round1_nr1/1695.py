#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

const int maxn=10000;

double p[maxn+10];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int A,B,T;
    double ans,f;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        scanf("%d%d",&A,&B);
        for(int i=0;i<A;i++) scanf("%lf",&p[i]);
        ans=B+2;
        f=1;
        for(int i=0;i<A;i++)
        {
            f*=p[i];
            ans=min(ans,f*((A-i-1)*2+B-A+1)+(1-f)*((A-i-1)*2+B-A+1+B+1));
        }
        printf("Case #%d: %.6f\n",t,ans);
    }
    return 0;
}
