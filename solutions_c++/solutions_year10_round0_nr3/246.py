#include <iostream>
#include <cstdio>

using namespace std;

int t,n,m,k,r;
int jmp[2000],sum[2000];
int a[2000];

int main()
{
    //freopen("input.txt","r",stdin);
//    freopen("C-small-attempt0.in","r",stdin);
//    freopen("C-small-attempt0.out","w",stdout);
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&t);
    for(int test=0;test<t;test++){
        scanf("%d %d %d",&r,&k,&n);
        for(int i=0;i<n;i++)
            scanf("%d",&a[i]);
        for(int i=0;i<n;i++){
            int j=i,sm=0,q=0;
            for(;q<n&&sm+a[j]<=k;sm+=a[j],j=(j+1)%n,q++);
            jmp[i]=j;
            sum[i]=sm;
        }

        int pos=0;
        long long ans=0;
        for(int i=0;i<r;i++){
            ans=ans+sum[pos];
            pos=jmp[pos];
        }
        printf("Case #%d: %I64d\n",test+1,ans);
        fprintf(stderr,"%d\n",test+1);
    }
    return 0;
}
