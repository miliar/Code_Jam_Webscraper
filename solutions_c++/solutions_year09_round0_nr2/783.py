
#include <cstring>
#include <iostream>

using namespace std;

const int g_nN = 100;

typedef struct SPos
{
	int nR, nC;
}SPos;

int g_dR[] = {-1, 0, 0, 1};
int g_dC[] = {0, -1, 1, 0};

int Next(int nMap[g_nN][g_nN], int nH, int nW, const SPos& sPos)
{
	int nMinAlt = nMap[sPos.nR][sPos.nC], nMinIdx = -1;
	for (int i = 0; i < 4; i++)
	{
		SPos sNPos;
		sNPos.nR = sPos.nR + g_dR[i];
		sNPos.nC = sPos.nC + g_dC[i];

		if (sNPos.nR < 0 || sNPos.nR >= nH)
			continue;
		if (sNPos.nC < 0 || sNPos.nC >= nW)
			continue;

		if (nMap[sNPos.nR][sNPos.nC] < nMinAlt)
		{
			nMinAlt = nMap[sNPos.nR][sNPos.nC];
			nMinIdx = i;
		}
	}

	return nMinIdx;
}

int main()
{
	freopen("s.txt", "r", stdin);
	freopen("o.txt", "w", stdout);

	int nTC;
	int nMap[g_nN][g_nN];
	SPos sPrev[g_nN][g_nN];

	cin >> nTC; 
	for (int nC = 1; nC <= nTC; nC++)
	{
		int nH, nW;

		cin >> nH >> nW;

		for (int i = 0; i < nH; i ++)
			for (int j = 0; j < nW; j++)
				cin >> nMap[i][j];

		for (int i = 0; i < nH; i++)
			for (int j = 0; j < nW; j++)
			{
				SPos sTmp;
				sTmp.nR = i; 
				sTmp.nC = j;

				int nNext = Next(nMap, nH, nW, sTmp);

				if (nNext < 0)
				{
					sPrev[i][j].nR = i;
					sPrev[i][j].nC = j;
				}
				else
				{
					sPrev[i][j].nR = i + g_dR[nNext];
					sPrev[i][j].nC = j + g_dC[nNext];
				}
			}

			memset(nMap, 0, sizeof(nMap));
			int k = 1;

			for (int i = 0; i < nH; i++)
				for (int j = 0; j < nW; j++)
				{
					if (0 == nMap[i][j])
					{
						SPos sTmp = sPrev[i][j];

						int nMark = 0;
						for (; ; )
						{
							if (nMap[sTmp.nR][sTmp.nC])
							{
								nMark = nMap[sTmp.nR][sTmp.nC];
								break;
							}

							SPos sFat = sPrev[sTmp.nR][sTmp.nC];
							if (sFat.nR == sTmp.nR && sFat.nC == sTmp.nC)
								break;

							sTmp = sFat;
						}

						if (nMark == 0)
							nMark = k++;

						sTmp.nR = i;
						sTmp.nC = j;
						for (; ; )
						{
							if (nMap[sTmp.nR][sTmp.nC])
								break;

							nMap[sTmp.nR][sTmp.nC] = nMark;

							SPos sFat = sPrev[sTmp.nR][sTmp.nC];
							if (sFat.nR == sTmp.nR && sFat.nC == sTmp.nC)
								break;

							sTmp = sFat;
						}
					}
				}

				cout << "Case #" << nC << ':' << endl;
				for (int i = 0; i < nH; i++)
					for (int j = 0; j < nW; j++)
					{
						cout << char('a' + nMap[i][j] - 1);
						if (j < nW - 1)
							cout << ' ';
						else
							cout << endl;
					}
	}

	return 0;
}