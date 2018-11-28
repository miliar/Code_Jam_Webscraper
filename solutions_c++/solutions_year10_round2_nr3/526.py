#include<cstdio>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
#include<cmath>
#include<iostream>
#define out(x) cout<<#x<<": "<<(x)<<endl;
using namespace std;

int mark[26];
int ans;
int n;

int check()
{
    int temp=n;
    int cnt;
    int i;
    while(temp!=1)
    {
        cnt=1;
        for(i=2;i<temp;i++) if(mark[i]) cnt++;
        
        if(cnt==0) return 0;
        if(cnt==1) return 1;
        if(mark[cnt]!=1) return 0;
        else temp=cnt;
    }
    
    return 1;
}
        

void gene(int now)
{
    if(now==n)
    {
        if(check()) 
        {
            ans++;
            ans%=100003;
        }
        return;
    }
    gene(now+1);
    mark[now]=1;
    gene(now+1);
    mark[now]=0;
}

int main()
{
    int t,T=1;
    freopen("C-small-attempt2.in","r",stdin);
    freopen("C.txt","w",stdout);
    int tt[26];
   
    for(int i=2;i<=25;i++)
    {
        ans=0;
        n=i;
        gene(2);
        tt[i]=ans;
    }
    
    
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        
        printf("Case #%d: %d\n",T++,tt[n]);
    }
    return 0;
} 
