#include<iostream>
#include<string>
#include<cmath>

using namespace std;

string s[300];

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int N,M;
		cin >> N >> M;
		for (int i = 0; i < N; i++) cin >> s[i];
		for (int i = 0; i < M; i++) cin >> s[i + N];
		int ans = 0;
		for (int i = 0; i < M + N; i++) s[i] += "/";
		for (int i = N; i < M + N; i++)
		{
			int m = 0;
			for (int j = 0; j < i; j++)
			{
				int p = 0;
				for (int k = 0; k < min(s[i].length(),s[j].length()); k++)
				{
					if (s[i][k] != s[j][k]) p = k;
					if (p != 0) break;
				}
				if (p == 0) p = min(s[i].length(),s[j].length()) + 1;
				p --;
				if (p > m) m = p;
			}
			for (int j = m + 1; j < s[i].length(); j++)
				if (s[i][j] == '/') ans++;
		}
		cout << "Case #" << t + 1 << ": " << ans << "\n";
	}
}
