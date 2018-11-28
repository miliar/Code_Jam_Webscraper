#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<vector>
using namespace std;
#define rep(i,n) for(i=0;i<n;i++)
#define FOR(i,j,k) for(i=j;i<=k;i++)
#define FORD(i,j,k) for(i=j;i>=k;i--)
#define met(i,j) memset(i,j,sizeof(i))
#define PB push_back
#define sz size()
#define oo 0x7fffffff
#define Abs(a) (a>0?a:-(a))
typedef long long LL;
typedef unsigned long long ULL;

int main()
{
    freopen("sr.in","r",stdin);
    freopen("sc.out","w",stdout);
    int k,i,T,ans,fs,n,s,p,a[4];
    scanf("%d",&T);
    FOR(k,1,T)
    {
        printf("Case #%d: ",k);
        scanf("%d%d%d",&n,&s,&p);
        ans=0;
        FOR(i,1,n)
        {
            scanf("%d",&fs);
            a[1]=a[2]=a[3]=fs/3;
            if(fs%3==0)
            {
                if(a[1]>=p)
                {
                    ans++;
                }else
                {
                    if(a[1]+1>=p&&s&&a[1]-1>=0)
                    {
                        s--;
                        ans++;
                    }
                }
            }else
            {
                if(fs%3==1)
                {
                    if(a[1]+1>=p)ans++;
                }else
                {
                    if(fs%3==2)
                    {
                        if(a[1]+1>=p)
                        {
                            ans++;
                        }else
                        {
                            if(a[1]+2>=p&&s)
                            {
                                s--;
                                ans++;
                            }
                        }
                    }
                }
            }
        }
        cout<<ans<<endl;
    }
}
