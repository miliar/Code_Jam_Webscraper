#include <iostream>
#include <cstdio>

using namespace std;

int score[110],high[110],ans,n,s,p;;
void dfs(int id,int cnt,int res)
{
    if(cnt>ans) ans=cnt;
    if(res==0) return ;
    for(int i=id;i<n;i++)
    {
        if(high[i]>=p) continue;
        if(score[i]==0&&high[i]==p-1) dfs(i+1,cnt+1,res-1);
        if(score[i]==2&&high[i]==p-1) dfs(i+1,cnt+1,res-1);
    }
}
int main()
{
    //freopen("B-small-attempt0.in","r",stdin);
    //freopen("B-small-attempt0.out","w",stdout);
    int ca,cas=1;
    cin>>ca;
    while(ca--)
    {
        cin>>n>>s>>p;
        ans=0;
        for(int i=0;i<n;i++)
        {
           cin>>score[i];
           if(score[i]==0)
            {
                score[i]=1;
                high[i]=0;
                if(p==0) ans++;
                continue;
            }
           if(score[i]%3==0)
           {
                high[i]=score[i]/3;
                score[i]=0;
           }
           else if(score[i]%3==1)
           {
               high[i]=score[i]/3+1;
               score[i]=1;
           }
           else
            {
               high[i]=score[i]/3+1;
               score[i]=2;
            }
           if(high[i]>=p) ans++;
        }
        cout<<"Case #"<<cas++<<": ";
        dfs(0,ans,s);
        cout<<ans<<endl;
    }
    return 0;
}
