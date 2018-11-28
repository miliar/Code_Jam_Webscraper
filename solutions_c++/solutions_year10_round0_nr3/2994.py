#include<stdio.h>
#include<queue>
#include<algorithm>

using namespace std;

int main(void){
	int T;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		queue<int > q;

		int R,K,N,i;
		scanf("%d%d%d",&R,&K,&N);

		int p;
		for(i=0;i<N;i++)
		{
			scanf("%d",&p);
			q.push(p);
		}

		int cost = 0;
		for(i=0;i<R;i++)
		{
			int count = 0,flg = 0;
			while(count + q.front()<=K && flg<N)
			{
				int tmp = q.front();
				count += tmp;
				q.pop();
				q.push(tmp);
				flg++;
			}
			cost += count;
		}

		while(!q.empty())
		{
			q.pop();
		}
		printf("Case #%d: %d\n",t,cost);
	}
	return 0;
}