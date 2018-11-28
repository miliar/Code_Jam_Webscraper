#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int tmp=0,v[2000010],cnt;
void ini(int beg,int end)
{
    memset(v,0,sizeof(v));
    int i;
    for(i=beg;i<=end;++i)
    {
        if(i<10) continue;
        int x=i,y=i,z=i;
        int d=-1,D=1;
        if(v[i]) continue;
        while(y)
        {
            d++;
            y/=10;
        }
        while(d--)
        {
            D*=10;
        }
        v[x]=true;
        y=x%10;
        x/=10;
        tmp=1;
        while(1)
        {
            x=x+y*D;
            if(x==z) break;
            if(x>=beg&&x<=end&&x>=10)
            {
                tmp++;
                v[x]=true;
            }

            y=x%10;
            x/=10;
        }
        cnt+=tmp*(tmp-1)/2;
        //cout<<cnt<<" ";
    }
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C_ans.out","w",stdout);
    int t,i,n,m;
    scanf("%d",&t);
    for(i=1;i<=t;++i)
    {
        scanf("%d%d",&n,&m);
        cnt=0;
        ini(n,m);
        printf("Case #%d: %d\n",i,cnt);
    }
    return 0;
}
