#include<iostream>
#include<string>
using namespace std;

const int maxd = 5000;
const int maxl = 15;
int l, d, n;
string a[maxd];
bool mark[maxl][26];

int main()
{
	freopen("p1.in", "r", stdin);
	freopen("p1.out", "w", stdout);
	cin >> l >> d >> n;
	for (int i = 0; i < d; i++) cin >> a[i];
	for (int T = 1; T <= n; T++)
	{
		cout << "Case #" << T << ": " ;
		string z;
		cin >> z;
		bool flag = false;
		memset(mark, 0, sizeof(mark));
		for (int p = 0, cur = 0; p < z.size(); p++)
		{
			if (z[p] == '(') { flag = true; continue; }
			if (z[p] == ')') { flag = false; cur++; continue; }
			if (flag) mark[cur][z[p] - 'a'] = true;
			else mark[cur++][z[p] - 'a'] = true;
		}
		int ans = 0;
		for (int i = 0; i < d; i++)
		{
			flag = true;
			for (int j = 0; j < l; j++)
				if (!mark[j][a[i][j] - 'a'])
				{
					flag = false; break;
				}
			ans += flag;
		}
		cout << ans << endl;
	}
	return 0;
}
