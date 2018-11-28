#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

FILE
	*fpi = fopen("A-small.in", "r"),
	*fpo = fopen("A-small.out", "w");

int main(int argc, char *argv[])
{
	int
		T;

	fscanf(fpi, "%d", &T);
	for (int i = 0; i < T; i++)
		{
		int
			N,
			Pd,
			Pg,
			D;

		bool
			bPoss = false;

		fscanf(fpi, "%d %d %d", &N, &Pd, &Pg);
		if (Pd == 0 || N > 99)
			bPoss = true;
		else
			{
			for (D = 1; D <= N; D++)
				if ((D * Pd) % 100 == 0)
					{
					bPoss = true;
					break;
					}
			}

		if (bPoss)
			if (Pg == 100 && Pd < 100)
				bPoss = false;
			else if (Pg == 0 && Pd > 0)
				bPoss = false;

		fprintf(fpo, "Case #%d: %s\n", i + 1, bPoss ? "Possible" : "Broken");
		}

	fclose(fpi);
	fclose(fpo);
	return 0;
}
