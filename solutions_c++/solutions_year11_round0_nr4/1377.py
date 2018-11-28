#include<iostream>

using namespace std;

double ans[1100];
void f(void)
{
    double d[1100];
    d[1]=0;
    d[2]=0.5;
    ans[1]=0.0;
    ans[2]=2.0;
    ans[3]=3.0;
    for(int i=4;i<=1000;i++){
        ans[i]=ans[i/2]+ans[i-i/2];
    }
}

void deal(void)
{
    int n,a,s=0;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%d",&a);
        if(a!=i)
            s++;
    }
    printf("%lf\n",ans[s]);
}

int main(void)
{
    f();
    int num=0;
    scanf("%d",&num);
    for(int i=1;i<=num;i++){
        printf("Case #%d: ",i);
        deal();
    }
    return 0;
}
/* vim: set expandtab ts=4 sw=4 sts=4 tw=100: */
