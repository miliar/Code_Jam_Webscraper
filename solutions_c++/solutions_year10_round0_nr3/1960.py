#include <cstdio>
unsigned long long m[1024],p[1024];
void pri(int *a, int n)
{
    int i;
    for(i=1;i<=n;++i) printf("%d ",a[i]);
    printf("\n");
    return;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    unsigned long long t,N,r,k,n,i,j,v[2048],s;
    scanf("%lld",&N);
    for(t=1;t<=N;++t)
    {
        scanf("%lld%lld%lld",&r,&k,&n); s=0;
        for(i=1;i<=n;++i) {scanf("%lld",&v[i]); s+=v[i];}
        if (s>=k) {
        for(j=n+1,i=1;i<=n;++i,++j) v[j]=v[i];
        s=v[1];  j=2;
        for(i=1;i<=n;++i)
        {
             s-=v[i-1]; --j;
            while(s<=k) { ++j;
                s+=v[j];
                }
            s-=v[j];
            if(j>n) m[i]=j-n;
            else m[i]=j;
            p[i]=s;
        }
        s=0; j=1;
        for(i=1;i<=r;++i)
        {
            s+=p[j];
            j=m[j];
        }
        printf("Case #%lld: %lld\n",t,s);
        }
        else printf("Case #%lld: %lld\n",t,s*r);
    }
    return 0;
}
