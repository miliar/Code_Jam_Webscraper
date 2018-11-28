#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>

using namespace std;

const int MaxN = 100;
//const char phrase[] = "welcome";
const char phrase[] = "welcome to code jam";
const int len = sizeof(phrase) - 1;

void main()
{
	int n;
	scanf("%d\n", &n);

	vector<int> idxCandidates[512];
	vector<int> pcount[512];

	for (int i = 1; i <= n; i++)
	{
		char line[512];
		gets(line);

		for (int j = 0; j < strlen(line) + 1; j++)
		{
			idxCandidates[j].clear();
			idxCandidates[j].reserve(len);
			pcount[j].clear();
			pcount[j].reserve(len);

			if (j == strlen(line))
			{
				idxCandidates[j].push_back(strlen(phrase));
				pcount[j].push_back(0);
				break;
			}

			//printf("chr %2d %c\n", j, line[j]);

			for (int k = len - 1; k >= 0; k--)
			{
				if (line[j] == phrase[k])
				{
					int kk = k - 1;
					for (int jj = j - 1; jj >= 0; jj--)
					{
						if (kk >= 0 && line[jj] == phrase[kk])
						{
							kk--;
						}
					}

					if (kk < 0)
					{
						idxCandidates[j].push_back(k);
						pcount[j].push_back(0);
						//printf("  candidate idx %d\n", k);
					}
				}
			}
		}

		for (int j = 0; j < strlen(line) + 1; j++)
		{
			for (int k = 0; k < (int)idxCandidates[j].size(); k++)
			{
				int idx = idxCandidates[j][k];

				//printf("chr %d %c idx %d\n", j, line[j], idx);
				if (idx == 0)
				{
					pcount[j][k] = 1;
				}
				else
				{
					for (int jj = j - 1; jj >= 0; jj--)
					{
						for (int kk = 0; kk < (int)idxCandidates[jj].size(); kk++)
						{
							int idx2 = idxCandidates[jj][kk];
							if (idx2 == idx - 1)
							{
								//printf("  add chr %d pcount %d (idx %d)\n", jj, pcount[jj][kk], idx2);
								pcount[j][k] = (pcount[j][k] + pcount[jj][kk]) % 10000;
							}
						}
					}
				}
				//printf("  - pcount %d\n", pcount[j][k]);
			}
		}

		printf("Case #%d: %04d\n", i, pcount[strlen(line)][0] % 10000);
	}
}
