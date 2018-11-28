#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string.h>
using namespace std;

int n,k;

int cache[1<<16];
int vl[1<<16];

int vv[17][17];

vector<int> inp[110];

bool valid(int i, int j)
{
    if(vv[i][j]!=-1)
        return vv[i][j];
    for(int x=0;x<k;x++)
        if(inp[i][x]>=inp[j][x])
            return vv[i][j]=false;
    return vv[i][j]=true;
}

bool valid( int msk)
{
    if(vl[msk]!=-1)
        return vl[msk];

    for(int i=0;i<n;i++)
        if(msk & (1<<i))
            for(int j=i+1;j<n;j++)
                if(msk & (1<<j))
                    if(!valid(i,j))
                        return vl[msk]=false;
    return vl[msk]=true;
}

int minw(int msk)
{
    if(!msk)
        return 0;
    if(cache[msk]!=-1)
        return cache[msk];
    cache[msk]=n;
    
    int nmsk=msk;
    while(nmsk)
    {
        if(valid(nmsk))
        {
            if(cache[msk]>minw(msk^nmsk)+1)
                cache[msk]=minw(msk^nmsk)+1;
        }
        nmsk--;
        nmsk&=msk;
    }
    return cache[msk];

}

int main()
{
    freopen("C1.in","r",stdin);
    freopen("C1.out","w",stdout);
    int t,i,j,a;
    scanf("%d",&t);
    for(int cs=1;cs<=t;cs++)
    {
        scanf("%d%d",&n,&k);
        for(i=0;i<n;i++)
        {
            inp[i].clear();
            for(j=0;j<k;j++)
            {
                scanf("%d",&a);
                inp[i].push_back(a);
            }
        }
        memset(cache,-1,sizeof(cache));
        memset(vl,-1,sizeof(vl));
        memset(vv,-1,sizeof(vv));
        sort(inp,inp+n);
        int ans=minw((1<<n)-1);
        printf("Case #%d: %d\n",cs,ans);
        if(cs%10==0)
            fprintf(stderr,"Done Case %d\n",cs);
    }
    return 0;
}
