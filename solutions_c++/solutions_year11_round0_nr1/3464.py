#include <iostream>
#define N_MAX 101

using namespace std;

int T, N;
int buttons[N_MAX] = {0};
char robots[N_MAX];
int currentTC = 1;

int main()
{
	freopen("bottrust.in", "r", stdin);
	freopen("bottrust.out", "w", stdout);
	
	scanf("%d", &T);
	for(int i = 0; i < T; ++i)
	{	
		scanf("%d", &N);
		for(int j = 0; j < N; ++j)
		{
			scanf(" %c", &robots[j]);
			scanf("%d", &buttons[j]);
		}
		
		int totalMoves = 0;
		int freeMoves[2] = {0, 0};
		int currentPos[2] = {1, 1};
		int robot = 0; // 1: Orange, 2: Blue
		int moves = 0;
		for(int j = 0; j < N; ++j)
		{
			robot = 0;
			if (robots[j] != 'O') robot = 1;
			
			moves = buttons[j] - currentPos[robot];
			if (moves < 0) moves *= -1;
			moves -= freeMoves[robot];
			if (moves < 0) moves = 0;
			totalMoves += ++moves;
			
			if (robot == 0)
			{
				freeMoves[0] = 0;
				freeMoves[1] += moves;
				currentPos[0] = buttons[j];
			}
			else
			{
				freeMoves[1] = 0;
				freeMoves[0] += moves;
				currentPos[1] = buttons[j];
			}
		}
		
		printf("Case #%d: %d\n", currentTC++, totalMoves);
	}
}