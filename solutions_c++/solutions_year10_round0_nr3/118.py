#include <iostream>

using namespace std;

long long g[2000];
bool vis[2000];
long long lef,limit,n,key,j1,j2,ans;

int main()
{
    freopen("c-large.in","r",stdin);
    freopen("c.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int casenum=1;casenum<=T;casenum++)
    {
        printf("Case #%d: ",casenum);
        cin >> lef >> limit >> n;
        for (int i=0;i<n;i++) cin >> g[i];
        int st=0; memset(vis,0,sizeof(vis));
        while (!vis[st])
        {
            vis[st]=true; long long s=g[st],i=(st+1)%n;
            while (s+g[i]<=limit && i!=st)
            {
                s+=g[i],i=(i+1)%n;
            }
            st=i;
        }
        key=st; j1=0; j2=0;
        while (st!=key || j1==0)
        {
            j1++;
            vis[st]=true; long long s=g[st],i=(st+1)%n; j2+=g[st];
            while (s+g[i]<=limit && i!=st)
            {
                s+=g[i],j2+=g[i]; i=(i+1)%n; 
            }
            st=i;
        }       
        st=0; ans=0;
        while (lef>0 && st!=key)
        {
            lef--;
            vis[st]=true; long long s=g[st],i=(st+1)%n; ans+=g[st];
            while (s+g[i]<=limit && i!=st)
            {
                s+=g[i],ans+=g[i]; i=(i+1)%n; 
            }
            st=i;
        }
        ans+=j2*(lef/j1);
        lef=lef % j1; 
        while (lef>0)
        {
            lef--;
            vis[st]=true; long long s=g[st],i=(st+1)%n; ans+=g[st];
            while (s+g[i]<=limit && i!=st)
            {
                s+=g[i],ans+=g[i]; i=(i+1)%n; 
            }
            st=i;
        }
        cout << ans << endl;
    }
}
