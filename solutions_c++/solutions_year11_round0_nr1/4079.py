#include <cstdio>
#include <algorithm>
using namespace std;

int posB, posO, lastMoveB, lastMoveO, elapsedTime;
char lastBot = 'X';

inline void nextMove(char bot, int markPos) {

	int curPos = (bot == 'B') ? posB : posO;
	// Time without marking
	int neededTime = abs(curPos-markPos);
	
	if(lastBot == 'X' || lastBot == bot)
	{
		elapsedTime += neededTime+1;
	}
	else if(lastBot != bot)
	{
		int lastMove = (bot == 'B') ? lastMoveB : lastMoveO;
		int x = neededTime-(elapsedTime-lastMove);
		// Waiting longer doesn't make it faster
		x = (x < 0) ? 0 : x;
		elapsedTime += x+1;
	}
	
	if(bot == 'B')
	{
		lastBot = 'B';
		lastMoveB = elapsedTime;
		posB = markPos;
	}
	else
	{
		lastBot = 'O';
		lastMoveO = elapsedTime;
		posO = markPos;
	}
}


int main ()
{
	int T, TC = 1;
	int C, CC;
	char bot;
	int label;
    for(scanf("%d", &T); TC <= T; TC++)
    {
		elapsedTime = 0;
		lastMoveB = 0;
		lastMoveO = 0;
		lastBot = 'X';
		posB = 1;
		posO = 1;
		CC = 1;
		for(scanf("%d", &C); CC <= C; CC++)
		{
			scanf(" %c %d", &bot, &label);
			nextMove(bot, label);
		}
		printf("Case #%d: %d\n", TC, elapsedTime);
    }

    return 0;
}
