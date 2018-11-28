#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
int n;
int a[1009];
void init()
{
    scanf("%d",&n);
    int sum=0;
    int k=0;
    int Min=1000009;
    for(int i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
        {
            sum+=a[i];
            k=k^a[i];
        }
        if(a[i]<Min)
        Min=a[i];
    }

    if(k!=0)
    printf("NO\n");
    else
    printf("%d\n",sum-Min);
}
int main()
{

    int Case;
     freopen("E:\\aa.out","w",stdout);
    scanf("%d",&Case);
    for(int i=1;i<=Case;i++)
    {
        printf("Case #%d: ",i);
        init();
    }
return 0;
}
