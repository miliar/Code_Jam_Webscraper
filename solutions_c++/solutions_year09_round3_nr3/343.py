#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;


int q[101],p,chu[101];
bool up[111];

int main()
{
	int t,i,j,ooo=1;
	freopen("h://f.in","r",stdin);
	freopen("h://ans.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		int k;
		int maxx=1000000000;
		int sum=0;
		scanf("%d%d",&p,&k);
		for(i=0;i<k;i++)
		{
			scanf("%d",&q[i]);
			chu[i]=q[i];
		}
		memset(up,false,sizeof(up));
		for(i=0;i<k;i++)
		{
			up[q[i]]=true;
			for(j=q[i]+1;j<=p;j++)
			{
				if(up[j])
					break;
				sum++;
			}
			for(j=q[i]-1;j>=1;j--)
			{
				if(up[j])
					break;
				sum++;
			}
		}
		if(sum<maxx) maxx=sum;
		while(next_permutation(q,q+k)) 
		{
			sum=0;
			for(i=0;i<k;i++)
				if(q[i]!=chu[i]) break;
			if(i==k)
				break;
			memset(up,false,sizeof(up));
			for(i=0;i<k;i++)
			{
				up[q[i]]=true;
				for(j=q[i]+1;j<=p;j++)
				{
					if(up[j])
						break;
					sum++;
				}
				for(j=q[i]-1;j>=1;j--)
				{
					if(up[j])
						break;
					sum++;
				}
			}
			if(sum<maxx) maxx=sum;
		}
		printf("Case #%d: %d\n",ooo++,maxx);
	}
}
