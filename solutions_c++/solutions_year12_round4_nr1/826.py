#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
int n,T;
long long a[11111],b[11111],h[11111],d;
long long can[11111];
long long ml;



void glide(int x)
{
    ml=max(ml,a[x]+h[x]);
    for(int i=x+1;i<n;i++)
    {
        if(a[i]<=ml)
        {
            can[i]=true;
            long long dis=a[i]-a[x];
            h[i]=max(h[i],min(dis,b[i]));
        }
    }
}

int main()
{
    freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
    cin>>T;
    int casno=1;
    while(T--)
    {
        cin>>n;
        for(int i=0;i<n;i++) cin>>a[i]>>b[i];
        cin>>d;
        ml=0;
        memset(can,0,sizeof(can));
        memset(h,0,sizeof(h));
        can[0]=1;
        h[0]=a[0];
        for(int i=0;i<n;i++)
        {
            if(can[i]) glide(i);
        }
        printf("Case #%d: %s\n",casno++,ml>=d?"YES":"NO");
    }
}
