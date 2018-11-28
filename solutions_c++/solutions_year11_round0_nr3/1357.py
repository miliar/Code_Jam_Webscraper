#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int m,n,s[1005],i,j,huang,sum;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&m);
    for (i=1;i<=m;i++)
    {
        scanf("%d",&n);
		for(j=0;j<n;j++)
            scanf("%d",&s[j]);
        sum=huang=s[0];
        for(j=1;j<n;j++)
        {
            sum+=s[j];
            huang^=s[j];
        }
        sort(s,s+n);
        if(huang==0)
			printf("Case #%d: %d\n",i,sum-s[0]);
        else 
			printf("Case #%d: NO\n",i);
    }
    return 0;
}
