#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

int main()
{
    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);
    int t;
    int a[10000];
    int n,l,h;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        scanf("%d%d%d",&n,&l,&h);
        for(int i=0;i<n;i++)
            scanf("%d",&a[i]);
        int res=-1;
        for(int i=l;i<=h;i++)
        {
            int j;
            for(j=0;j<n;j++)
            {
                if(i%a[j]!=0&&a[j]%i!=0)
                break;
            }
            if(j==n)
            {
                res=i;
                break;
            }
        }

        if(res==-1)
            printf("Case #%d: NO\n",i+1);
        else
            printf("Case #%d: %d\n",i+1,res);
    }
    return 0;
}
