#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
struct card
{
	int t,c,s;
	bool operator<(const card &a)const
	{
		return t<a.t||(t==a.t&&(c<a.c||(c==a.c&&s<a.s)));
	}
	card(int _c,int _s,int _t)
	{
		c=_c;s=_s;t=_t;
	}
};
bool cmp(const int &a,const int &b)
{
	return a>b;
}
int num[1000];
int cal(int turn)
{
	int ans=0;
	for(int i=99;i>0&&turn>0;i--)
	{
		ans+=min(num[i],turn)*i;
		turn-=min(num[i],turn);
	}
	//printf("turn=%d ans=%d\n",turn,ans);
	return ans;
}
int main()
{
	freopen("c_small.in","r",stdin);
	freopen("c_small.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
		priority_queue<card> que;
		for(int i=0;i<100;i++)num[i]=0;
		int n,m;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			int a,b,c;
			scanf("%d%d%d",&a,&b,&c);
			que.push(card(a,b,c));
			num[b]++;
		}
		scanf("%d",&m);
		int top=0,turn=1,ans=0,sum=0;
		while(turn>0&&!que.empty())
		{
			//printf("card %d %d %d nn\n",que.top().c,que.top().s,que.top().t);
			if(que.top().t>0)
			{
				turn--;
				turn+=que.top().t;
				sum+=que.top().s;
				int k=que.top().c;
				num[que.top().s]--;
				que.pop();
				for(int i=0;i<k;i++)
				{
					if(top==m)break;
					top++;
					int a,b,c;
					scanf("%d%d%d",&a,&b,&c);
					num[b]++;
					
					que.push(card(a,b,c));
				}
			}
			else
			{
				ans=max(ans,sum+cal(turn));
			
				turn--;
				turn+=que.top().t;
				sum+=que.top().s;
				int k=que.top().c;
				num[que.top().s]--;
				que.pop();
				for(int i=0;i<k;i++)
				{
					if(top==m)break;
					top++;
					int a,b,c;
					scanf("%d%d%d",&a,&b,&c);
					num[b]++;
					que.push(card(a,b,c));
				}
			}
		}
		ans=max(ans,sum);
		while(top<m)
		{
			top++;
			int a,b,c;
			scanf("%d%d%d",&a,&b,&c);
		}
		printf("Case #%d: %d\n",cas,ans);
	}
}

