#include <iostream>
#define size 100000

using namespace std;
int store[size],si,first;
void gcd(int a,int b)
{
    if(b==0)
        return;
    int num=a/b;/*
    if(a==b)
    {
        printf("LOSING\n");
        return;
    }
    else if(a==1&&b==1)
    {
        printf("LOSING\n");
        return;
    }
    else if(b==1)
    {
        printf("WINNING\n");
        return;
    }*/
    store[si]=num;
    if(num>1&&first==-1)
        first=si+1;
    si++;
    a=a%b;
    gcd(b,a);
}

bool solve(int a,int b)
{
    if(a<b)
    {
        return solve(b,a);
    }
    si=0;
    first=-1;
    gcd(a,b);
    if(first%2==1)
        return true;
    return false;
}

int main()
{
    int a1,a2,b1,b2,cnt=0,i,j,t,p;
    FILE *out;
    out=fopen("C-smallOut.out","w");
    scanf("%d",&t);
    for(p=0;p<t;p++)
    {
    scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
    cnt=0;
    for(i=a1;i<=a2;i++)
    {
        for(j=b1;j<=b2;j++)
        {
            if(solve(i,j))
                cnt++;
        }
    }
    fprintf(out,"Case #%d: %d\n",p+1,cnt);
    }
    fclose(out);
    return 0;
}

/*

(n,1) is winning n!=1
(n,n) is losing
*/



