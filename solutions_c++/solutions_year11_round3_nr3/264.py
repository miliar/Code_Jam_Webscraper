#include<iostream>
using namespace std;
long long gcd(long long x, long long y){
	if (!x || !y) return x > y ? x : y;
	for (long long t; t = x % y; x = y, y = t);
	return y;
}
int a[10005];
int l,h;
int n;
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("c.out","w",stdout);
    int t,i,j,k;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d%d%d",&n,&l,&h);
        for(j=0;j<n;j++)
        scanf("%d",&a[j]);
        int flag=0;
        for(j=l;j<=h;j++)
        {
            for(k=0;k<n;k++)
            {
                if(a[k]%j==0 || j%a[k]==0 ) continue;
                else break;
            }
            if(k==n) break;
        }
        printf("Case #%d: ",i);
        if(j<=h) printf("%d\n",j);
        else printf("NO\n");
    }
    return 0;
}


