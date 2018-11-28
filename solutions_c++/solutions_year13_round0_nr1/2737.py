/******************************************************************************
 * Directives
 *****************************************************************************/
#ifdef WIN32
#define _CRT_SECURE_NO_WARNINGS
#endif

/******************************************************************************
 * Header Files
 *****************************************************************************/
#include <stdio.h>

/******************************************************************************
 * Constants, Macros, Typedefs, Enums & Structures
 *****************************************************************************/

/******************************************************************************
 * Global & Static Variables
 *****************************************************************************/
int g_N;
char g_data[4][4];

static char *RESULT[4] = {
	" Draw\n",
	" O won\n",
	" X won\n",
	" Game has not completed\n"
};

/******************************************************************************
 * Global & Static Function Prototypes
 *****************************************************************************/
void runCase();

/******************************************************************************
 * Function Implementations
 *****************************************************************************/
int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <=T; t++) {
		printf("Case #%d:", t);
		runCase();
	}

	return 0;
}

int chkData()
{
	// chk row
	for (int row = 0; row < 4; row++) {
		char a = g_data[row][0];
		for (int col = 1; col < 4; col++) {
			if (g_data[row][col] == 'T') {
				// go next
			} else if (a == 'T') {
				// update
				a = g_data[row][col];
			} else if (a != g_data[row][col]) {
				a = '.';
				break;
			}
		}
		if (a == 'O') {
			return 1;
		} else if (a == 'X') {
			return 2;
		}
	}
	// chk col
	for (int col = 0; col < 4; col++) {
		char a = g_data[0][col];
		for (int row = 1; row < 4; row++) {
			if (g_data[row][col] == 'T') {
				// go next
			} else if (a == 'T') {
				// update
				a = g_data[row][col];
			} else if (a != g_data[row][col]) {
				a = '.';
				break;
			}
		}
		if (a == 'O') {
			return 1;
		} else if (a == 'X') {
			return 2;
		}
	}
	// chk diagonal 1
	{
		char a = g_data[0][0];
		for (int row = 1; row < 4; row++) {
			int col = row;
			if (g_data[row][col] == 'T') {
				// go next
			} else if (a == 'T') {
				// update
				a = g_data[row][col];
			} else if (a != g_data[row][col]) {
				a = '.';
				break;
			}
		}
		if (a == 'O') {
			return 1;
		} else if (a == 'X') {
			return 2;
		}
	}
	// chk diagonal 2
	{
		char a = g_data[0][3];
		for (int row = 1; row < 4; row++) {
			int col = 3 - row;
			if (g_data[row][col] == 'T') {
				// go next
			} else if (a == 'T') {
				// update
				a = g_data[row][col];
			} else if (a != g_data[row][col]) {
				a = '.';
				break;
			}
		}
		if (a == 'O') {
			return 1;
		} else if (a == 'X') {
			return 2;
		}
	}
	{
		for (int i = 0; i < 16; i++) {
			if (g_data[0][i] == '.') {
				return 3;
			}
		}
	}
	return 0;
}

void runCase()
{
	char line[32];

	for (int i = 0; i < 4; i++) {
		scanf("%s", line);
		g_data[i][0] = line[0];
		g_data[i][1] = line[1];
		g_data[i][2] = line[2];
		g_data[i][3] = line[3];
	}

	int ret = chkData();
	printf(RESULT[ret]);
}
