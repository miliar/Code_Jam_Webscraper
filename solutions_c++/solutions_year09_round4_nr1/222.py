#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void solve()
{
	int i,j,k,cnt,n;
	char str[70];
	int A[70];
	scanf("%d",&n);
	for(i=0;i<n;++i)
	{
		A[i]=0;
		scanf("%s",str);
		for(j=0;j<n;++j)
		{
			if(str[j]=='1')
				A[i]=j;
		}
	}
	cnt=0;
	for(i=0;i<n;++i)
	{
		if(A[i]>i)
		{
			for(j=i+1;j<n;++j)
			{
				if(A[j]<=i)
					break;
			}
			for(;j>i;--j)
			{
				A[j]=A[j-1];
				++cnt;
			}
		}
	}
	printf("%d\n",cnt);
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large11111.out","w",stdout);
	int t, i;
	scanf("%d", &t);
	for(i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}

