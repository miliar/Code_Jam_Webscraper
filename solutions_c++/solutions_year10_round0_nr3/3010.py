#include <stdio.h>
#include <string.h>
#include <queue>
#include <math.h>
using namespace std;

int r,k,n;

struct node
{
	int id;
	int people;
}no[1010];

queue<node> que;

int main()
{
	freopen("C-small-attempt2.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	int cas=1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d%d",&r,&k,&n);
		int i,p,z;
		for(i=0;i<n;i++)
		{
			scanf("%d",&no[i].people);
			no[i].id=i;
			que.push(no[i]);
		}
		int sign=0;
		node temp;
		temp=no[0];
		__int64 sum=0,ans=0;
		for(i=0;i<r;i++)
		{
			node q;
			q=que.front();
			sum=q.people;
			sign=0;
			int id1=q.id;
			while(sum<=k)
			{
				que.pop();
				if(que.empty())
				{
					sign=1;
					break;
				}
				q=que.front();
				sum+=q.people;
			}
			int id2=(q.id-1+n)%n;
			if(sign)
			{
				for(p=0;p<n;p++)
				{
					ans+=no[p].people;
				}
				ans*=r;
				break;
			}
			else
			{
				if(id1<=id2)
				{
					for(p=id1;p<=id2;p++)
					{
						que.push(no[p]);
						ans+=no[p].people;
					}
				}
				else
				{
					for(p=id1;p<n;p++)
					{
						que.push(no[p]);
						ans+=no[p].people;
					}
					for(p=0;p<=id2;p++)
					{
						que.push(no[p]);
						ans+=no[p].people;
					}
				}
				q=que.front();
				if(q.id==temp.id)
				{
					int d;
					d=i+1;
					int num;
					num=r/d;
					ans*=num;
					i=d*num-1;
				}
			}
		}
		printf("Case #%d: %I64d\n",cas++,ans);
		while(!que.empty())
			que.pop();
	}
	return 0;
}