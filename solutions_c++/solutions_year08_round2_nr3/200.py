#include<iostream>
#include<string>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;
int f[5006],si[5004];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
freopen("C-small-attempt0.out","w",stdout);
	int N,ca;
	scanf("%d",&N);
	for(ca=1;ca<=N;ca++)
	{
		int k,n,j;
		scanf("%d%d",&k,&n);
		int now=0,num;
		memset(si,0,sizeof(si));
		for(num=1;num<=k;num++)
		{
			int count=0;
			for(j=now;j<k;j=(j==k-1?0:(j+1)))
				if(si[j]);
				else
				{
					count++;
					if(count==num)
					{
						si[j]=1;
						f[j]=count;
						now=(j==k-1?0:(j+1));
						break;

					}
				}
		}
		int ans[300],i;
		for(i=0;i<n;i++)
			scanf("%d",&ans[i]);
		printf("Case #%d:",ca);
		for(i=0;i<n;i++)
			printf(" %d",f[ans[i]-1]);
		printf("\n");
	}
return 0;
}