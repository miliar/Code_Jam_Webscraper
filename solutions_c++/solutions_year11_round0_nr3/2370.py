#include <stdio.h>
#include <algorithm>
using namespace std;
int A[1005];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t,i,j,n;
	int tmp=0;
	int ans=0;
	scanf("%d",&t);
	for (i=1;i<=t;i++)
	{
		ans=0;
		tmp=0;
		scanf("%d",&n);
		for (j=0;j<n;j++)
		{
			scanf("%d",&A[j]);
			tmp=tmp^A[j];
			ans+=A[j];
		}
		sort(A,A+n);
		if(tmp==0)ans-=A[0];
		if(tmp!=0)
			printf("Case #%d: NO\n",i);
		else printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}