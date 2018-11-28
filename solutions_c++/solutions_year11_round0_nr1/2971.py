#include <cstdio>
#include <iostream>

#define N 239

using namespace std;

char robot[N];
int number[N], q_o[N], q_b[N];

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int n, now = 0, n_b = 0, n_o = 0, pos_b = 1, pos_o = 1, t_b = 0, t_o = 0;

		cin >> n;

		for (int j = 0; j < n; j++)
		{
			char sym;
			int num;

			cin >> sym >> num;

			if (sym == 'B')
				q_b[n_b++] = num;				
			else
				q_o[n_o++] = num;

			robot[j] = sym;
			number[j] = num;
		}

		for (int timer = 1; ; timer++)
		{
			if (robot[now] == 'B' && pos_b == number[now])
			{
				t_b++;
				now++;

				if (now == n)
				{
					printf("Case #%d: %d\n", i + 1, timer);
					break;
				}

				if (pos_o < q_o[t_o]) pos_o++;
				if (pos_o > q_o[t_o]) pos_o--;

				continue;
			}

			if (pos_b < q_b[t_b]) pos_b++;
			if (pos_b > q_b[t_b]) pos_b--;					
			
			if (robot[now] == 'O' && pos_o == number[now])
			{
				t_o++;
				now++;

				if (now == n)
				{
					printf("Case #%d: %d\n", i + 1, timer);
					break;
				}

				continue;
			}

			if (pos_o < q_o[t_o]) pos_o++;
			if (pos_o > q_o[t_o]) pos_o--;					
		}
	}
	return 0;
}
