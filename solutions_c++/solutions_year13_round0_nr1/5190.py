#include <stdio.h>

//using namespace std;

#define N 4
char A[10][90];

bool noDot()
{
	for(int i=0;i<N;++i)
	{
		if (A[i][0] =='.' || A[i][1] =='.' || A[i][2] =='.' ||  A[i][3] =='.') return false;
	}
	return true;
}

bool match(char c, char d)
{
	return (d == c || d == 'T');
}

bool check(char c)
{
//check diagonals
	if(match(c, A[0][0]) && match(c, A[1][1]) && match(c, A[2][2]) && match(c, A[3][3])) return true;
	if(match(c, A[0][3]) && match(c, A[1][2]) && match(c, A[2][1]) && match(c, A[3][0])) return true;
	if(match(c, A[0][0]) && match(c, A[0][1]) && match(c, A[0][2]) && match(c, A[0][3])) return true;
	if(match(c, A[1][0]) && match(c, A[1][1]) && match(c, A[1][2]) && match(c, A[1][3])) return true;
	if(match(c, A[2][0]) && match(c, A[2][1]) && match(c, A[2][2]) && match(c, A[2][3])) return true;
	if(match(c, A[3][0]) && match(c, A[3][1]) && match(c, A[3][2]) && match(c, A[3][3])) return true;
	for(int i=0;i<N;++i)
	{
		if(match(c, A[0][i]) && match(c, A[1][i]) && match(c, A[2][i]) && match(c, A[3][i])) return true;
	}
	return false;
}


int main()
{
	int t;
	scanf("%d", &t);
	int Case = 0;
	for(int T =1; T<=t; ++T)
	{
		for(int i=0;i<N;++i)
		{
			scanf("%s", A[i]);
		 //	printf("%s\n", A[i]);
		}
		if(check('X'))
		{
			printf("Case #%d: X won\n", T);
			continue;
		}
		if(check('O'))
		{
			printf("Case #%d: O won\n", T);
			continue;
		}
		if(noDot())
		{
			printf("Case #%d: Draw\n", T);
			continue;
		}
		printf("Case #%d: Game has not completed\n", T);
	}
	return 0;
	
}
