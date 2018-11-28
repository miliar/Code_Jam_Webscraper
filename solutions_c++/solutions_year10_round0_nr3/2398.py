#include<stdio.h>
#include<queue>

using namespace std;

queue <int> Q;

int main()
{
	int t, R, n, k, g, i, sum, tmp, front, cnt, caseno=1;



	scanf("%d",&t);

	while(t--)
	{
		sum = 0;
		while(!Q.empty())
			Q.pop();

		scanf("%d%d%d",&R,&k,&n);

		for(i=0; i<n; i++)
		{
			scanf("%d",&g);
			Q.push(g);
		}

		for(i=0; i<R; i++)
		{
			cnt=0;
			tmp = k;
			while(tmp>=Q.front())
			{ 
				cnt++;
				front = Q.front();
				sum = sum + front;
				tmp = tmp - front;
				Q.push(front);
				Q.pop();

				if(cnt==n)
					break;
			}
		}

		printf("Case #%d: %d\n",caseno++,sum);
	}
	return 0;

}