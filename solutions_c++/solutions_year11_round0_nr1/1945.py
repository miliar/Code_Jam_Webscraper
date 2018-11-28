#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
#define abs(x)  ((x)>0?(x):-(x))
const int MAXN=105;
int T,n;
char robot[MAXN];
int dis[MAXN];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("data.out","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;cas++)
    {
        int i,j;
        cin>>n;
        for(i=1;i<=n;i++)
            cin>>robot[i]>>dis[i];
        int s1=1,s2=1,t1=0,t2=0,ans=0;
        for(i=1;i<=n;i++)
        {
            if(robot[i]=='O')
            {
                int temp=abs(dis[i]-s1);
                if(t1>=temp) 
                {
                    ans++;
                    t2++;
                }
                else 
                {
                    ans+=temp-t1+1;
                    t2+=temp-t1+1;
                }
                t1=0;
                s1=dis[i];
            }
            else 
            {
                int temp=abs(dis[i]-s2);
                if(t2>=temp) 
                {
                    ans++;
                    t1++;
                }
                else
                {
                    ans+=temp-t2+1;
                    t1+=temp-t2+1;
                }
                t2=0;
                s2=dis[i];
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
            
        
