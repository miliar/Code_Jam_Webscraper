#include <cstdio>
#include <algorithm>

using namespace std;

char B[5][5];
int R[1000][5];
int C[1000][5];
int D[1000][5];
char S[4] = {'O', 'X', 'T', '.' };

void read()
{
	for(int i = 0;i<4;i++)
		scanf("%s", B[i]);
	for(int i = 0;i<4;i++)
		for(int j = 0;j<4;j++)
			C[S[i]][j] = R[S[i]][j] = D[S[i]][j] = 0;
	for(int i = 0;i<4;i++)
		for(int j = 0;j<4;j++)
		{
			R[B[i][j]][i]++;
			C[B[i][j]][j]++;
		}
	for(int i = 0;i<4;i++)
	{
		D[B[i][i]][0]++;
		D[B[i][3-i]][1]++;
	}
}
bool check(char t)
{
	for(int i = 0;i<4;i++)
		if(R[t][i] + R['T'][i] == 4 || C[t][i] + C['T'][i] == 4)
			return true;
	if(D[t][0] + D['T'][0] == 4 || D[t][1] + D['T'][1] == 4)
		return true;
	return false;
}
bool finished()
{
	for(int i = 0;i<4;i++)
		if(R['.'][i])
			return false;
	return true;
}
void solve(int tc)
{
	if(check('O'))
	{
		printf("Case #%d: O won\n", tc);
		return;
	}
	if(check('X'))
	{
		printf("Case #%d: X won\n", tc);
		return;
	}
	if(finished())
		printf("Case #%d: Draw\n", tc);
	else
		printf("Case #%d: Game has not completed\n", tc);
}
int main()
{
	int Z;
	scanf("%d", &Z);
	for(int i = 1;i<=Z;i++)
	{
		read();
		solve(i);
	}
	return 0;
}
