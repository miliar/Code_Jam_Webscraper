#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;
unsigned long long gcd(long long a=0ll, long long b=0ll)
{
    unsigned long long t=0ll;
    while (b != 0)
    {
       t = b;
       b = a % b;
       a = t;
    }
    return a;
}
int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int t,cases=1;
    scanf("%d",&t);
    while(t-- > 0)
    {
        int n,i;
        unsigned long long temp=0ull,a=0ull,b=0ull,c=0ull,num1=0ull,num2=0ull;
        scanf("%d",&n);
        vector <unsigned long long> aa;
        for(i=0;i<n;i++)
        {
            scanf("%lld",&temp);
            aa.push_back(temp);   
        }
        sort(aa.begin(),aa.end());
        if(n==3){
        num1 = aa[1]-aa[0];
        num2 = aa[2]-aa[1];
        
            
        a=gcd(num1,num2);
        i=2;
        b=a;
        if(b==1)
        {
            printf("Case #%d: %lld\n",cases++,0);
            continue;
        }
        while(b<aa[2])
        {
            b=a*i;
            i++;
        }
        printf("Case #%d: %lld\n",cases++,b-aa[2]);
        }
        else
        {
            i=2;
            num1=aa[1]-aa[0];
            b=num1;
            
            while(b<aa[1])
            {
                b=num1*i;
                i++;
            }
            printf("Case #%d: %lld\n",cases++,b-aa[1]);
        }
    }
    return 0;
}
        
            
            
        

