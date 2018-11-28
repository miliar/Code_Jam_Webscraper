#include <cstdio>
#include <cmath>

const int N = 200;
int n;
int seq[N];
char type[N];

void Scan()
{
	for (int i = 0; i < N; i++)
	{
		seq[i] = 0;
		type[i] = 0;
	}


	scanf("%d\n", &n);
	for (int i = 0; i < n; i++)
		scanf("%c%d\n", &type[i], &seq[i]);
}

int GetTask(int pos, char task)
{
	for (int i = pos; i < n; i++)
		if (task == type[i]) return i;
	return -1;
}

int Move(int from, int to)
{
	if (from < to) return from+1;
	else if (from > to) return from-1;
	else return to;
}

void Solve(int t)
{
	int p1 = 1, p2 = 1;
	int cur = 0;	
	int time = 0;
	for (int cur = 0; cur < n; cur++)
	{
		if (type[cur] == 'O')
		{
			int dif = abs(p1-seq[cur]);
			int passiveTask = GetTask(cur, 'B');
			for (int i = 0; i <= dif; i++)
			{
				p1 = Move(p1, seq[cur]);
				if (passiveTask != -1)
					p2 = Move(p2, seq[passiveTask]);
			}
			time += dif+1;
		}
		else if (type[cur] == 'B')
		{
			int dif = abs(p2-seq[cur]);
			int passiveTask = GetTask(cur, 'O');
			for (int i = 0; i <= dif; i++)
			{
				p2 = Move(p2, seq[cur]);
				if (passiveTask != -1)
					p1 = Move(p1, seq[passiveTask]);
			}
			time += dif+1;
		}
	}
	printf("Case #%d: %d\n", t+1, time);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		Scan();
		Solve(i);
	}
	return 0;
}