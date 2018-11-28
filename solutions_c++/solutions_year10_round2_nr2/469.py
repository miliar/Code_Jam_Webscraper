#include<cstdio>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
#include<cmath>
#include<iostream>
#define out(x) cout<<#x<<": "<<(x)<<endl;
using namespace std;

const double eps=1e-9;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B.txt","w",stdout);
    int cases,T=1,i,n,k,b,t,ans,cnt;
    int a[200],v[200];
    scanf("%d",&cases);
    while(cases--)
    {
        scanf("%d%d%d%d",&n,&k,&b,&t);
        
        for(i=0;i<n;i++) scanf("%d",&a[i]);
        for(i=0;i<n;i++) scanf("%d",&v[i]);
        
        ans=0;
        cnt=0;
        for(i=n-1;i>=0;i--)
        {
            if((b-a[i])*1.0/v[i]>t+eps) cnt++;
            else 
            {
                k--;
                ans+=cnt;
                if(k==0) break;
            }
        }
        
        if(k!=0) printf("Case #%d: IMPOSSIBLE\n",T++);
        else printf("Case #%d: %d\n",T++,ans);
    }
    return 0;
}
            
            
