#include <iostream>
#include <algorithm>
#include <string.h>
#include <string>
#include <vector>

using namespace std;

const int MAXN = 12800;

int n;
int d[MAXN], l[MAXN];

//bool f[MAXN][MAXN];
int f[MAXN];

bool Work()
{
	cin >> n;
	d[0] = 0;  l[0] = 0;
	for (int i = 1; i <= n; i ++)
		cin >> d[i] >> l[i];
	cin >> d[n+1];   l[n+1] = 10000000;
	/*
	memset(f, false, sizeof(f));
	f[1][0] = true;

	for (int i = 1; i <= n; i ++)
		for (int j = i - 1; j >= 0; j --)
		{
			if (!f[i][j])  continue;
			for (int k = i + 1; k <= n + 1; k ++)
			{
				if (d[k] - d[i] > min(d[i] - d[j], l[i]))  break;
				f[k][i] = true;
				if (k == n + 1)  return true;
			}
		}

	for (int i = 0; i <= n; i ++)
		if (f[n+1][i])  return true;
*/
	memset(f, 0, sizeof(f));
	f[1] = d[1];
	for (int i = 1; i <= n; i ++)
		for (int j = i + 1; j <= n + 1 && d[i] + f[i] >= d[j]; j ++)
		{
			f[j] = max(f[j], min(d[j] - d[i], l[j]));
			if (d[j] + f[j] >= d[n+1])  return true;
		}

	if (f[n+1] > 0)  return true;
		
	return false;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin.sync_with_stdio(false);
	int T;
	cin >> T;
	for (int k = 1; k <= T; k ++)
	{
		cout << "Case #" << k << ": " << (Work()? "YES": "NO") << endl;
	}

	return 0;
}