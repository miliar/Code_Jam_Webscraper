#include<cstdio>
#include<cstring>
typedef long long ll;
int use[2000010];
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("c.txt","w",stdout);
    int ti;
    scanf("%d",&ti);
    for(int ca=1;ca<=ti;ca++)
    {
        memset(use,0,sizeof(use));
        int a,b;
        scanf("%d%d",&a,&b);
        int lll=1,l=1;
        while(a/(lll*10))
        {
            lll*=10;
            l++;
        }
        for(int i=a;i<=b;i++)
        {
            int min=i;
            int tmp=i;
            for(int j=1;j<l;j++)
            {
                int tt=tmp/lll;
                tmp%=lll;
                tmp=tmp*10+tt;
                if(tmp>=a&&tmp<min)min=tmp;
            }
            use[min]++;
        }
        ll ret=0;
        for(int i=a;i<=b;i++)
        {
            ret+=(ll)use[i]*(use[i]-1)/2;
        }
        printf("Case #%d: %I64d\n",ca,ret);
    }
    return 0;
}
