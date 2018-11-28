
#include <iostream>

using namespace std;

const int g_nL = 16;
const int g_nD = 5000;
const int g_nN = 500;

bool  IsMatch(char* szWord, int* nPat)
{
	for (int i = 0; szWord[i]; i++)
	{
		if (0 == ((nPat[i] >> (szWord[i] - 'a')) & 1))
			return false;
	}

	return true;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("o.txt", "w", stdout);

	int nL, nD, nN;

	cin >> nL >> nD >> nN;

	char szDict[g_nD][g_nL];
	char szPat[g_nL * 32];

	for (int i = 0; i < nD; i++)
		scanf("%s", szDict[i]);

	int nPat[g_nL];
	for (int i = 0; i < nN; i++)
	{
		scanf("%s", szPat);

		memset(nPat, 0, sizeof(nPat));

		int k = 0;
		for (int j = 0; j < nL; j++)
		{
			if (szPat[k] == '(')
			{
				for (k++; szPat[k] != ')'; k++)
					nPat[j] |= (1 << (szPat[k] - 'a'));
			}
			else
			{
				nPat[j] = (1 << (szPat[k] - 'a'));
			}
			k++;
		}

		int nRes = 0;
		for (int j = 0; j < nD; j++)
			if (IsMatch(szDict[j], nPat))
				nRes++;

		cout << "Case #" << i + 1 << ": " << nRes << endl;
	}

	return 0;
}