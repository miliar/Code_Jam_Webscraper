#include <iostream>

using namespace std;


int a[10000];
int step[10000];
long long pay[10000];
bool was[10000];

int cur; 
int r, k ,n, t, T;
long long ans;
void GetNext()
{
	int start = cur;
	int sum = a[cur++];

	cur %= n;

	while (sum + a[cur] <= k && cur != start)
	{
		sum += a[cur];
		cur ++;
		cur %= n;
	}
	ans += sum;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;

	cin >> T;

	for (int t = 1; t <= T; ++ t)
	{
		cin >> r >> k >> n;

		int i;
		for ( i = 0; i < n; ++ i)
		{
			cin >> a[i];
		}

		memset(was, false, sizeof(was));

		i = 0;
		ans = 0;
		cur = 0;

		while (i < r && !was[cur])
		{

			was[cur] = true;
			step[cur] = i;
			pay[cur] = ans;
			++ i;

			GetNext();
		}


		if (was[cur] && i < r)
		{
			ans = pay[cur] + (ans - pay[cur]) * ((r - step[cur]) / (i - step[cur]));

			int prom_r = r - step[cur];
			prom_r %= i - step[cur];
			r = prom_r;

			//r = r - (step[cur] + ((r - step[cur]) / (i - step[cur])));

			i = 0;
			while (i < r)
			{
				GetNext();
				++ i;
			}
		}

		cout << "Case #" << t << ": " << ans << '\n';

	}
	return 0;
}