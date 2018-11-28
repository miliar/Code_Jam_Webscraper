#include<iostream>
#include<stdio.h>
using namespace std;

int i,j,k,t,pd,pg;
__int64 n;

bool judge()
{
    if(pd!=100 && pg==100)
        return false;
    if(pd!=0 && pg==0)
        return false;
    if(pd==0 || pd==100)
        return true;
    if(n>=100)
        return true;
    if(n>=50)
        if(pd%5!=0 && pd%2!=0)
            return false;
        else
            return true;
    if(n>=25)
        if(pd%4!=0 && pd%5!=0)
            return false;
        else
            return true;
    if(n>=20)
        if(pd%5!=0)
            return false;
        else  
            return true;
    if(n>=10)
        if(pd%10!=0 && pd%25!=0)
            return false;
        else  
            return true; 
    if(n>=5)
        if(pd%20!=0 && pd%25!=0)
            return false;
        else  
            return true;
    if(n>=4)
        if(pd%25!=0)
            return false;
        else  
            return true;
    if(n>=2)
        if(pd%50!=0)
            return false;
        else  
            return true;
    if(n>=1)
        if(pd%100!=0)
            return false;
        else  
            return true;
}

int main()
{
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%I64d%d%d",&n,&pd,&pg);
        if(judge())
            printf("Case #%d: Possible\n",k);
        else
            printf("Case #%d: Broken\n",k);
           
    }
    
    return 0;
}
