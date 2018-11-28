#include <iostream>
#include <queue>

using namespace std;

int g[1010];

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	
	queue<int> q;
	int R,k,N,t,i,j,total,now,m,cnt;
	cin>>t;
	for(int tcase = 1;tcase<=t;tcase++)
	{
		while(!q.empty())
			q.pop();
		total=0,cnt=0;
		cin>>R>>k>>N;
		now = k;
		for(i=0;i<N;i++)
		{
			cin>>g[i];
			q.push(g[i]);
		}
		for(i=0;i<R;i++)
		{
			if(q.size()==1)
			{
				total = R * q.front();
				break;
			}
			m = q.front();
			//printf("Before while %d ",m);
			while(m<=now)
			{
				q.pop();
				q.push(m);
				cnt++;
				if(cnt>N)
				{
					break;
				}
				else
				{
					total +=m;
					now-=m;
					m = q.front();
				}
			}
			now=k;
			cnt=0;
		}
		
		printf("Case #%d: %d\n",tcase,total);
	}



return 0;
}