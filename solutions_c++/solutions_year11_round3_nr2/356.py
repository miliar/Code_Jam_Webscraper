#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
typedef long long int lint;
lint a[1000005];
lint b[1000005];
int main()
{
    lint i,j,k,t1,T;
    lint l,t,n,c;
    scanf("%lld",&T);
    for(t1=1;t1<=T;t1++)
    {
        scanf("%lld %lld %lld %lld",&l,&t,&n,&c);
        for(i=0;i<c;i++)
            scanf("%lld",&a[i]);
        for(i=0;i<c;i++)
        {
            k=1;
            a[i]*=2;
            while(((k*c)+i)<n)
            {
                a[(k*c)+i]=a[i];
                k++;
            }
        }
        /*for(i=0;i<n;i++)
            printf("%d\n",a[i]);
        printf("here\n");*/
        i=0;
        lint sum=0;
        while(sum<t && i<n)
        {
            sum+=a[i];
            //printf("sum %d,%d\n",sum,i);
            i++;
        }
        if(sum>t)
        {
            i--;
            a[i]=(sum-t);
            sum=t;
        }
        lint ans=sum;
        lint index=i;
        for(i=index;i<n;i++)
        {
            b[i-index]=a[i];
            //printf("b[i] %d",b[i-index]);
        }
        lint n1=n-index;
        sort(b,b+n1);
        for(i=n1-1;i>=(n1-l)&& i>=0;i--)
        {

            ans+=(b[i]/2);
            //printf("ans=%d\n",ans);
        }
        for(;i>=0;i--)
        {
            ans+=b[i];
            //printf("ans=%d\n",ans);
        }
        printf("Case #%lld: %lld\n",t1,ans);
    }
    return 0;
}
