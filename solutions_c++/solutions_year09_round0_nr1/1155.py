#include <stdio.h>
#include <vector>
using namespace std;

int L, D, N;
vector<int> tab[15][26];
int ret[5000];
char buff[2048];

int main()
{
	scanf("%d%d%d", &L, &D, &N);

	for (int i = 0; i < D; i++)
	{
		scanf("%s", buff);
		for (int j = 0; j < L; j++)
		{
			tab[j][buff[j]-'a'].push_back(i);
		}
	}

	for (int i = 1; i <= N; i++)
	{
		memset(ret, 0, sizeof(ret));
		scanf("%s", buff);
		int j = 0;
		bool flag = false;
		for (char *p = buff; *p != '\0'; p++)
		{
			char ch = *p;
			switch (ch)
			{
			case '(':
				flag = true;
				break;
			case ')':
				flag = false;
				j++;
				break;
			default:
				for (vector<int>::iterator it = tab[j][ch-'a'].begin(); it != tab[j][ch-'a'].end(); ++it)
				{
					ret[*it]++;
				}
				if (!flag) j++;
			}
		}
		int count = 0;
		for (int j = 0; j < D; j++)
		{
			if (ret[j] == L) count++;
		}
		printf("Case #%d: %d\n", i, count);
	}

	return 0;
}