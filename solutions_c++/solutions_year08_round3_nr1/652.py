#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
int a[1003];
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt3.out","w",stdout);
	int c,C;
	int i;
	scanf("%d",&C); 
	for(c=1;c<=C;c++)
	{
		int P,K,L;
		scanf("%d%d%d",&P,&K,&L); 
		for(i=0;i<L;i++)
		{
			scanf("%d",&a[i]);
		
		}
		printf("Case #%d:",c);
		if(K*P<L)
			printf("Impossible\n");
		else 
		{
			sort(a,a+L);


			int ans=0,sum=0,bei=1;
			for(i=L-1;i>=0;i--)
			{
				sum+=a[i]*bei;
				ans++;
				if(ans>=K)
				{
					bei++;
				   ans=0;
				}
			}
			printf(" %d\n",sum);
		}


	}
}