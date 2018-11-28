#include <stdio.h>
#include <string.h>

char* count(const char t4[4][8], int i, int j, int di, int dj, int& ec)
{
	int oc = 0, xc = 0;

	ec = 0;
	for (int k = 0; k < 4; ++k, i += di, j += dj)
		{
		if (t4[i][j] == 'O')
			{
			++oc;
			}
		else if (t4[i][j] == 'X')
			{
			++xc;
			}
		else if (t4[i][j] == 'T')
			{
			++oc;
			++xc;
			}
		else{
			++ec;
			}//end if
		}//end for

	if (oc == 4)
		{
		return "O won";
		}
	else if (xc == 4)
		{
		return "X won";
		}//end if
	return NULL;
}//end count

char* judge(const char t4[4][8])
{
	int sec, ec;
	char *res;
	int i;

	sec = 0;

	for (i = 0; i < 4; ++i)
		{
		if ((res = count(t4, i, 0, 0, 1, ec)) != NULL)
			{
			return res;
			}//end if
		sec += ec;
		}//end for

	for (i = 0; i < 4; ++i)
		{
		if ((res = count(t4, 0, i, 1, 0, ec)) != NULL)
			{
			return res;
			}//end if
		sec += ec;
		}//end for
	
	if ((res = count(t4, 0, 0, 1, 1, ec)) != NULL)
		{
		return res;
		}//end if
	sec += ec;

	if ((res = count(t4, 0, 3, 1, -1, ec)) != NULL)
		{
		return res;
		}//end if
	sec += ec;

	return (sec > 0) ? "Game has not completed" : "Draw";
}//end judge

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	char t4[4][8];
	int t;
	int c, i;

	scanf("%d", &t);
	for (c = 1; c <= t; ++c)
		{
		for (i = 0; i < 4; ++i)
			{
			scanf("%s", t4[i]);
			}//end for
		printf("Case #%d: %s\n", c, judge(t4));
		}//end for
	
	return 0;
}//end main
