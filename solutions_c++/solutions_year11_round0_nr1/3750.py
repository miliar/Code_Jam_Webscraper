#include<iostream>
#include<stdio.h>
using namespace std;

int i,j,t,k,n;
int o,b,target,step;
int ans;
char c[5];

int abs(int x,int y)
{
    if(x>y)
        return x-y;
    else
        return y-x;
}

void runB(int tar);
void runO(int tar)
{
    int temp;
    temp=max(abs(tar,o)-step,0)+1;
    o=tar;
    n--;
    while(n>0)
    {
        scanf("%s%d",c,&target);   
        if(c[0]=='O')
        {
            temp+=abs(target,o)+1;
            n--;
            o=target;
        }
        else
        {
            step=temp;
            ans+=temp;
            runB(target);
        }
    }
    if(n==0)
    {
        ans+=temp;
        n--;
    }
}

void runB(int tar)
{
    int temp;
    temp=max(abs(tar,b)-step,0)+1;
    b=tar;
    n--;
    while(n>0)
    {
        scanf("%s%d",c,&target);   
        if(c[0]=='B')
        {
            temp+=abs(target,b)+1;
            n--;
            b=target;
        }
        else
        {
            step=temp;
            ans+=temp;
            runO(target);
        }
    }
    if(n==0)
    {
        ans+=temp;
        n--;
    }
}

int main()
{
    freopen("A-large.in","r",stdin);freopen("A-large-out.out","w",stdout);
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d",&n);
        scanf("%s%d",c,&target);
        o=b=1;
        ans=0;
        step=0;
        if(c[0]=='B')
            runB(target);
        else
            runO(target);
        printf("Case #%d: %d\n",k,ans);
    }
    
    return 0;
}
