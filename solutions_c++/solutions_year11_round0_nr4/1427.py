#include <iostream>
#include <string.h>
#include <stdio.h>
#include <stdio.h>
#define MAXN 10000
using namespace std;
int a[MAXN+10];
bool temp[MAXN+10];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        memset(temp,0,sizeof(temp));
        int n;
        cin>>n;
        double ans=0;
        for(int i=1;i<=n;i++) cin>>a[i];
        for(int i=1;i<=n;i++)
        {
            int l=0;
            int h=a[i];
            if(temp[i]) continue;
            if(a[i]==i)
            {
                temp[a[i]]=1;
                continue;
            }
            temp[a[i]]=1;
            while(1)
            {
                l++;
                h=a[h];
                if(temp[h]) break;
                if(h==a[h]) break;
                temp[h]=1;
            }
            ans+=l;
        }
        printf("Case #%d: %.6lf\n",k,ans);
    }
    return 0;
}
