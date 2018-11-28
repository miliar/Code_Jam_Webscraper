#include <fstream>

using namespace std;

ifstream cin("data.in");
ofstream cout("data.out");

int n,m,r;
int x[100], y[100];
int opt[1000][1000];


void init()
{
	cin >> n >> m;
	cin >> r;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
			opt[i][j] = -2;
	for (int i = 0; i < r; i++)
	{
		cin >> x[i] >> y[i];
		opt[x[i]][y[i]] = -1;
	}
}

int calc()
{
	opt[1][1] = 1;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
		{
			if (opt[i][j] < 0)
				continue;
			if (i+1 <= n && j+2 <= m && opt[i+1][j+2] != -1)
			{
				if (opt[i+1][j+2] == -2)
					opt[i+1][j+2] = opt[i][j];
				else
					opt[i+1][j+2] += opt[i][j];
				opt[i+1][j+2] %= 10007;
			}
			if (i+2 <= n && j+1 <= m && opt[i+2][j+1] != -1)
			{
				if (opt[i+2][j+1] == -2)
					opt[i+2][j+1] = opt[i][j];
				else
					opt[i+2][j+1] += opt[i][j];
				opt[i+2][j+1] %= 10007;
			}
		}
	if (opt[n][m] == -2)
		return 0;
	else
		return (opt[n][m] % 10007);
}


int main()
{
	int N;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		init();
		cout << "Case #" << i+1 << ": " << calc() << endl;
	}
}
