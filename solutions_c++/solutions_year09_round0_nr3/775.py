
#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

const int g_nN = 512;
const int g_nMod = 10000;

class Welcome
{
private:
public:
	int Count(char* szText, char* szInput)
	{
		int nN = strlen(szText), nM = strlen(szInput);
		if (nN > nM)
			return 0;

		int nDP[2][g_nN];

		int ii = 0;
		if (szText[0] == szInput[0])
			nDP[ii][0] = 1;
		else
			nDP[ii][0] = 0;
		for (int j = 1; j < nM; j++)
		{
			if (szText[0] == szInput[j])
				nDP[ii][j] = nDP[ii][j - 1] + 1;
			else
				nDP[ii][j] = nDP[ii][j - 1];
		}

		ii ^= 1;
		for (int i = 1; i < nN; i++, ii ^= 1)
		{
			nDP[ii][i - 1] = 0;
			for (int j = i; j < nM; j++)
			{
				if (szText[i] == szInput[j])
					nDP[ii][j] = nDP[1 ^ ii][j - 1] + nDP[ii][j - 1];
				else
					nDP[ii][j] = nDP[ii][j - 1];

				if (nDP[ii][j] >= g_nMod)
					nDP[ii][j] -= g_nMod;
			}
		}

		return nDP[1 ^ ii][nM - 1];
	}
};

int main()
{
	freopen("s.txt", "r", stdin);
	freopen("o.txt", "w", stdout);

	int nTC;
	cin >> nTC;
	getchar();

	Welcome wel;

	char szText[] = "welcome to code jam";
	char szInput[g_nN];

	for (int nC = 1; nC <= nTC; nC++)
	{
		gets(szInput);

		printf("Case #%d: %04d\n", nC, wel.Count(szText, szInput));
	}

	return 0;
}