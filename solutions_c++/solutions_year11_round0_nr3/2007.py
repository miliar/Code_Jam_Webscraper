#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;

int a[1000100];

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;
    int cs=0;
    int n;
    int i,j;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        int s=0,x=0;
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            x^=a[i];
            s+=a[i];
        }
        if(x) printf("Case #%d: NO\n",++cs);
        else
        {
            sort(a,a+n);
            printf("Case #%d: %d\n",++cs,s-a[0]);
        }
    }
    return 0;
}


