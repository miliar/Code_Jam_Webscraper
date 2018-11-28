#include<iostream>
#include<algorithm>
using namespace std;
int s[40];
int main()
{
    freopen("in.in","r",stdin);
    freopen("A.txt","w",stdout);
    int t,cas=1;
    scanf("%d",&t);
    while(t--)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        memset(s,0,sizeof(s));
        int i=1;
        while(k)
        {
            s[i++]=k%2;
            k/=2;
        }
        bool f=1;
        for(int i=1;i<=n;i++)if(!s[i])f=0;
        if(f)printf("Case #%d: ON\n",cas++);
        else printf("Case #%d: OFF\n",cas++);
    }
    return 0;    
}
