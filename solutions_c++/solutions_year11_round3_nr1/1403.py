#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <memory.h>
#include <string.h>

#define BLUE	'#'
#define WHITE	'.'
#define MAXR	50
#define MAXC	50

void main2()
{
	int row, col;
	int i, j;
	int cnt;
	char pic[MAXC][MAXR+1];

	scanf("%d %d", &row, &col);
	for(i = 0; i < row; i++)
	{
		scanf("%s", pic + i);
	}

	for(i = 0; i < row; i++) {
		cnt = 0;
		for(j = 0; j < col; j++) {
			if(pic[i][j] == BLUE) cnt++;
		}
		if(cnt % 2 == 1) break;
	}
	if(i < row) {
		printf("Impossible\n");
		return;
	}

	for(i = 0; i < col; i++) {
		cnt = 0;
		for(j = 0; j < row; j++) {
			if(pic[j][i] == BLUE) cnt++;
		}
		if(cnt % 2 == 1) break;
	}
	if(i < col) {
		printf("Impossible\n");
		return;
	}

	for(i = 0; i < row; i++)
	{
		for(j = 0; j < col; j++)
		{
			if(pic[i][j] == BLUE) {
				pic[i][j]   = '/';	pic[i][j+1]   = '\\';
				pic[i+1][j] = '\\';	pic[i+1][j+1] = '/';
			}
		}
	}

	for(i = 0; i < row; i++)
	{
		printf("%s\n", pic[i]);
	}

}

//======================================================
int main()
{
	int t, T;

	//freopen("A.txt", "r", stdin);

	//freopen("A-small.in", "r", stdin);
	//freopen("A-small.out.txt", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out.txt", "w", stdout);

	scanf("%d", &T);
	for(t = 0; t < T; t++)
	{
		printf("Case #%d:\n", t+1);
		main2();
	}
	return 0;
}