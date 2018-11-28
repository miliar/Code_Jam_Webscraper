#include<stdio.h>
#include<queue>
using namespace std;

int r, k, n, cap, n1;
long long int sum;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
#endif

	int cases, tmp;
	scanf("%d\n", &cases);

	for(int i = 1; i <= cases; i++)
	{
		queue<int> que;
		sum = 0;

		scanf("%d %d %d", &r, &k, &n);
		for(int j = 0; j < n; j++)
		{
			scanf("%d\n", &tmp);
			que.push(tmp);
		}

		printf("Case #%d: ", i);
		for(int j = 0; j < r; j++)
		{
			cap = n1 = 0;
			while(1)
			{
				if(n1 >= n) break;
				tmp = que.front();
				if(cap + tmp > k) break;
				cap += tmp;
				que.pop();
				que.push(tmp);
				n1++;
			}
			sum += cap;
		}

		printf("%d\n", sum);

	}


	return 0;

}
