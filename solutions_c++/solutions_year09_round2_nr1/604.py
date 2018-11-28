#include <iostream>
#include <string>
#include <sstream>
#include <set>

using namespace std;

string fea[20000];
double P[20000];
bool vis[20000];
set<string> hash;


int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++)
	{
		int L;
		cin >> L;
		string s;
		int now = 0;
		memset(vis, 0, sizeof(vis));
		vis[1] = true;
		while (1)
		{
			cin >> s;
			if (s[0] == '(')
			{
				if (now == 0)
					now = 1;
				else
				{
					if (!vis[now<<1])
					{
						vis[now<<1] = true;
						now <<= 1;
					}
					else
					{
						vis[now+now+1] = true;
						now = now+now+1;
					}
				}
				s.erase(0, 1);
			}
			if (s.length() > 0)
			{
				if (s[0] == ')')
				{
					for (int i = 0; i < s.length(); i++)
						now >>= 1;
				}
				else
				{
					if (s[s.length()-1] == ')')
					{
						s.erase(s.length()-1, 1);
						if (s.length() > 0)
						{
							istringstream sin(s);
							sin >> P[now];
						}
						now >>= 1;
					}
					else
					{
						if (s[0] >= 'a' && s[0] <= 'z')
							fea[now] = s;
						else
						{
							istringstream sin(s);
							sin >> P[now];
						}
					}
				}
			}
			if (now == 0) break;
		}
		int N;
		cin >> N;
		cout << "Case #" << tt << ":" << endl;
		for (int i = 0; i < N; i++)
		{
			cin >> s;
			int M;
			cin >> M;
			hash.clear();
			for (int j = 0; j < M; j++)
			{
				cin >> s;
				hash.insert(s);
			}
			now = 1;
			double ans = 1.0;
			while (vis[now])
			{
				ans *= P[now];
				if (hash.count(fea[now]))
					now <<= 1;
				else
					now = now+now+1;
			}
			cout.precision(7);
			cout << fixed;
			cout << ans << endl;
		}
	}
}