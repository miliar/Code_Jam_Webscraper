#include<iostream>
#include<queue>
using namespace std;
int T,R,k,N;
int main()
{
	int i=1,j;
	freopen("D://C-small-attempt4.in","r",stdin);
	freopen("D://C-small.out","w",stdout);
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		queue<int> q;
		scanf("%d %d %d ",&R,&k,&N);
		for(j=0;j<N;j++)
		{
			int t;
			scanf("%d",&t);
			q.push(t);
		}

		int total=0;
		for(j=0;j<R;j++)
		{
			queue<int> p; 
			int m=k;
			while(!q.empty())
			{
				int a=q.front();
				if(m>=a)
				{
					m-=a;
					q.pop();
					total+=a;
					p.push(a);
				}  else break;
			}
			while(!p.empty())
			{
				q.push(p.front());
				p.pop();
			}
			
		}
		printf("Case #%d: %d\n",i,total);

	}


	return 0;
}