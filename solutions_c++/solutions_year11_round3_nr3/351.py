#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
typedef long long int lint;
lint a[100000];
int main()
{
    lint i,j,k,n,l,h,ans;
    int t,T;
    scanf("%d",&T);
    bool possible;
    for(t=1;t<=T;t++)
    {
        scanf("%lld %lld %lld",&n,&l,&h);
        for(i=0;i<n;i++)
            scanf("%lld",&a[i]);
        for(i=l;i<=h;i++)
        {
            possible=true;
            for(j=0;j<n;j++)
            {
                if( a[j]%i!=0 && i%a[j]!=0)
                {
                    possible=false;
                    break;
                }
            }
            if(possible)
            {
                ans=i;
                break;
            }
        }
        printf("Case #%d: ",t);
        if(possible)
            printf("%lld\n",i);
        else
            printf("NO\n");
    }
    return 0;
}

