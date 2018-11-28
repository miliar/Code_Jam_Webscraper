#include <string.h>
#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;
int n,r,k;
int pe[11],pp[11];
int main()
{
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	int t,i,j;
	int cnt=1;
	scanf("%d",&t);
	while(t--)
	{
		int tot=0;
		memset(pe,0,sizeof(pe));
		memset(pp,0,sizeof(pp));
		scanf("%d%d%d",&r,&k,&n);
		for(i=0;i<n;++i)scanf("%d",&pe[i]);
		while(r)
		{
			int sum=0;
			for(i=0;sum<=k&&i<n;++i)
			{
				sum+=pe[i];
			}
			if(i==n&&sum<=k)sum-=pe[i];
			else  sum-=pe[i-1];
				tot+=sum;
				i--;
			for(j=0;j<n;++j)
			{
				pp[j]=pe[i];
				i++;
				i%=n;
			}
			for(j=0;j<n;++j)
				pe[j]=pp[j];
			r--;
		}
		printf("Case #%d: ",cnt++);
		printf("%d\n",tot);
	}
	return 0;
}