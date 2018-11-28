#include <cstdio>
#include <algorithm>

using namespace std;

int T;
char A[5][5];

int main()
{
	scanf("%d",&T);
	for(int tt = 1 ; tt <= T ; tt++)
	{
		printf("Case #%d: ", tt);
		for(int c = 0 ; c < 4 ; c++)
			scanf(" %s",A[c]);
		int tc = -1 , td = -1;
		for(int c = 0 ; c < 4 ; c++)
			for(int d = 0 ; d < 4 ; d++)
				if(A[c][d] == 'T')
					tc = c , td = d;
		if(tc != -1 and td != -1)
			A[tc][td] = 'X';
		for(int c = 0 ; c < 4 ; c++)
		{
			bool x,y,z,w;
			x = y = z = w = true;
			for(int d = 0 ; d < 4 ; d++)
			{
				if(A[c][d] != 'X')
					x = false;
				if(A[d][c] != 'X')
					y = false;
				if(A[d][d] != 'X')
					z = false;
				if(A[d][3-d] != 'X')
					w = false;
			}
			if(x or y or z or w)
			{
				printf("X won\n");
				goto xxx;
			}
		}

		if(tc != -1 and td != -1)
			A[tc][td] = 'O';
		for(int c = 0 ; c < 4 ; c++)
		{
			bool x,y,z,w;
			x = y = z = w = true;
			for(int d = 0 ; d < 4 ; d++)
			{
				if(A[c][d] != 'O')
					x = false;
				if(A[d][c] != 'O')
					y = false;
				if(A[d][d] != 'O')
					z = false;
				if(A[d][3-d] != 'O')
					w = false;
			}
			if(x or y or z or w)
			{
				printf("O won\n");
				goto xxx;
			}
		}

		for(int c = 0 ; c < 4 ; c++)
			for(int d = 0 ; d < 4 ; d++)
				if(A[c][d] == '.')
				{
					printf("Game has not completed\n");
					goto xxx;
				}
		printf("Draw\n");
		xxx:;
	}
}