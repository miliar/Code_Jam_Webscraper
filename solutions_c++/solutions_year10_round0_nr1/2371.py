#include<stdio.h>
#include<string>
#include<vector>
#include<string.h>
#include<algorithm>
#include<map>
#include<stack>
#include<set>
#include<math.h>

using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-largeout.txt","w",stdout);
	int test,i,j,n,k,team=0;
	scanf("%d",&test);
	while(test--)
	{
		team++;
		scanf("%d%d",&n,&k);
		int a[40];
		memset(a,0,sizeof(a));
		int count=0;
		a[0]=1;
		for(i=1;i<n;i++)
			a[i]=a[i-1]*2+1;
		if(k==0)
			printf("Case #%d: OFF\n",team);
		else if(n==1)
		{
			if(k%2==1)
				printf("Case #%d: ON\n",team);
			else
				printf("Case #%d: OFF\n",team);
		}
		else if(k==a[n-1])
		{
			printf("Case #%d: ON\n",team);
			continue;
		}
		else if(k<a[n-1])
		{
			printf("Case #%d: OFF\n",team);
			continue;
		}
		else
		{
			int temp=k-a[n-1];
			if(temp%(a[n-1]+1)==0)
            	printf("Case #%d: ON\n",team);
			else
				printf("Case #%d: OFF\n",team);
		}
	}
	return 0;
}
