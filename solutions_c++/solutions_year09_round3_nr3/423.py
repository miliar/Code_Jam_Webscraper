#include <iostream>
#include <algorithm>

using namespace std;

int used[10];
int ans,num[10], visit[105];
int p, q, value[10];
void work()
{
	memset(visit, 0, sizeof(visit));

	int re = 0, i , j, k;
	for(i = 0; i < q; i ++)
	{
		visit[num[i]] = 1;
		for(j = num[i]-1; j >= 1; j --)
		{
			if(visit[j] == 1)
				break;
			re ++;
		}
		for(j = num[i]+1; j <= p; j ++)
		{
			if(visit[j] == 1)
				break;
			re ++;
		}
	}
	if(re < ans)
		ans = re;
}


int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small.txt", "w", stdout);
	int Test, i ,j , tt;
	scanf("%d",&Test);
	for(tt = 1; tt <= Test; tt ++)
	{
		scanf("%d %d",&p,&q);
		for(i = 0; i < q; i ++)
			scanf("%d",&num[i]);

		ans = p * q;
		do
		{
			work();
		}
		while(next_permutation(num, num + q));
		printf("Case #%d: %d\n", tt , ans);
	}
	return 0;
}