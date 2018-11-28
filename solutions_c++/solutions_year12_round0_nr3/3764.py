#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;

int mt[2000005];
int shi[]= {1,10,100,1000,10000,100000,1000000,10000000};
int len(int a)
{
    int r=0;
    while(a>0)
    {
        r++;
        a/=10;
    }
    return r;
}
int a,b;
vector<int>h;
int trans(int n)
{
    h.clear();
    int t=len(n);
    int ans=0;
    for(int i=1; i<t; i++)
    {
        int tmp=n/shi[i]+shi[t-i]*(n%shi[i]);
        //printf("%d %d\n",n,tmp);
        if(len(tmp)==t&&tmp>n&&tmp<=b&&tmp>=a)
            {
                h.push_back(tmp);
            }
    }
    sort(h.begin(),h.end());
    t=0;
    for(int i=0;i<h.size();i++)
    {
        int tmp=h[i];
        if(mt[tmp]==1&&tmp!=t)
        {
            ans++;
        }
        t=tmp;
    }
    return ans;
}
int main()
{
    freopen("c.in","r",stdin);
    freopen("ans.txt","w",stdout);
    int n;
    scanf("%d",&n);
    int res;
    for(int C=1; C<=n; C++)
    {
        memset(mt,0,sizeof(mt));
        res=0;
        scanf("%d%d",&a,&b);
        for(int i=b; i>=a; i--)
        {
            res+=trans(i);
            mt[i]=1;
        }
        printf("Case #%d: %d\n",C,res);
    }

    return 0;
}
