#include<cstdio>
#include<iostream>
using namespace std;
namespace solve
{
	const int N_MAX = 100;
	int o[N_MAX], b[N_MAX], n, o_cnt, b_cnt;
	struct Step
	{
		bool o;
		int num;
	} step[N_MAX];
	void work();
}

void solve::work()
{
	int t;
	scanf("%d", &t);
	for (int ii = 0; ii < t; ii ++)
	{
		b_cnt = o_cnt = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; i ++)
		{
			char a;
			cin>>a>>step[i].num;
			step[i].o = (a == 'O');
			if (a == 'O')
				o[o_cnt ++] = step[i].num;
			else
				b[b_cnt ++] = step[i].num;
		}
		int i = 0, j = 0, s = 0, oo = 0, bb = 0, ans = 0;
		while (s < n)
		{
			if (step[s].o)
			{
				if (o[oo] == i && oo < o_cnt)
				{
					oo ++;
					s ++;
				}
				else
					if (oo < o_cnt)
					{
						if (o[oo] > i)
							i ++;
						if (o[oo] < i)
							i --;
					}
				if (bb < b_cnt)
				{
					if (b[bb] > j)
						j ++;
					if (b[bb] < j)
						j --;
				}
			}
			else
			{
				if (oo < o_cnt)
				{
					if (o[oo] > i)
						i ++;
					if (o[oo] < i)
						i --;
				}
				if (!step[s].o && b[bb] == j && bb < b_cnt)
				{
					bb ++;
					s ++;
				}
				else
					if (bb < b_cnt)
					{
						if (b[bb] > j)
							j ++;
						if (b[bb] < j)
							j --;
					}
			}
			ans ++;
		}
		printf("Case #%d: %d\n", ii + 1, ans - 1);
	}
}

int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	solve::work();
}
