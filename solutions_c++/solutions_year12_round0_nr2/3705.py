#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;
typedef long long LL;
int main()
{
    int t,n,s,p,in[1000],i,j;
    freopen("gcb.in","r",stdin);
    freopen("gcb.out","w",stdout);
    scanf("%d",&t);
    for(int cn=1;cn<=t;cn++)
    {
        scanf("%d%d%d",&n,&s,&p);
        for(i=0;i<n;i++)
            scanf("%d",in+i);
        sort(in,in+n);
        //for(i=0;i<n;i++)printf("%d ",in[i]);printf("\n");
        int ret=0;
        for(i=n-1;i>=0;i--)
        {
            if(in[i]>3*p-3)
                ret++;
            else if(in[i]>=3*p-4&&p>1)
                if(s>0)
                {
                    //printf("%d %d %d\n",in[i],s,ret);
                    ret++;
                    s--;
                }
        }
        printf("Case #%d: %d\n",cn,ret);
    }
    return 0;
}
