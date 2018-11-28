#include<stdio.h>
#include <iostream>
#define N 100
using namespace std;
int A[100];

int isValid(int a,int b,int c)//a<=b<=c
{
    if(a>=0&&c<=10)
        return 1;
    return 0;
}

int solve(int n,int s,int p)
{
    int i,mod,x,ans=0;

    for(i=0;i<n;i++)
    {
        mod=A[i]%3;
        x=A[i]/3;
        switch(mod)
        {
            case 0:
            if(isValid(x,x,x)&&x>=p)
                ans++;
            else if(isValid(x-1,x,x+1)&&x+1>=p&&s)
            {
                ans++;
                s--;
            }
            break;

            case 1:
            if(isValid(x,x,x+1)&&x+1>=p)
                ans++;
            break;

            case 2:
            if(isValid(x,x+1,x+1)&&x+1>=p)
                ans++;
            else if(isValid(x,x,x+2)&&x+2>=p&&s)
            {
                ans++;
                s--;
            }
            break;
        }
    }
    return ans;
}

int main()
{
    int t,n,s,p,i,caseNum=1;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    while(t>0)
    {
        scanf("%d%d%d",&n,&s,&p);
        for(i=0;i<n;i++)
            scanf("%d",&A[i]);
        printf("Case #%d: %d\n",caseNum,solve(n,s,p));
        caseNum++;
        t--;
    }
    return 0;
}
