#include <fstream>

using namespace std;

ifstream cin("data.in");
ofstream cout("data.out");

int tree[20000];
int opt[20000][2];
int g[20000];
int c[20000];
int m, v;

void init()
{
	cin >> m >> v;
	for (int i = 1; i <= m; i++)
	{
		tree[i] = 0;
		opt[i][0] = -1;
		opt[i][1] = -1;
		g[i] = -1;
		c[i] = -1;
	}
	for (int i = 1; i <= (m-1)/2; i++)
	{
		cin >> g[i] >> c[i];
	}
	for (int i = (m-1)/2+1; i <= m; i++)
	{
		cin >> tree[i];
		opt[i][tree[i]] = 0;
	}
}

void dp()
{
	for (int i = (m-1)/2; i >= 1; i--)
	{
 		int ls = i*2;
		int lr = i*2+1;
			if (g[i] == 1)
			{
				for (int x = 0; x < 2; x++)
					for (int y = 0; y < 2; y++)
					{
						if (opt[ls][x] >= 0 && opt[lr][y] >= 0 && (opt[i][x&y] == -1 || opt[ls][x] + opt[lr][y] < opt[i][x&y]))
						{
							opt[i][x&y] = opt[ls][x] + opt[lr][y];
						}
					}
			}
			else
			{
				for (int x = 0; x < 2; x++)
					for (int y = 0; y < 2; y++)
					{
						if (opt[ls][x] >= 0 && opt[lr][y] >= 0 && (opt[i][x|y] == -1 || opt[ls][x] + opt[lr][y] < opt[i][x|y]))
						{
							opt[i][x|y] = opt[ls][x] + opt[lr][y];
						}
					}
			}
		if (c[i] == 1)
		{
			if (g[i] == 1)
			{
				for (int x = 0; x < 2; x++)
					for (int y = 0; y < 2; y++)
					{
						if (opt[ls][x] >= 0 && opt[lr][y] >= 0 && (opt[i][x|y] == -1 || opt[ls][x] + opt[lr][y]+1 < opt[i][x|y]))
						{
							opt[i][x|y] = opt[ls][x] + opt[lr][y]+1;
						}
					}
				
			}
			else
			{
				for (int x = 0; x < 2; x++)
					for (int y = 0; y < 2; y++)
					{
						if (opt[ls][x] >= 0 && opt[lr][y] >= 0 && (opt[i][x&y] == -1 || opt[ls][x] + opt[lr][y]+1 < opt[i][x&y]))
						{
							opt[i][x&y] = opt[ls][x] + opt[lr][y]+1;
						}
					}
			}
		}
	}
}


int main()
{
	int N;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		init();
		dp();
		cout << "Case #" << i+1 << ": " ;
		if (opt[1][v] == -1)
			cout << "IMPOSSIBLE";
		else
			cout << opt[1][v];
		cout << endl;
	}
}
