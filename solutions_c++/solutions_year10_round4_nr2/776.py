#include <iostream>
using namespace std;

const int N = 1030;

int f[N][N];
int M[N];
int n;

bool check(int x, int y)
{
	bool flag = false;
	for (int i = 0; i < (1 << n); i++)
		if (i >> x == y)
			if (M[i] > 0)
			{
				flag = true;
				M[i]--;
			}
	return flag;
}

void work()
{
	cin >> n;
	for (int i = 0; i < (1 << n); i++)
	{
		cin >> M[i];
		M[i] = n - M[i];
	}
	for (int i = 1; i <= n; i++)
	{
		for (int j = 0; j < (1 << (n-i)); j++)
			cin >> f[i][j];
	}
	int cnt = 0;
	for (int i = n; i >= 1; i--)
		for (int j = 0; j < (1 << (n-i)); j++)
			if (check(i,j))
			{
				cnt++;

			}
	cout << cnt << endl;
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		work();
	}
}