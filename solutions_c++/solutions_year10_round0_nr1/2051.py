#include <stdio.h>
#include <string.h>
const int MAXN = 31;
int arr[MAXN];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d",&T);
	for (int t=0;t<T;t++)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		int ind=((k+1)%(1<<n) == 0);
/*		memset(arr,0,sizeof(arr));
		for (int i=0;i<k;i++)
		{
			int j;
			for (j=0;j<n && arr[j];j++)
				arr[j]=1-arr[j];
			if (j<n)
				arr[j]=1;
		}
		int ind=1;
		for (int j=0;j<n;j++)
			if (!arr[j])
				ind=0;*/
		printf(ind?"Case #%d: ON\n":"Case #%d: OFF\n",t+1);
	}
	return 0;
}
