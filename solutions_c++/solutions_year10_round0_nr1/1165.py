#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
using namespace std;

int main()
{
    int t,cs,n,k,i,f[31]={0,1};
    freopen("C:\\Users\\LL\\Desktop\\A-small-attempt0.in","r",stdin);
    freopen("C:\\Users\\LL\\Desktop\\1.out","w",stdout);
    scanf("%d",&t);
    for(i=2;i<=30;i++)
        f[i]=f[i-1]*2+1;
    for(cs=1;cs<=t;cs++)
    {
        scanf("%d%d",&n,&k);
        printf("Case #%d: ",cs);
        if(k%(f[n]+1)==f[n])
            printf("ON\n");
        else
            printf("OFF\n");
    }
}