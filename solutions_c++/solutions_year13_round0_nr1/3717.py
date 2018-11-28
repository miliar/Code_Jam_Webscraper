#include "stdio.h"
#include "string.h"
#include "math.h"

#define debug(...) 
//#define debug(...) printf("[debug]");printf(__VA_ARGS__);

#define equals(x, y, b) ((m[x][y] == b) || (m[x][y] == 'T'))

#define row_equals(a, b) (equals(a, 0, b) && equals(a, 1, b) && equals(a, 2, b) && equals(a, 3, b))
#define col_equals(a, b) (equals(0, a, b) && equals(1, a, b) && equals(2, a, b) && equals(3, a, b))

#define diag1_equals(b) (equals(0, 0, b) && equals(1, 1, b) && equals(2, 2, b) && equals(3, 3, b))
#define diag2_equals(b) (equals(0, 3, b) && equals(1, 2, b) && equals(2, 1, b) && equals(3, 0, b))
#define diag_equals(b) (diag1_equals(b) || diag2_equals(b))
#define win(b) (\
		row_equals(0, b) || row_equals(1, b) || row_equals(2, b) || row_equals(3, b) ||\
		col_equals(0, b) || col_equals(1, b) || col_equals(2, b) || col_equals(3, b) ||\
		diag1_equals(b) || diag2_equals(b))

#define row_contains(a, b) ((m[a][0] == b) || (m[a][1] == b) || (m[a][2] == b) || (m[a][3] == b) )
#define col_contains(a, b) ((m[0][a] == b) || (m[1][a] == b) || (m[2][a] == b) || (m[3][a] == b) )
#define any_contains(b) (row_contains(0, b) || row_contains(1, b) || row_contains(2, b) || row_contains(3, b))

int main()
{
	char m[4][4];
	int i, num;
	scanf("%d\n", &num);
	
	for (i = 1; i <= num; ++i)
	{
		scanf("%c%c%c%c\n", &(m[0][0]), &(m[0][1]), &(m[0][2]), &(m[0][3]));
		scanf("%c%c%c%c\n", &(m[1][0]), &(m[1][1]), &(m[1][2]), &(m[1][3]));
		scanf("%c%c%c%c\n", &(m[2][0]), &(m[2][1]), &(m[2][2]), &(m[2][3]));
		scanf("%c%c%c%c\n", &(m[3][0]), &(m[3][1]), &(m[3][2]), &(m[3][3]));

		debug ("%c%c%c%c\n", (m[0][0]), (m[0][1]), (m[0][2]), (m[0][3]));
		debug ("%c%c%c%c\n", (m[1][0]), (m[1][1]), (m[1][2]), (m[1][3]));
		debug ("%c%c%c%c\n", (m[2][0]), (m[2][1]), (m[2][2]), (m[2][3]));
		debug ("%c%c%c%c\n", (m[3][0]), (m[3][1]), (m[3][2]), (m[3][3]));

		bool x = win('X');
		bool o = win('O');

		if (o && !x)
			printf("Case #%d: %s\n", i, "O won");
		else if (!o && x)
			printf("Case #%d: %s\n", i, "X won");
		else if (!o && !x && any_contains('.'))
			printf("Case #%d: %s\n", i, "Game has not completed");
		else
			printf("Case #%d: %s\n", i, "Draw");
	}
	return 0;
}
