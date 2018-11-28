#include<iostream>
#include<queue>

using namespace std;

int main()
{
	int c,t,i,r,k,n,sum,cost,num,w,j,s;

//	freopen("C-small-attempt.in","r",stdin);
//	freopen("outputs.out","w",stdout);

	scanf("%d",&t);

	for(c=1;c<=t;c++)
	{
		scanf("%d%d%d",&r,&k,&n);
		
		queue<int> q;

		for(i=0,s=0;i<n;i++)
		{	
			scanf("%d",&num);
			q.push(num);
			s+=num;
		}

		for(i=0,sum=0,cost=0;i<r;i++,cost+=sum)
		{
			for(sum=0,w=q.front(),j=0;(sum+w)<=k && (sum+w)<=s;w=q.front(),j++)
			{
				q.pop();
				sum+=w;
				q.push(w);
			}
		}

		printf("Case #%d: %d\n",c,cost);
	}

	return 0;
}
