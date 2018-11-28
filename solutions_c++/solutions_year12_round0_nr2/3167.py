#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<map>
#include<set>
#include<queue>
#include<string>
#include<vector>
#include<ctime>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large-out.out","w",stdout);
    int t,tt=0,n,s,p,a[105],b[105],c[105],i,cnt;
    scanf("%d",&t);
    while(t--)
    {
        tt++;
        cnt=0;
        scanf("%d%d%d",&n,&s,&p);
        for(i=0;i<n;i++)
        {
            scanf("%d",a+i);
            if(a[i]%3==0)
            {
                b[i]=a[i]/3;
                if(a[i]!=0 && a[i]!=30)c[i]=a[i]/3+1;
                else c[i]=-1;
            }
            else if(a[i]%3==1)
            {
                b[i]=a[i]/3+1;
                c[i]=-1;
            }
            else
            {
                b[i]=a[i]/3+1;
                if(c[i]!=29)c[i]=a[i]/3+2;
                else c[i]=-1;
            }
        }
        for(i=0;i<n;i++)
        {
            if(b[i]>=p)cnt++;
            else if(b[i]<p && c[i]>=p && s)
            {
                s--;
                cnt++;
            }
        }
        printf("Case #%d: %d\n",tt,cnt);
    }
    return 0;
}
