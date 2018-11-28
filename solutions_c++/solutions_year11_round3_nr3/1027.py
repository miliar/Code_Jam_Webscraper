#include<cstdio>
#include<string.h>
#include<cstdlib>

#define REP(i,n) for(int i=0;i<n;i++)

long long n,l,h,ans,tempa;
long long f[10010];

int compare (const void * a, const void * b)
{
  return ( *(long long*)a - *(long long*)b );
}

int main() {
    freopen("D://test.txt","r",stdin);
    freopen("D://testout.txt","w",stdout);
    int t;
    scanf("%d\n",&t);
    REP(i,t) {
        scanf("%lld%lld%lld",&n,&l,&h);
        for(long long j=0;j<n;j++) {
            scanf("%lld",&f[j]);
        }
        qsort(f,n,sizeof(long long),compare);
        ans=-1;
        for(long long j=l;j<=h;j++) {
            tempa=0;
            for(long long k=0;k<n;k++) {
                if(f[k]%j==0 || j%f[k]==0) {
                    ++tempa;
                }
            }
            if(tempa==n) {
                ans=j;
                break;
            }
        }
        printf("Case #%d: ",i+1);
        if(ans>0) {
            printf("%lld\n",ans);
        }
        else {
            printf("NO\n");
        }
    }
    fclose(stdout);
    fclose(stdin);
    return 0;
}
