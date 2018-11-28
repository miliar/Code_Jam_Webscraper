#include <stdio.h>
#include <math.h>
#include <iostream>
using namespace std;
long long n,k,test,m,t=0;
int main()
{
    freopen("a.txt","r",stdin);
    freopen("b.txt","w",stdout);
    cin>>test;
    while(test--)
    {
        cin>>n>>k;
        m=pow(2,n)-1;
        if(k==m || (k-m)%(m+1)==0)
            printf("Case #%lld: ON\n",++t);
        else
            printf("Case #%lld: OFF\n",++t);
    }
    return 0;
}


