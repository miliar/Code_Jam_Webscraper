#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string.h>
#include <algorithm>
#define maxn 100
using namespace std;
int a[maxn+10];
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int cas,n,s,p,k,i;
    while(scanf("%d",&cas)!=EOF)
    {
        for(int kk=1; kk<=cas; kk++)
        {
            scanf("%d%d%d",&n,&s,&p);
            printf("Case #%d: ",kk);
            memset(a,0,sizeof(a));
            for(i=1; i<=n; i++)
            {
                scanf("%d",&a[i]);
            }
            sort(a+1,a+1+n);
            int t,ans=0;
            t=3*p;
            for(i=n; i>=1; i--)
            {
                if(a[i]<t)
                {
                // printf("a[%d]= %d,t=%d \n",i,a[i],t);
                     ans=n-i;
                     break;
                }
            }
            if(i==0)
            {
                printf("%d\n",n);
                continue;
            }
            //cout<<ans<<endl;
            for(k=i; k>=1; k--)
            {
                int stmp=s;
                int tmp=a[k]/3;
                if(s==0)
                {
                    if(a[k]%3==1)
                    {
                        if(tmp+1>=p)ans++;
                    }
                    else if(a[k]%3==2)
                    {
                        if(tmp+1>=p)ans++;
                    }
                }
                else
                {
                    if(a[k]%3==0)
                    {
                        if(a[k]==0)
                        {
                            if(p==0)ans++;
                        }
                        else if(tmp+1>=p)
                        {
                            s--;
                            ans++;
                        }
                    }
                    else if(a[k]%3==1)
                    {
                        if(tmp+1>=p)ans++;
                    }
                    else if(a[k]%3==2)
                    {
                        if(tmp+1>=p)ans++;
                        else if(tmp+2>=p)
                        {
                            ans++;
                            s--;
                        }
                    }
                }
//                if(stmp==s+1)
//                {
//                    cout<<"k= "<<k<<endl;
//                }
            }
            printf("%d\n",ans);
        }
    }
    return 0;
}
