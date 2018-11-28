
	#include <stdio.h>
	#include <string.h>
	
	using namespace std;

	char buffer[64];
	char grid[4][4];

    char *getline (FILE *fp)
    {
        char *p;

		if (!fgets (buffer, sizeof(buffer), fp)) return NULL;

		p = strchr (buffer, '\n');
		if (p) *p = '\0';

		return buffer;
    }

	void eatWhiteSpace (FILE *fp)
	{
		int ch;
		
		while (1) {
			ch = getc(fp);
			if (ch == EOF || ch > 32) break;
		}

		if (ch != EOF) ungetc(ch, fp);
	}

	int checkVertical (int v)
	{
		int i, j, k;

		for (i = 0; i < 4; i++)
		{
			for (j = k = 0; j < 4; j++)
			{
				if (grid[j][i] == v || grid[j][i] == 'T')
					k++;
			}

			if (k == 4) return 1;
		}

		return 0;
	}

	int checkHorizontal (int v)
	{
		int i, j, k;

		for (i = 0; i < 4; i++)
		{
			for (j = k = 0; j < 4; j++)
			{
				if (grid[i][j] == v || grid[i][j] == 'T')
					k++;
			}

			if (k == 4) return 1;
		}

		return 0;
	}

	int checkDiagonal (int v)
	{
		int i, j, k;

		for (i = k = 0; i < 4; i++)
		{
			if (grid[i][i] == v || grid[i][i] == 'T')
				k++;
		}

		if (k == 4) return 1;

		for (i = k = 0; i < 4; i++)
		{
			if (grid[i][3-i] == v || grid[i][3-i] == 'T')
				k++;
		}

		if (k == 4) return 1;

		return 0;
	}

	int checkEmpty ()
	{
		int i, j;

		for (i = 0; i < 4; i++)
		for (j = 0; j < 4; j++)
			if (grid[i][j] == '.') return 1;

		return 0;
	}

	char *gameResult ()
	{
		int xv, ov;

		xv = checkVertical('X') + checkHorizontal('X') + checkDiagonal('X');
		ov = checkVertical('O') + checkHorizontal('O') + checkDiagonal('O');

		if (xv && ov)
			return "Draw";

		if (xv)
			return "X won";

		if (ov)
			return "O won";

		return checkEmpty() ? "Game has not completed" : "Draw";
	}

	int main (int argc, char *argv[])
	{
		FILE *fp;
		char *line;
		int testCase, testCases;

		if (argc < 2)
		{
			printf ("Use: main <input-file>\n");
			return -1;
		}

		fp = fopen (argv[1], "rt");
		if (!fp) return -2;

		sscanf(getline(fp), "%u", &testCases);

		for (testCase = 1; testCase <= testCases; testCase++)
		{
			memcpy(&grid[0], getline(fp), 4);
			memcpy(&grid[1], getline(fp), 4);
			memcpy(&grid[2], getline(fp), 4);
			memcpy(&grid[3], getline(fp), 4);

			eatWhiteSpace(fp);

			printf ("Case #%u: %s\n", testCase, gameResult());
		}

		fclose(fp);
		return 0;
	}
