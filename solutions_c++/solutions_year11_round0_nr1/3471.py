#include <cstdio>

int s[500];
int N;
int b[500];
int n_b;
int o[500];
int n_o;

int abs(int a)
{
	return a > 0? a : -a;
}

int main()
{
	freopen("D:/A-small-attempt0.in", "r", stdin);
	freopen("in.txt", "w", stdout);
	int T, i, j;
	scanf("%d", &T);
	for (i = 1; i <= T; i++)
	{
		printf("Case #%d: ", i);

		scanf("%d", &N);
		n_b = 0;
		n_o = 0;
		for (j = 0; j < N; j++)
		{
			char c[10];
			int p;
			scanf("%s%d", c, &p);
			if (c[0] == 'O') 
			{
				s[j] = p;
				o[n_o++] = p;
			}
			else
			{
				s[j] = -p;
				b[n_b++] = p;
			}
		}
		int cur_o = 1;
		int cur_num_o = 0;
		int cur_b = 1;
		int cur_num_b = 0; 
		int count = 0;
		for (j = 0; j < N; j++)
		{
			if (s[j] > 0)
			{
				int num;
				num = abs(cur_o - s[j]) + 1;
				count += num;
				cur_o = s[j];
				cur_num_o++;
				if (cur_num_b < n_b && b[cur_num_b] < cur_b)
				{
					if (cur_b - num > b[cur_num_b]) cur_b -= num;
					else cur_b = b[cur_num_b];
				}
				else if (cur_num_b < n_b && b[cur_num_b] > cur_b)
				{
					if (cur_b + num < b[cur_num_b]) cur_b += num;
					else cur_b = b[cur_num_b];
				}
			}
			else
			{
				int num;
				num = abs(cur_b + s[j]) + 1;
				count += num;
				cur_b = -s[j];
				cur_num_b++;
				if (cur_num_o < n_o && o[cur_num_o] < cur_o)
				{
					if (cur_o - num > o[cur_num_o]) cur_o -= num;
					else cur_o = o[cur_num_o];
				}
				else if (cur_num_o < n_o && o[cur_num_o] > cur_o)
				{
					if (cur_o + num < o[cur_num_o]) cur_o += num;
					else cur_o = o[cur_num_o];
				}
			}
		}
		printf("%d\n", count);
	}
	return 0;
}

