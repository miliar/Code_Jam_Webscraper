#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<set>
using namespace std;
int a[5];
int gcd(int x,int y)
{
    while(x!=0)
    {
        int t=x;
        x=y%x;
        y=t;
    }
    return y;
}
int main()
{
    int c;
    scanf("%d",&c);
    int cas;
    for(cas=1;cas<=c;cas++)
    {
        int n;
        scanf("%d",&n);
        int i,j;
        for(i=1;i<=n;i++)
            scanf("%d",&a[i]);
        sort(a+1,a+n+1);
        set<int> s1;
        for(i=1;i<n;i++)
                s1.insert(a[i+1]-a[i]);
        set<int>::iterator it;
        it=s1.begin();
        if(*it==0)
            ++it;
        int r=*it;
        for(++it;it!=s1.end();++it)
            r=gcd(r,*it);
        int res=a[1]%r;
        if(res!=0) res=r-res;
        printf("Case #%d: %d\n",cas,res);
    }
    return 0;
}
