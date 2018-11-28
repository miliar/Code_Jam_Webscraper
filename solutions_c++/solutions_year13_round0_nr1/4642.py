#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	char A[4][6];
	int Z; bool done;
	scanf("%d", &Z);
	for(int z=1; z<=Z; z++)
	{
		done = false;
		for(int i=0; i<4; i++)
			scanf("%s", A[i]);
		printf("Case #%d: ", z);
		for(int i=0; i<4; i++)
		{
			if(A[i][0] != '.' && (A[i][0] == A[i][1] && (A[i][1] == A[i][2] && (A[i][2] == A[i][3]))))
			{
				done = true;
				printf("%c won\n", A[i][0]);
				break;
			}
			if(A[i][1] != '.' && (A[i][0] == 'T' && (A[i][1] == A[i][2] && A[i][2] == A[i][3])))
			{
				done = true;
				printf("%c won\n", A[i][1]);
				break;
			}
			if(A[i][0] != '.' && (A[i][1] == 'T' && (A[i][0] == A[i][2] && A[i][2] == A[i][3])))
			{
				done = true;
				printf("%c won\n", A[i][0]);
				break;
			}
			if(A[i][0] != '.' && (A[i][2] == 'T' && (A[i][0] == A[i][1] && A[i][1] == A[i][3])))
			{
				done = true;
				printf("%c won\n", A[i][0]);
				break;
			}
			if(A[i][0] != '.' && (A[i][3] == 'T' && (A[i][0] == A[i][1] && A[i][1] == A[i][2])))
			{
				done = true;
				printf("%c won\n", A[i][0]);
				break;
			}
		}
		for(int i=0; i<4 && !done; i++)
		{
			if(A[0][i] != '.' && (A[0][i] == A[1][i] && (A[1][i] == A[2][i] && (A[2][i] == A[3][i]))))
			{
				done = true;
				printf("%c won\n", A[0][i]);
				break;
			}
			if(A[1][i] != '.' && (A[0][i] == 'T' && (A[1][i] == A[2][i] && A[2][i] == A[3][i])))
			{
				done = true;
				printf("%c won\n", A[1][i]);
				break;
			}
			if(A[0][i] != '.' && (A[1][i] == 'T' && (A[0][i] == A[2][i] && A[2][i] == A[3][i])))
			{
				done = true;
				printf("%c won\n", A[0][i]);
				break;
			}
			if(A[0][i] != '.' && (A[2][i] == 'T' && (A[0][i] == A[1][i] && A[1][i] == A[3][i])))
			{
				done = true;
				printf("%c won\n", A[0][i]);
				break;
			}
			if(A[0][i] != '.' && (A[3][i] == 'T' && (A[0][i] == A[1][i] && A[1][i] == A[2][i])))
			{
				done = true;
				printf("%c won\n", A[0][i]);
				break;
			}
		}
		if(!done && (A[0][0] != '.' && (A[0][0] == A[1][1] && (A[1][1] == A[2][2] && A[2][2] == A[3][3]))))
		{
				done = true;
				printf("%c won\n", A[0][0]);
		}
		if(!done && (A[0][0] == 'T' && (A[1][1] != '.' && (A[1][1] == A[2][2] && A[2][2] == A[3][3]))))
		{
				done = true;
				printf("%c won\n", A[1][1]);
		}
		if(!done && (A[1][1] == 'T' && (A[0][0] != '.' && (A[0][0] == A[2][2] && A[2][2] == A[3][3]))))
		{
				done = true;
				printf("%c won\n", A[0][0]);
		}
		if(!done && (A[2][2] == 'T' && (A[0][0] != '.' && (A[0][0] == A[1][1] && A[1][1] == A[3][3]))))
		{
				done = true;
				printf("%c won\n", A[1][1]);
		}
		if(!done && (A[3][3] == 'T' && (A[0][0] != '.' && (A[0][0] == A[1][1] && A[1][1] == A[2][2]))))
		{
				done = true;
				printf("%c won\n", A[1][1]);
		}
		
		if(!done && (A[0][3] != '.' && (A[0][3] == A[1][2] && (A[1][2] == A[2][1] && A[2][1] == A[3][0]))))
		{
				done = true;
				printf("%c won\n", A[0][3]);
		}
		if(!done && (A[0][3] == 'T' && (A[1][2] != '.' && (A[1][2] == A[2][1] && A[2][1] == A[3][0]))))
		{
				done = true;
				printf("%c won\n", A[1][2]);
		}
		if(!done && (A[1][2] == 'T' && (A[0][3] != '.' && (A[0][3] == A[2][1] && A[2][1] == A[3][0]))))
		{
				done = true;
				printf("%c won\n", A[2][1]);
		}
		if(!done && (A[2][1] == 'T' && (A[0][3] != '.' && (A[0][3] == A[1][2] && A[1][2] == A[3][0]))))
		{
				done = true;
				printf("%c won\n", A[1][2]);
		}
		if(!done && (A[3][0] == 'T' && (A[0][3] != '.' && (A[0][3] == A[1][2] && A[1][2] == A[2][1]))))
		{
				done = true;
				printf("%c won\n", A[1][2]);
		}
		for(int i=0; i<4 && !done; i++)
			for(int j=0; j<4 && !done; j++)
				if(A[i][j] == '.')
				{
					done = true;
					printf("Game has not completed\n");
				}
		if(!done)
			printf("Draw\n");
	}
	return 0;
}
