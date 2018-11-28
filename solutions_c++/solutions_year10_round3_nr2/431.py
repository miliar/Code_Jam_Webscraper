#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
#define see(x) cout<<#x<<" "<<x<<endl
#define sp system("pause")
bool inter(int a1,int a2,int b1,int b2)
{
     if(a1>b1 && a2<b2)
         return true;
     if(a1<b1 && a2>b2)
         return true;
     return false;
}
int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    long long T,n,i,j;
    int ans;
    long long sum;
    long long L,P,C;
    cin>>T;
    for(int cas=1;cas<=T;cas++)
    {
        cin>>L>>P>>C;
        
        if(L*C>=P)
        {    
            printf("Case #%d: %d\n",cas,0);
            continue;
        }
        long long l=L;
        sum=0;
        while(l<P)
        {
            l*=C;
            sum++;
        }
        sum--;
        ans=0;
        
        while(sum)
        {
            //see(sum);
            //sp;
            if(sum%2==0)
            {
                sum/=2;
                ans++;
            }
            else
            {
                sum/=2;
                ans++;
            }
            if(sum==0)
                break;
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
