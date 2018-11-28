#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

FILE
	*fpi = fopen("A-large.in", "r"),
	*fpo = fopen("A-large.out", "w");

// Code uses int 0 for Orange and 1 for Blue

typedef struct tagBUTTONPRESS
{
	tagBUTTONPRESS(int c = -1, int n = 0)
	{
		nColor = c;
		nPos   = n;
	}

	int
		nColor,
		nPos;

} BUTTONPRESS;

int
	T;

int main(int argc, char *argv[])
{
	fscanf(fpi, "%d", &T);
	for (int i = 0; i < T; i++)
		{
		int
			N,
			nColor,
			nPos,
			nCountByColor[2] = { 0 },
			nRobotPos[2] = { 1, 1 },
			nSlice = 0;

		char
			s[100];

		BUTTONPRESS
			all[100],
			*pFilteredByColor[2][101] = { NULL },
			*pNext = &all[0],
			**ppNextByColor[2] = { &pFilteredByColor[0][0], &pFilteredByColor[1][0] };

		fscanf(fpi, "%d", &N);
		for (int j = 0; j < N; j++)
			{
			fscanf(fpi, "%s", s);
			fscanf(fpi, "%d", &nPos);
			nColor = (s[0] == 'B' ? 1 : 0);
			all[j] = BUTTONPRESS(nColor, nPos);
			pFilteredByColor[nColor][nCountByColor[nColor]] = &all[j];
			nCountByColor[nColor]++;
			}

		while (*ppNextByColor[0] || *ppNextByColor[1])
			{
			bool
				bButtonPress = false;

			for (int k = 0; k < 2; k++)
				{
				if (!*ppNextByColor[k])
					continue;

				sprintf(s, "k = %d, robot = %d, next button = %d\n", k, nRobotPos[k], (*ppNextByColor[k])->nPos);

				if (nRobotPos[k] == (*ppNextByColor[k])->nPos)
					{
					if (*ppNextByColor[k] == pNext)
						{
						bButtonPress = true;
						ppNextByColor[k]++;
						}
					}
				else if (nRobotPos[k] < (*ppNextByColor[k])->nPos)
					nRobotPos[k]++;
				else
					nRobotPos[k]--;
				}

			if (bButtonPress)
				pNext++;

			nSlice++;
			}

		fprintf(fpo, "Case #%d: %d\n", i + 1, nSlice);
		}

	fclose(fpi);
	fclose(fpo);
	return 0;
}
