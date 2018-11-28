#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

const int inf = 1000000;
const int maxn = 100 + 5;
const int maxm = 1000 + 5;
string name[maxn];
int f[maxm][maxn];

int main()
{
	int tCase;
	cin >> tCase; 
	for (int nCase = 1; nCase <= tCase; nCase ++)
	{
		int n, m;
		string tmps;
		cin >> n; getline(cin, tmps);
		for (int i = 0; i < n; i ++)
			getline(cin, name[i]);
		cin >> m; getline(cin, tmps);
		for (int i = 0; i < n; i ++)
			f[0][i] = 0;
		for (int i = 1; i <= m; i ++)
		{
			string nstr;
			getline(cin, nstr);
			for (int j = 0; j < n; j ++)
			{
				int tmp = inf;
				if (nstr != name[j])
					for (int k = 0; k < n; k ++)
						tmp = min(tmp, f[i - 1][k] + (j == k? 0: 1));
				f[i][j] = tmp;
			}
		}
		int ans = inf;
		for (int i = 0; i < n; i ++)
			ans = min(ans, f[m][i]);
		cout << "Case #" << nCase << ": " << ans << endl;
	}
}
