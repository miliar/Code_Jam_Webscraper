#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
double p[100000];
#define l 1e-10;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
	freopen("out.out","w",stdout);
    int T;
    cin>>T;
    for(int i=0;i<T;i++)
    {
        int A,B;
        cin>>A>>B;
        int j;
        double ans,temple;
        double k=1;
        for(int j=0;j<A;j++)
        {
            cin>>p[j];
            k*=p[j];
        }
        ans=(B-A+1)*k+(2*B-A+2)*(1-k);
        if((B+2)-ans<1e-10) ans=B+2;
        for(int j=A-1;j>0;j--)
        {
            k=k/p[j];
            temple=(B-A+2*(A-j)+1)*k+(2*B-A+2*(A-j)+2)*(1-k);
            if(temple-ans<1e-10) ans=temple;
        }
        printf("Case #%d: %.6f\n",i+1,ans);
    }
return 0;
}
