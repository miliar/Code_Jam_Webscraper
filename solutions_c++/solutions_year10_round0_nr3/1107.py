#include <iostream>
#include <queue>
using namespace std;
struct group
{
	int num;
	int remaining;
	int total;
};
int main ()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int T,R,k,N;
	scanf("%d",&T);
	for(int i=0;i<T;++i)
	{
		int sum = 0,total = 0;
		queue<group> groups;
		scanf("%d %d %d",&R,&k,&N);
		for(int j=0;j<N;++j)
		{
			group g;
			scanf("%d",&g.num);
			g.remaining=0;
			g.total=0;
			groups.push(g);
			sum+=g.num;
		}
		//check trivial case where sum(g) < k
		if(sum < k)
		{
			total = sum * R;
		}
		else
		{
			while(R > 0)
			{
				group g = groups.front();
				if(g.remaining > 0 && g.remaining < R)
				{
					int r = g.remaining;
					int t = g.total;
					int n = R/(r - R);
					total += (total - t) * n;
					R = R % (r-R);
				}
				else
				{
					groups.pop();
					g.remaining = R;
					g.total = total;
					sum = g.num;
					groups.push(g);
					while(sum + groups.front().num <= k)
					{
						g = groups.front();
						groups.pop();
						sum += g.num;
						groups.push(g);
					}
					total+=sum;
					--R;
				}

			}
		}
		printf("Case #%d: %d\n",i+1,total);
	}
	return 0;
}
