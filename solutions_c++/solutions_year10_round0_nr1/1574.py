#include<iostream>
#include<algorithm>
using namespace std;


int main(void)
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T;
    scanf("%d",&T);
    int CAS=1;
    while(T--)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        int b[50];
        for(int i=0;i<35;i++)
            b[i]=0;
        int m=0;
        while(k)
        {
           b[m++]=k%2;
           k/=2;
        }
        printf("Case #%d: ",CAS++);
        int ans=1;
        for(int i=0;i<n;i++)
            ans&=b[i];
        if(ans)
            printf("ON\n");
        else
            printf("OFF\n");
    }
    return 0;
}
