#include<iostream>
#include<cmath>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;

#define llong __int64
const int maxn = 1000;
int T;

llong L,P,C,base[100];

llong get(llong n)
{
    llong ret=1,t=C;
    while(n)
    {
        if( n%2 )ret = ret* t;
        t = t*t;
        n/=2;
    }
    return ret;
}

int main(){    
    freopen("B-Large.in","r",stdin);
    freopen("B-Large.out","w",stdout);
    int i,j,k;
    cin>>T;
    base[0]=1;
    for(i=1;i<=40;i++)base[i]=base[i-1]*2;

    for(int ca=1;ca<=T;ca++)
    {
        scanf("%I64d%I64d%I64d",&L,&P,&C);
        int n;
        for(n=0;n<=50;n++)
        {
            if( ( L*get( base[n] ) )>=P )break;
        }
        printf("Case #%d: %d\n",ca,n);
    }
    
}

