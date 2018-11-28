#include<iostream>
#include<algorithm>
#include<iomanip>
#include<cstring>
#include<string>
#include<cstdio>
#include<queue>
#include<map>
#include<set>
using namespace std;
int p(int x)
{
    int ans=1;
    for(int i=1;i<=x;i++)
    {
        ans*=10;
    }
    return ans;
}
int solve(int x,int a)
{
    int cur=x,k=0,j,z=0;
    while(cur!=0)
    {
        k++;
        cur/=10;
    }
    for(j=1;j<k;j++)
    {
        int ans=x%p(j)*p(k-j)+x/p(j);
        if(ans>=a&&ans<x)
        {
            z++;
        }
    }
    return z;
}
int main()
{
    int n,s;
    cin>>n;
    for(s=1;s<=n;s++)
    {
        int a,b,tmp=0;
        cin>>a>>b;
        for(int t=a;t<=b;t++)
        {
            tmp+=solve(t,a);
        }
        printf("Case #%d: %d\n",s,tmp);
    }
	return 0;
}
