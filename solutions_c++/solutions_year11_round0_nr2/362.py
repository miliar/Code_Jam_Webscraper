#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string>
using namespace std;

FILE
	*fpi = fopen("B-large.in", "r"),
	*fpo = fopen("B-large.out", "w");

typedef struct tagCombine
{
	tagCombine(char a = 0, char b = 0, char c = 0)
	{
		cBaseElem1 = a;
		cBaseElem2 = b;
		cNonBaseElem = c;
	}

	char
		cBaseElem1,
		cBaseElem2,
		cNonBaseElem;
} COMBINE;

typedef struct tagOppose
{
	tagOppose(char a = 0, char b = 0)
	{
		cBaseElem1 = a;
		cBaseElem2 = b;
	}

	char
		cBaseElem1,
		cBaseElem2;
} OPPOSE;

bool match(char a, char b, char x, char y)
{
	return ((a == x && b == y) || (a == y && b == x));
}

int
	T;

int main(int argc, char *argv[])
{
	fscanf(fpi, "%d", &T);
	for (int i = 0; i < T; i++)
		{
		int
			C,
			D,
			N;

		COMBINE
			combines[36];

		OPPOSE
			opposes[28];

		char
			sIn[101];

		string
			sOut;

		fscanf(fpi, "%d", &C);
		for (int j = 0; j < C; j++)
			{
			fscanf(fpi, "%s", sIn);
			combines[j] = COMBINE(sIn[0], sIn[1], sIn[2]);
			}

		fscanf(fpi, "%d", &D);
		for (int j = 0; j < D; j++)
			{
			fscanf(fpi, "%s", sIn);
			opposes[j] = OPPOSE(sIn[0], sIn[1]);
			}

		fscanf(fpi, "%d", &N);
		fscanf(fpi, "%s", sIn);

		for (int j = 0; j < N; j++)
			{
			sOut += sIn[j];

			int
				nLen = sOut.length(),
				k;

			if (nLen > 1)
				{
				for (k = 0; k < C; k++)
					if (match(sOut[nLen - 2], sOut[nLen - 1], combines[k].cBaseElem1, combines[k].cBaseElem2))
						{
						sOut = sOut.substr(0, nLen - 2) + combines[k].cNonBaseElem;
						break;
						}

				if (k == C)
					for (k = 0; k < D; k++)
						{
						if ((sOut.find(opposes[k].cBaseElem1) != string::npos) && (sOut.find(opposes[k].cBaseElem2) != string::npos))
							{
							sOut.clear();
							break;
							}
						}

				}
			}

		fprintf(fpo, "Case #%d: [", i + 1);

		for (int j = 0, size = sOut.length(); j < size; j++)
			{
			fprintf(fpo, "%c", sOut[j]);

			if (j < size - 1)
				fprintf(fpo, ", ", sOut[j]);
			}

		fprintf(fpo, "]\n");
		}

	fclose(fpi);
	fclose(fpo);
	return 0;
}
