#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;
struct Node
{
	int row;
	int target;
	Node(int r,int t):row(r),target(t){}
};
const int inf = -1;
int main()
{
	int t,i,j,k,n;
	char buf[42][42];
	int target[42];
	int sum,count;
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		//memset(target,0,sizeof(target));
		if(i==7)
			sum=0;
		sum=0;
		scanf("%d",&n);
		for(j=0;j<n;j++)
		{
			scanf("%s",buf[j]);
		}

		for(j=0;j<n;j++)
		{
			for(k=n-1;k>=0;k--)
			{
				if(buf[j][k] == '1')
				{
					target[j] = k;
					break;
				}
			}
			if(k==-1)
				target[j] =0;
		}

		for(j=0;j<n;j++)
		{
			count=0;
			for(k=0;k<n;k++)
			{
				if(target[k] == inf)
					continue;

				if(target[k] > j)
					count++;
				else
				{
					sum+= count;
					target[k] = inf;
					break;
				}
			}
		}

		printf("Case #%d: %d\n",i,sum);
	}
}