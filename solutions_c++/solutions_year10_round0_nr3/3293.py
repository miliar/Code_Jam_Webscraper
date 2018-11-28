#include <stdio.h>
#include <queue>
using namespace std;

int round;
queue<int>group;

int f(int r, int k)
{
	int res = 0;
	int qsize = group.size(), ini = 0, total = 0, flag = 0;
	while (ini != qsize)
	{
		int hold = group.front();
		if (total + hold <= k)
		{
			ini++;
			total += hold;
			group.pop();
			group.push(hold);
			if (ini == qsize)
			{
				if (round != 0)
				{
//					flag = 1;
//					ini = 0;
					ini++;
				}
				else
				{
					round++;
					res += total;
					break;
				}
			}
		}
		else
		{
			res += total;
			total = 0;
			round++;
//			if (flag)
//				break;
			if (round == r)
				break;
		}
	}
	return res;
}

int main()
{
	freopen("c.out.txt","w",stdout);
	freopen("c.in.txt","r",stdin);
	int kase, tCase = 0;
	scanf ("%d",&kase);

	while (kase--)
	{
		int ans = 0, p=group.size();
		int r,k,n,g;
		round = 0;
		for (int j=0; j<p; j++)
			group.pop();
		scanf ("%d%d%d",&r,&k,&n);
		for (int i=0; i<n; i++)
		{
			scanf ("%d",&g);
			group.push(g);
		}
		ans += f(r,k);
		if (round < r)
		{
			int mul = r/round;
			ans *= mul;
			r %= round;
			round = 0;
			if (r!=0)
				ans += f(r,k);
		}
		printf ("Case #%d: %d\n", ++tCase, ans);
	}

	return 0;
}