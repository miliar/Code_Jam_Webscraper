#include<iostream>
#include<algorithm>
#include<vector>
#include<cstdio>
using namespace std;

double diff, inp[205];
int v[205];
int N;
bool ispossible(double val)
{
	int i,j;
	double prev=inp[0]-val;
	for(i=0;i<N;i++)
	{
		for(j=0;j<v[i];j++)
		{
			if(i==0 && j==0)
				continue;
			if(inp[i]-prev > diff)
			{
				if(inp[i]-val > prev+diff)
					prev=inp[i]-val;
				else
					prev=prev+diff;
			}
			else
			{
				if(prev+diff-inp[i] > val)
					return false;
				prev=prev+diff;
			}
		}
	}
	return true;
}

int main()
{
	double min,max,mid,ans;
	int t,i;
	scanf("%d",&t);
	for(int tt=1; tt<=t; tt++)
	{
		scanf("%d%lf",&N,&diff);
		for(i=0;i<N;i++)
			scanf("%lf%d",&inp[i],&v[i]);
		min=0.0, max=10000000000000.0, ans=0.0;
		for(i=0;i<100;i++)
		{
			mid=(min+max)/2.0000;
			if(ispossible(mid))
				max=mid , ans=mid;
			else	min=mid;
			//if(min==max)
			//	break;
		}
		
		/*for(i=0;i<N;i++)
			cout<<inp[i]<<" ";
		cout<<endl;*/
		printf("Case #%d: ",tt);
		printf("%.8lf\n",mid);
			
	}
	return 0;
}
