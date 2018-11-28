#include <iostream>
#include <string>
using namespace std;

#define INPUTFILENAME "C-small-attempt3.in.txt"
#define OUTPUTFILENAME "output.txt"
template<class T> inline void smaller(T &a,T b){if(b<a) a=b;}
template<class T> inline void larger(T &a,T b){if(b>a) a=b;}

const int maxm = 15;
int map[maxm];
int adj[1100][1100];
int f[maxm][1100];
int m, n;
int sum[1100];

void init()
{
	string st;
	memset(map, 0, sizeof(map));
	memset(sum, 0, sizeof(sum));
	cin >> m >> n;
	for (int i = 0; i < m; i++)
	{
		cin >> st;
		for (int j = 0; j < n; j++)
			if (st[j] == 'x')
				map[i] += 1 << j;
	}
	for (int i = 0; i < 1 << n; i++)
	{
		sum[i] = 0;
		for (int j = 0; j < n; j++)
			if ((i & (1 << j)) > 0)
				sum[i]++;
		for (int j = 0; j < 1 << n; j++)
			if ((((i + i) & j) == 0) && ((i & (j + j)) == 0))
				adj[i][j] = 1;
			else 
				adj[i][j] = 0;
	}
}

void solve(int testnumber)
{
	for (int j = 0; j < (1 << n); j++)
		if ((map[0] & j) == 0 && (adj[j][j])) 
			f[0][j] = sum[j];
		else
			f[0][j] = 0;

	for (int i = 1; i < m; i++)
		for (int j = 0; j < (1 << n); j++)
		{
			f[i][j] = 0;
			if ((map[i] & j) == 0 && (adj[j][j]))
				for (int k = 0; k < 1 << n; k++)
					if (((map[i - 1] & k) == 0) && (adj[j][k]) && (adj[k][k]))
						larger(f[i][j], f[i - 1][k] + sum[j]);
		}
	
	int ans = 0;
	for (int j = 0; j < 1 << n; j++)
		larger(ans, f[m - 1][j]);

	cout << "Case #" << testnumber << ": " << ans << endl;
}	

int main()
{
	int testnumber;
	freopen(INPUTFILENAME, "r", stdin);
	freopen(OUTPUTFILENAME, "w", stdout);
	cin >> testnumber;
	for (int i = 0; i < testnumber; i++)
	{
		init();
		solve(i + 1);
	}
	return 0;
}