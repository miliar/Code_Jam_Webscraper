#include<stdio.h>
#include<iostream>
#include<algorithm>

using namespace std;

long long r[1010],nx[1010],ans,s[1010],l[1010],cl,cw,tim;
int g[2010],cs[1005];
bool f[1005];

int main()
{
    int ks=1,t,R,k,n,i,j,cur,m;

    freopen("a.txt","r",stdin);
    freopen("out.txt","w",stdout);

    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d%d",&R,&k,&n);
        m = 2*n;
        for(i=0;i<n;i++)    scanf("%d",&g[i]);

        for(i=n,j=0;i<m;i++,j++)
        {
            g[i] = g[j];
            f[j] = false;
        }

        for(i=0;i<n;i++)
        {
            m = i+n;
            s[i] = 0;
            for(j=i;j<m;j++)
            {
                if(s[i]+g[j]<=k)
                {
                    s[i] +=g[j];
                    nx[i]=j+1;
                    if( nx[i] >= n )   nx[i] -=n;
                }
                else break;
            }
        }
        ans=0;
        cur=0;

        for(i=0;i<R;i++)
        {
            if(!f[cur])
            {
                f[cur] = true;
                ans += s[cur];
                r[cur] = ans;
                cs[cur] = i;
                cur = nx[cur];
            }
            else
            {
                ans += s[cur];
                cw = ans - r[cur];
                cl = i - cs[cur];
                tim = (R-i-1)/cl;
                ans += cw*tim;
                i +=tim*cl+1;
                cur = nx[cur];
                break;
            }

        }

        //Loop for extra
        //cout<<"ans:"<<ans<<endl;
        for(;i<R;i++)
        {
            ans += s[cur];
            cur = nx[cur];
        }

        printf("Case #%d: ",ks++);
        cout<<ans<<endl;
    }

    return 0;
}
