#include <stdio.h>
#include <map>
#include <string>
#include <iostream>
#include <vector>
using namespace std;

int ans[1001][101];
vector<int> words;
map<string, int> enignes;



int main()
{
	int n;
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);

	scanf("%d\n", &n);
	for (int i = 0; i < n; i ++)
	{
		int q, k;
		scanf("%d\n", &q);
		enignes.clear();
		string s;
		char st[300];
		for (int j = 0; j < q ;j ++)
		{
			gets(st);
			s = st;
			enignes[s] = j;
			ans[0][j] = 0;
		}

		scanf("%d\n", &k);
		if (k == 0)
		{
			printf("Case #%d: 0\n", i+1);
			continue;
		}
		words.resize(k);
		for (int j = 0; j < k; j ++)
		{
			gets(st);
			s = st;
			words[j] = enignes[s];
		}
		int m;
		int last = 0;
		for (int j = 1; j <= k; j ++)
		{
			m = j+1;
			for (int t = 0; t < q; t ++)
				if (ans[j-1][t] != -1 && ans[j-1][t] < m)
					m = ans[j-1][t];
			if (ans[j-1][last] == -1)			
				ans[j-1][last] = m+1;
			for (int t = 0; t < q; t ++)
				if (t != words[j-1])
					ans[j][t] = ans[j-1][t];
				else
					ans[j][t] = -1;
			last = words[j-1];
		}
		m = k+1;
		for (int t = 0; t < q; t ++)
			if (ans[k][t] != -1 && ans[k][t] < m)
				m = ans[k][t];
		
		printf("Case #%d: %d\n", i+1, m);
	}
	return 0;
}