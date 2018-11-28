#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

char s[120];

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		char comb[26][26];
		fill_n(comb[0], 26*26, -1);
		bool opp[26][26];
		fill_n(opp[0], 26*26, false);
		
		int C;
		scanf("%d", &C);
		for (int c = 0; c < C; c++)
		{
			scanf("%s", s);
			s[0] -= 'A';
			s[1] -= 'A';
			comb[s[1]][s[0]] = comb[s[0]][s[1]] = s[2] - 'A';
		}
		
		int D;
		scanf("%d", &D);
		for (int d = 0; d < D; d++)
		{
			scanf("%s", s);
			s[0] -= 'A';
			s[1] -= 'A';
			opp[s[0]][s[1]] = opp[s[1]][s[0]] = true;
		}
		
		vector<char> inv;
		
		int N;
		scanf("%d", &N);
		scanf("%s", s);
		for (int i = 0; i < N; i++)
		{
			char r;
			s[i] -= 'A';
			if (inv.size() > 0 && (r = comb[s[i]][*inv.rbegin()]) >= 0)
			{
				inv.pop_back();
				inv.push_back(r);
			}
			else
			{
				int j;
				for (j = 0; j < int(inv.size()); j++)
					if (opp[s[i]][inv[j]])
						break;
				if (j < int(inv.size()))
					inv.clear();
				else
					inv.push_back(s[i]);
			}
		}
		
		printf("Case #%d: [", t);
		for (int i = 0; i < int(inv.size()); i++)
			printf("%c%s", inv[i] + 'A', i < int(inv.size()) - 1 ? ", ":"");
		puts("]");
	}
	return 0;
}
