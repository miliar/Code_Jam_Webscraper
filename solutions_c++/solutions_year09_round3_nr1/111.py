#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>
#include <math.h>
using namespace std;
char s[100];
int L[100];
bool ok[1000];
int mark[1000];
int n,T,K;
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
  //cout<<(1LL<<63)-1<<endl;
    K = 1;
    scanf("%d",&T);
    int i,j,k;
    while(T--)
    {
        scanf("%s",&s);
        memset(ok,0,sizeof(ok));
        memset(mark,-1,sizeof(mark));
        n=strlen(s);
        for(i=0;i<n;i++)
            ok[s[i]]=1;
        int ct = 0;
        for(i=0;i<256;i++)
            if(ok[i])ct++;
        if(ct==1)ct++;
        int pt = 1;
        for(i=1;i<n;i++)
        {
            if(s[i]!=s[0])
            {
                mark[s[i]]=0;break;
            }
        }
        for(i=0;i<n;i++)
        {
            if(mark[s[i]]==-1)
            {
                mark[s[i]]=pt++;
            }
        }
        long long ans = 0;
        for(i=0;i<n;i++)
        {
            ans=ans*ct + mark[s[i]];
        }
        cout<<"Case #"<<K++<<": ";
        cout<<ans<<endl;
    }

    return 0;
}
