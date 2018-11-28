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

int num[10000];

int main()
{
    int T,CASE=1;
    int n,i,res,sum,mark;
    
    freopen("C-large.in","r",stdin);
    freopen("1.out","w",stdout);
    
    
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        res=0x7fffffff;
        sum=0;
        for(i=0;i<n;i++) 
        {
            scanf("%d",&num[i]);
            res=min(res,num[i]);
            sum+=num[i];
        }
        
        mark=0;
        for(i=0;i<n;i++) mark^=num[i];
        
        if(mark) printf("Case #%d: NO\n",CASE++);
        else
        {
            printf("Case #%d: %d\n",CASE++,sum-res);
        }
    }
    return 0;
}
