#include <stdio.h>
#include <queue>
using namespace std;
int main()
{
	queue<int>que1;
	queue<int>que2;
	queue<int>t;
	int T;
	scanf("%d",&T);
	int id;
	for(id=1;id<=T;id++)
	{
		int r,k,n;
		scanf("%d%d%d",&r,&k,&n);
		que1=que2=t;
		while(n--)
		{
			int p;
			scanf("%d",&p);
			que1.push(p);
		}
		int ans=0;
		while(r--)
		{
			int sum=0;
			while(!que1.empty())
			{
				if(sum+que1.front()>k)
					break;
				else
				{
					sum+=que1.front();
					que2.push(que1.front());
					que1.pop();
				}
			}
			ans+=sum;
			while(!que2.empty())
			{
				que1.push(que2.front());
				que2.pop();
			}
		}
		printf("Case #%d: %d\n",id,ans);
	}
	return 0;
}



