#include <iostream>
#include <string>

using namespace std;

int				L, D, N;
string			word[5000];
bool			hash[15][30];

int	main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> L >> D >> N;
	for (int i = 0; i < D; ++i) cin >> word[i];

	for (int ncase = 0; ncase < N; ++ncase)
	{
		string pat;
		cin >> pat;
		int count = 0;
		memset(hash, 0, sizeof(hash));
		for (int i = 0, k = 0; i < pat.size(); ++i, ++k)
		{
			if (pat[i] == '(')
			{
				int j = i + 1;
				while (pat[j] != ')') 
				{
					hash[k][pat[j] - 'a'] = true;
					++j;
				}
				i = j;
			} else
				hash[k][pat[i] - 'a'] = true;
		}

		for (int i = 0; i < D; ++i)
		{
			bool pass = 1;
			for (int j = 0; j < L; ++j)
				if (hash[j][word[i][j] - 'a'] == 0)
				{
					pass = 0;
					break;
				}
			count += (int)pass;
		}
		printf("Case #%d: %d\n", ncase + 1, count);
	}
	return 0;
}