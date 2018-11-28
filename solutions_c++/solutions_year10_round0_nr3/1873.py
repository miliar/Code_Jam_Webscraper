
#include <stdio.h>
#include <string.h>

typedef struct Group
{
	int next_r;
	long long money;
	long long total_money;
} Group;

#define MAX 1001

int visit[MAX];
Group group[MAX];
int num[MAX];

int main()
{
	int t, ca = 1;
	int r, k, n;

	freopen("D:\\c-large.in", "r", stdin);
	freopen("D:\\c-large.out", "w", stdout);

	scanf("%d", &t);
	while (t--)
	{
		memset(visit, 0, sizeof(visit));
		scanf("%d %d %d", &r, &k, &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", &num[i]);

		int man_num;
		for (int i = 0; i < n; ++i)
		{
			man_num = num[i];
			if (man_num >= k)
			{
				group[i].next_r = (i+1)%n;
				group[i].money = man_num;
				group[i].total_money = 0;
				continue;
			}
			
			int j;
			for (j = (i+1)%n; j != i;)
			{
				if (man_num + num[j] <= k)
					man_num += num[j];
				else
					break;

				j = (j+1)%n;
			}
			
			group[i].money = man_num;
			group[i].next_r = j;
			group[i].total_money = 0;
		}
		
		long long total = 0;
		int next = 0;
		int round = 1;
		int notexe = 0;

		for (; round <= r; ++round)
		{
			if (visit[next] == 0)
			{
				visit[next] = round;
				total += group[next].money;
				group[next].total_money = total;
				next = group[next].next_r;
			}
			else
			{
				notexe = 1;
				break;
			}
		}

		printf("Case #%d: ", ca++);

		if (notexe)
		{
			round--;
			int not_ite_round = visit[next]-1;
			long long not_ite_mon = 0;
			if (not_ite_round > 0)
				not_ite_mon = group[next].total_money-group[next].money;
			long long ite_mon = total-not_ite_mon;
			int ite_round = round-not_ite_round;

			r -= not_ite_round;

			long long ans = 0;
			ans += not_ite_mon;
			ans += (r/ite_round)*ite_mon;

			int tmp = r%ite_round;
		
			for (int i = 1; i <= tmp; ++i)
			{
				ans += group[next].money;
				next = group[next].next_r;
			}

			printf("%lld\n", ans);
		}
		else
			printf("%lld\n", total);
	}

	return 0;
}