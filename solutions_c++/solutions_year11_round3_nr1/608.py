// Google Codejam
// May 22, 2011
// Author	::	MIB
// Problem	::	A


#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>


using namespace std;

const int MAX = 55;

char board[MAX][MAX];

int main(void)
{
	freopen ("C:\\Documents and Settings\\Mainul\\My Documents\\Downloads\\Codejam\\input\\A-large.in", "rt", stdin);
	freopen ("C:\\Documents and Settings\\Mainul\\My Documents\\Downloads\\Codejam\\output\\A-large.out", "wt", stdout);

	int t, T;
	int R, C;
	int i, j;
	int bc;
	bool possible;

	scanf(" %d",&T);
	
	for(t=1; t<=T; t++)
	{
		scanf(" %d %d ", &R, &C);

		bc = 0;

		for(i=0; i<R; i++)
		{
			gets(board[i]);

			for(j=0; j<C; j++)
			{
				if(board[i][j] == '#')
					bc++;
			}
		}

		printf( "Case #%d:\n", t);

		if(bc % 4 != 0)
		{
			printf( "Impossible\n", t);
			continue;
		}


		possible = true;

		for(i=0; i<R; i++)
		{
			for(j=0; j<C; j++) {
				
				if(board[i][j] == '#') {
					
					if(i+1 < R && j+1 < C) {
						
						if(	board[i][j+1] == '#' && 
							board[i+1][j] == '#' && 
							board[i+1][j+1] == '#') {
								board[i][j] = '/'; 
								board[i][j+1] = '\\'; 
								board[i+1][j] = '\\'; 
								board[i+1][j+1] = '/';
						}

						else {
							possible = false;
							break;
						}
					}

					else {
						possible = false;
						break;
					}
				}
			}

			if(!possible)
				break;
		}

		if(!possible)
			printf( "Impossible\n", t);
		else {
			for(i=0; i<R; i++) {
				for(j=0; j<C; j++)
					printf("%c",board[i][j]);
				printf("\n");
			}
		}
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
