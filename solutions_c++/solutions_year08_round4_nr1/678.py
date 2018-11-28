#include <iostream>
#include <string>
using namespace std;

#define INPUTFILENAME "A-large.in.txt"
#define OUTPUTFILENAME "output.txt"

const int maxm = 20000;
int m, v;
int g[maxm], c[maxm];

void init()
{
	cin >> m >> v;
	for (int i = 0; i < (m - 1) / 2; i++)
		cin >> g[i] >> c[i];
	for (int i = (m - 1) / 2; i < m; i++)
		cin >> g[i];
}

int calc(int node, int v)
{
	int tmp;
	if (node >= (m - 1) / 2) 
		if (g[node] == v) 
			return 0;
		else
			return m;
	if (v == 0)
		if (g[node] == 1)
			return min(calc(node + node + 1, 0), calc(node + node + 2, 0));
		else
		{
			tmp = calc(node + node + 1, 0) + calc(node + node + 2, 0);
			if (c[node] == 0)
				return tmp;
			else
				return min(tmp, min(calc(node + node + 1, 0), calc(node + node + 2, 0)) + 1);
		}
	else
		if (g[node] == 0)
			return min(calc(node + node + 1, 1), calc(node + node + 2, 1));
		else
		{
			tmp = calc(node + node + 1, 1) + calc(node + node + 2, 1);
			if (c[node] == 0)
				return tmp;
			else
				return min(tmp, min(calc(node + node + 1, 1), calc(node + node + 2, 1)) + 1);
		}
}

void solve(int testnumber)
{
	int ans = calc(0, v);
	cout << "Case #" << testnumber << ": ";
	if (ans >= m)
		cout << "IMPOSSIBLE" << endl;
	else
		cout << ans << endl;
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