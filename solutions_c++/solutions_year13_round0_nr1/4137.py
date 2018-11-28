using namespace std;
#include<cstdio>
#include<cstring>
char A[5][5];
int main()
{
	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);
	int TT, i, j, X, O, T;
	scanf("%d\n", &TT);
	int test = 1;
	while(TT--)
	{
		int dots = 0;
		bool OK = false;
		memset(A, 0, sizeof(A));
		for(i = 1; i <= 4; ++i)
			scanf("%s\n", A[i] + 1);
		for(i = 1; i <= 4;++i)
			for(j = 1; j <= 4;++j)
				dots += (A[i][j] == '.');
		for(i = 1; i <= 4; ++i)
		{
			X = 0, O = 0, T = 0;
			for(j = 1; j <= 4; ++j)
			{
				X += (A[i][j] == 'X');
				O += (A[i][j] == 'O');
				T += (A[i][j] == 'T');
			}
			if ( X == 4 || (X == 3 && T == 1))
			{
				printf("Case #%d: X won\n", test);
				OK = true;
			}
			else if ( O == 4 || (O == 3 && T == 1))
			{
				OK = true;
				printf("Case #%d: O won\n", test);
			}
		}
		for(i = 1; i <= 4 && OK == false; ++i)
		{
			X = 0, O = 0, T = 0;
			for(j = 1; j <= 4; ++j)
			{
				X += (A[j][i] == 'X');
				O += (A[j][i] == 'O');
				T += (A[j][i] == 'T');
			}
			if ( X == 4 || (X == 3 && T == 1))
			{
				printf("Case #%d: X won\n", test);
				OK = true;
			}
			else if ( O == 4 || (O == 3 && T == 1))
			{
				OK = true;
				printf("Case #%d: O won\n", test);
			}
		}
		X = 0; O = 0; T = 0;
		for(i = 1; i <= 4 && OK == false; ++i)
		{
			X += (A[i][i] == 'X');
			O += (A[i][i] == 'O');
			T += (A[i][i] == 'T');
		}
		
		if ( X == 4 || (X == 3 && T == 1))
		{
			printf("Case #%d: X won\n", test);
			OK = true;
		}
		else if ( O == 4 || (O == 3 && T == 1))
		{
			OK = true;
			printf("Case #%d: O won\n", test);
		}

		X = 0; O = 0; T = 0;
		for(i = 1; i <= 4 && OK == false; ++i)
		{
			X += (A[i][4-i + 1] == 'X');
			O += (A[i][4-i + 1] == 'O');
			T += (A[i][4-i + 1] == 'T');
		}
		
		if ( X == 4 || (X == 3 && T == 1))
		{
			printf("Case #%d: X won\n", test);
			OK = true;
		}
		else if ( O == 4 || (O == 3 && T == 1))
		{
			OK = true;
			printf("Case #%d: O won\n", test);
		}
		if(OK == false)
		{
			if(dots == 0)
			{
				printf("Case #%d: Draw\n", test);
			}
			else
			{
				printf("Case #%d: Game has not completed\n", test);
			}
		}
		
		++test;
	}
	return 0;
}