#include  <cstdio> 
#include  <cstdlib> 
#include  <cstring> 
#include  <string> 
#include  <vector> 
#include  <cmath> 
#include  <algorithm> 
#include  <cassert> 
#include  <set> 
#include  <map> 
#include  <queue> 
#include  <iostream> 
#include <fstream> 
using namespace std; 
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )  

typedef long long LL; 
typedef pair<int,int> piii; 

int dir[4][2] = {-1, 0, 0, -1, 0, 1, 1, 0};
int M[100][100];
int D[100][100];
char R[100][100];
int H, W;

inline int valid(int x, int y)
{
	return x>=0 && y>=0 && x<H && y<W;
}

int getD(int x, int y)
{
	int B = M[x][y];
	int D = -1;
	REP(i, 4)
	{
		int NX = x + dir[i][0];
		int NY = y + dir[i][1];
		if (valid(NX, NY))
		{
			if (B > M[NX][NY])
			{
				B = M[NX][NY];
				D = i;
			}
		}
	}
	return D;
}

void DFS(int X, int Y, char C)
{
	if (R[X][Y])
		return ;
	R[X][Y] = C;
	if (D[X][Y] != -1)
		DFS(X  + dir[D[X][Y]][0], Y  + dir[D[X][Y]][1], C);
	REP(i, 4)
	{
		int NX = X + dir[i][0];
		int NY = Y + dir[i][1];
		if (valid(NX, NY) && (D[NX][NY] + i) == 3)
		{
			DFS(NX, NY, C);
		}
	}
}

int main()
{
	int cases;
	scanf("%d", &cases);
	REP(caseIndex, cases)
	{
		scanf("%d%d", &H, &W);
		REP(i, H)
			REP(j, W)
				scanf("%d", &M[i][j]);
		REP(i, H)
			REP(j, W)
				D[i][j] = getD(i, j);
		memset(R, 0, sizeof R);
		char index = 'a';
		REP(i, H)
			REP(j, W)
			{
				if (!R[i][j])
				{
					DFS(i, j, index++);
				}
			}
		printf("Case #%d:\n", caseIndex+1);
		REP(i, H)
		{
			REP(j, W)
			{
				if (j)
					printf(" %c", R[i][j]);
				else
					printf("%c", R[i][j]);
			}
			puts("");
		}
	}
	return 0;
}
