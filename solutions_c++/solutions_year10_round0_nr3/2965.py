#include<iostream>
#define LL long long
using namespace std;

LL G[1005];

int main()
{
    freopen("C:\\Users\\lenovo\\Desktop\\C.in","r",stdin);
    freopen("C:\\Users\\lenovo\\Desktop\\CC.out","w",stdout);
    int test,t=0;
    scanf("%d",&test);
    LL r,k,n;
    while(test--)
    {
        scanf("%lld%lld%lld",&r,&k,&n);
        for(int i=0; i<n; i++) scanf("%lld",G+i);
        LL unit=0,tmp=0,num=0,ans;
        int p=0,begin;
        bool done=false;
        while(1)
        {
            tmp=0;
            begin=p;
            while(tmp+G[p]<=k)
            {
                tmp+=G[p];
                p=(p+1)%n;
                if(begin==p) break;
            }num++;
            unit+=tmp;
            if(r==num)
            {
                break;
            }
        } 
        printf("Case #%d: ",++t);
        printf("%lld\n",unit);  
    }
}
