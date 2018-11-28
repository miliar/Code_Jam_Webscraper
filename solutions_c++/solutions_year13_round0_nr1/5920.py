#include <stdio.h>
#include <memory>
#include <cassert>

#define noPRINT_INPUT
#define SIZE 4
	
static const char NOT_COMPLETED[] = "Game has not completed";
static const char X_WON[] = "X won";
static const char O_WON[] = "O won";
static const char DRAW[] = "Draw";

class Case {
public:
	Case() 
	{
		memset(mTable, 0, SIZE*SIZE);
		mNotCompleted = false;
	}
	virtual ~Case() {}

	const char* result()
	{
		const char* result = DRAW;

		// check row/col
		for (int i=0; i<SIZE; ++i)
		{
			// check row
			char rowc = 0;
			bool rows = true;

			char colc = 0;
			bool cols = true;


			int j;
			for (j=0; j<SIZE; ++j)
			{
				if (rows)
				{
					rows = check(mTable[i][j], &rowc);
				}

				if (cols)
				{
					cols = check(mTable[j][i], &colc);
				}
			}

			if (rows)
			{
				if (rowc == 'O')
				{
					result = O_WON;
					break;
				}
				else
				{
					assert(rowc == 'X');
					result = X_WON;
					break;
				}
			}

			if (cols)
			{
				if (colc == 'O')
				{
					result = O_WON;
					break;
				}
				else
				{
					assert(colc == 'X');
					result = X_WON;
					break;
				}
			}

		}

		// check diag
		if (result == DRAW)
		{
			char downc = 0;
			bool downs = true;

			char upc = 0;
			bool ups = true;

			for (int i=0; i<SIZE; ++i)
			{
				if (downs)
				{
					downs = check(mTable[i][i], &downc);
				}

				if (ups)
				{
					ups = check(mTable[i][SIZE-(i+1)], &upc);
				}
			}

			if (downs)
			{
				if (downc == 'O')
				{
					result = O_WON;
				}
				else
				{
					assert(downc == 'X');
					result = X_WON;
				}
			}
			else if (ups)
			{
				if (upc == 'O')
				{
					result = O_WON;
				}
				else
				{
					assert(upc == 'X');
					result = X_WON;
				}
			}
		}

		// check if not completed
		if ((result == DRAW) && (mNotCompleted))
		{
			result = NOT_COMPLETED;
		}

		return result;
	}


	char mTable[SIZE][SIZE];

private:
	bool check(char c, char* lastc)
	{
		bool cont = true;

		if (c == '.')
		{
			mNotCompleted = true;
			cont = false;
		}
		else if (c == 'X')
		{
			if (*lastc == 0)
			{
				*lastc = 'X';
			}
			else if (*lastc != 'X')
			{
				cont = false;
			}
		}
		else if (c == 'O')
		{
			if (*lastc == 0)
			{
				*lastc = 'O';
			}
			else if (*lastc != 'O')
			{
				cont = false;
			}
		}

		return cont;
	}

	bool mNotCompleted;
};

int main(int argc, char** argv)
{
	FILE* in = fopen(argv[1], "r");
	assert(in != NULL);

	int T = 0;
	fscanf(in, "%d\n", &T);
#ifdef PRINT_INPUT
	printf("T:%d\n", T);
#endif

	for (int t=0; t<T; ++t)
	{
		Case c;

		for (int i=0; i<SIZE; ++i)
		{
			fscanf(in, "%c%c%c%c\n", 
				&(c.mTable[i][0]),
				&(c.mTable[i][1]),
				&(c.mTable[i][2]),
				&(c.mTable[i][3]));
#ifdef PRINT_INPUT
			printf("%c%c%c%c\n",
				(c.table[i][0]),
				(c.table[i][1]),
				(c.table[i][2]),
				(c.table[i][3]));
#endif

		}
#ifdef PRINT_INPUT
		printf("\n");
#endif

		printf("Case #%d: %s\n", (t+1), c.result());
	}

	fclose(in);
}