#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int n, t, m, k;
string dir[220];
string words1[200], words2[200];

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		printf("Case #%d: ", tt);
		scanf("%d%d\n", &n, &m);
		for (int i = 0; i < n; i++)
			getline(cin, dir[i]);
		dir[n++] = "";		
		int ans = 0;
		for (int i = 0; i < m; i++)
		{
			string s;
			int min = 1000;
			getline(cin, s);
//			cout << "s == " << s << endl;
			for (int j = 0; j < n; j++)
			{
				int cur = 0;
				bool ok = true;
				char c;
				string s2 = "";
				int k1 = 0, k2 = 0;
				for (int len = 0; len < s.length(); len++)
					if (s[len] == '/')
					{
						words1[k1++] = s2;
						s2 = "";
					}
					else
						s2 += s[len];
				words1[k1++] = s2;
				s2 = "";
				for (int len = 0; len < dir[j].length(); len++)
					if (dir[j][len] == '/')
					{
						words2[k2++] = s2;
						s2 = "";
					}
					else
						s2 += dir[j][len];
				words2[k2++] = s2;
//				printf("k1 == %d, k2 == %d\n", k1, k2);
				for (int k = 0; k < k1; k++)
					if (k2 == k || words1[k] != words2[k])
					{
//						cout << "w1 == " << words1[k] << " w2 == " << words2[k] << endl;
						cur = k1 - k;
						break;
					}
				if (cur < min)
					min = cur;
//				printf("j == %d\n, cur == %d\n", j, cur);
			}
			ans += min;
			if (min > 0)
				dir[n++] = s;
		}
		printf("%d\n", ans);
	}
	return 0;
}
