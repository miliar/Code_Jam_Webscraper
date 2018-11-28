#include<iostream>
#include<string>
using namespace std;

const int maxn = 5555;
const int maxm = 555;

int n, m, l, x, ans;
string a[maxn];
bool f[maxm][26];
string s;
bool flag;



int main()
{
	freopen(".in","r",stdin);
	freopen(".out","w",stdout);
	cin >> l >> n >> m;
	for (int i = 0; i < n; i++)
		cin >> a[i];

	for (int k = 0; k < m; k++)
	{
		cin >> s;
		memset(f, 0, sizeof(f));
		x = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == '(') flag = true; else
			if (s[i] == ')')
			{
				x++;
				flag = false;
			} else
			{
//				cout << x << " " << s[i] - 'a' << endl;
				f[x][s[i] - 'a'] = true;
				x += (flag == false);
			}
		}
		ans = 0;
		for (int i = 0; i < n; i++)
		{
			if (a[i].size() != x) continue;
			ans++;
			for (int j = 0; j < a[i].size(); j++)
				if (! f[j][a[i][j] - 'a'])
				{
					ans--;
					break;
				}
		}
		cout << "Case #" << k + 1 << ": " << ans << endl;
	}
	return 0;
}
