#include<iostream>
using namespace std;
long l,r,i,j,k,x,ans,s,a[1000],p;
long tst,w;
int main()
{
    freopen("Cin.txt","r",stdin);
    freopen("Cout.txt","w",stdout);
    for (scanf("%ld",&tst),w=1;w<=tst;w++)
    {
        scanf("%ld%ld",&l,&r);
        ans=0;
        for (i=l;i<=r;i++)
        {
            p=0;
            for (j=10;j<=i;j*=10)
            {
                k=i%j;
                x=i/j;
                for (s=j;s<=i;s*=10) k*=10;
                k+=x;
                if (k>i && k<=r)
                {
                   for (long c=0;c<p;c++) if (a[c]==k) goto wa;
                   ans++;
                   a[p++]=k;
                }
                wa:;
            }
        }
        printf("Case #%ld: %ld\n",w,ans);
    }
    return 0;
}
