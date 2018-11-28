#include<iostream>
using namespace std;
#define maxn 1010000
bool b[maxn];
long long n,x;
long ss[maxn],m,i,j,ans,cas,tst;
int main()
{
    memset(b,0,sizeof(b));
    m=0;
    for (i=2;i*i<maxn;i++) if (!b[i])
        for (j=i+i;j<maxn;j+=i) b[j]=1;
    for (i=2;i<maxn;i++) if (!b[i]) ss[m++]=i;
    freopen("C.in","r",stdin);
    freopen("out.txt","w",stdout);
    for (scanf("%ld",&cas),tst=1;tst<=cas;tst++)
    {
        cin>>n;
        if (n==1)
        {
           printf("Case #%ld: 0\n",tst);
           continue;
        }
        ans=1;
        for (i=0;i<m && (long long)ss[i]*(long long)ss[i]<=n;i++)
        {
            x=ss[i];
            while (x<=n)
            {
                  x*=ss[i];
                  ans++;
            }
            ans--;
        }
        printf("Case #%ld: %ld\n",tst,ans);
    }
//    system("PAUSE");
    return 0;
}
