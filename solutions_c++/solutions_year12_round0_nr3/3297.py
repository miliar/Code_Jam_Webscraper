#include <iostream>
#include <stdio.h>
using namespace std;

int a,b;
int n;
int ans,ans2;

int d(int x)
{
    int ret=1;
    while(x/10)
    {
        x/=10;
        ret++;
    }
    return ret;
}

int rot(int x,int d)
{
    int mask=1;
    d--;
    if(d) while(d--) mask*=10;
    return x/mask+(x%mask)*10;
}


void calc(int x)
{
    int n=d(x);
    int orix=x;
    for(int i=0;i<n;i++)
    {
        int t=rot(x,n);
        if(d(t)==n&&t>=a&&t<=b)
        {
            if(t>orix) ans++;
        }
        x=t;
    }
}



int main()
{
    //freopen("out.txt","w",stdout);
    scanf("%d",&n);
    int casno=1;
    while(n--)
    {
        scanf("%d%d",&a,&b);
        ans=ans2=0;
        for(int i=a;i<=b;i++) calc(i);
        //cout<<ans<<endl;
        printf("Case #%d: %d\n",casno++,ans);
    }
}
