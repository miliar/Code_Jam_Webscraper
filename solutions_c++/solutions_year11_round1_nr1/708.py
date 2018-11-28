#include<cstdio>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
#include<cstring>
#include<map>
#include<cmath>
#include<iostream>
#define out(x) cout<<#x<<": "<<(x)<<endl;
using namespace std;


long long gcd(long long t1,long long t2)
{
     if(t2==0) return t1;
     return gcd(t2,t1%t2);
     
}

int main()
{
    int Case,T=1;
    long long num,pd,pg;
    freopen("A-large.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&Case);
    while(Case--)
    {
        scanf("%I64d%I64d%I64d",&num,&pd,&pg);
        //long long g1=gcd(100,pd);
        //long long g2=gcd(100,pg);
        //long long g3=gcd(g1,g2);
        //long long g4=g1*g2/g3;
        
        long long g5=100/gcd(100,pd);
        if(num<g5) {printf("Case #%d: Broken\n",T++);continue;}
        
        if(pg==100) if(pd!=100) {printf("Case #%d: Broken\n",T++);continue;}
        if(pg==0) if(pd!=0) {printf("Case #%d: Broken\n",T++);continue;}
        
        printf("Case #%d: Possible\n",T++);
    }
    return 0;
}

        
        
         
