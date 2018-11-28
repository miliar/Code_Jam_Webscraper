#include <cstdio>
#include <cstring>

int no;

bool check(char m[4][4], char X)
{
	bool winX, winY, winL, winR;
	winL = winR = true;
	for(int i = 0; i < 4; i++)
	{
		winX = winY = true;
		for(int n = 0; n < 4; n++)
		{
			if(m[i][n] != 'T' && m[i][n] != X)
				winX = false;
		
			if(m[n][i] != 'T' && m[n][i] != X)
				winY = false;
		}
		if(winX || winY)
			return true;

		if(m[i][i] != 'T' && m[i][i] != X)
			winR = false;
		bool t = (m[3 - i][i] != 'T' && m[3 - i][i] != X);
		if(t) {
			winL = false;
		}
	}
	return (winR || winL);	
}


int main()
{
	int N; scanf("%d[^\n]", &N);
	getchar();	
	for(no = 0; no < N; no++)
	{
		char m[4][4];
		char cr;
		for(int y = 0; y < 4; y++)
			scanf("\n%c%c%c%c", &m[y][0], &m[y][1], &m[y][2], &m[y][3]);

		bool complete = true;
		for(int y = 0; y < 4; y++)
		{
			for(int x = 0; x < 4; x++)
			{
				// printf("%d", m[y][x]);
				if(m[y][x] == '.')
				{
					complete = false;
					break;
				}
			}
			if(!complete) break;
			// printf("\n");
		}

		printf("Case #%d: ", no + 1);

		if(check(m, 'X')) {
			printf("X won\n");
			continue;
		}
        if(check(m, 'O')) {
            printf("O won\n");
    		continue;
		}
	    if(complete)
            printf("Draw\n");
		else
			printf("Game has not completed\n");
	}

	return 0;	
}
