#include<queue>
#include<cstdio>

using namespace std;

int main()
{
	int T;

	long long int R,k,N,G[1005],sum,val[1005];
	int atHead[1005],visited[1005];

	scanf("%d\n",&T);
	for(int ii = 1; ii<=T ;++ii)
	{
		queue<int> Q;
		sum = 0;

		scanf("%lld %lld %lld",&R,&k,&N);
		for(int i = 0; i < N;++i)
		{
			scanf("%lld",G+i);
			Q.push(i);
			visited[i] = -1;
			val[i] = 0;

			sum += G[i];
		}

		if(sum <= k)
		{
			printf("Case #%d: %lld\n",ii,sum*R);
		}
		else
		{
			int cc = 0;
			while(R > 0 && visited[Q.front()] == -1)
			{
				R--;
				atHead[cc] = Q.front();
				visited[Q.front()] = cc;
				cc++;
				long long int s = 0;
				while(s + G[Q.front()] <= k)
				{
					s += G[Q.front()];
					sum = Q.front();
					Q.pop();
					Q.push(sum);
				}
				
				for(int i = 0;i < cc;++i) val[i] += s;
				//printf("s --> %lld\n",s );
				//for(int i = 0;i < cc;++i) printf("--> %lld\n",val[i]);
			}

			//for(int i = 0;i < cc;++i) printf("%lld\n",val[i]);

			int head = Q.front();
			int x = R / (cc - visited[head]);
			int y = R % (cc - visited[head]);
			printf("Case #%d: %lld\n",ii, val[0] + val[visited[head]] * x - val[visited[head]+y] + val[visited[head]]);
		}
	}
	return 0;
}
