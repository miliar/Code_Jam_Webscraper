// BotTrust.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <math.h>
#include <algorithm>
#include <stdlib.h>

//Microsot Visual Studio Express 2010 
// Przeciez i tak tego nikt nie czyta, prawda?
//Lubudubu, lubudubu, niechzyjenam, prezes naszego klubu,
//niech zyyyyje nam!

using namespace std;

enum BotType {
	OH = 0,
	BE =1
};

int getComplementBot(int source)
{
	if (source == OH)
		return BE;
	else
		return OH;
}

class State {
	public:
		long currTime[2];
		long freeTime[2];
		
		long currButton[2];
		int whoLast;

		void clear() 
		{
			whoLast = 0;
			for (int i=0; i<=1;++i)
			{
				currTime[i]=0;
				freeTime[i]=0;
				currButton[i]=1;
			};
		}
};

void makeMove(State& state, int curr, long newButton)
{
	int comp = getComplementBot(curr);
	
	if (curr != state.whoLast)
	{
		long actionTime = max( abs((long) (state.currButton[curr] - newButton)), state.freeTime[comp])+1;
		state.currTime[curr] += actionTime;
		state.freeTime[curr]  = max( (long) 0, actionTime - state.freeTime[comp]);
		state.freeTime[comp] = 0;
	} else {
		long actionTime = abs(state.currButton[curr] - newButton)+1;
		state.currTime[curr]  += actionTime;
		state.freeTime[curr] += actionTime;
	}

	state.currButton[curr] = newButton;
	state.whoLast = curr;
}

int main(int argc, char* argv[])
{
	int T, N;
	State state;
	char currBot;
	int button;
	char temp[10];

	freopen ("c://temp//BotTrust.in","r",stdin);
	 freopen ("c://temp//BotTrust.out","w",stdout);

	scanf("%i", &T);
	
	for (int i=1; i<=T; ++i)
	{
		state.clear();
		scanf("%[ \n]", temp);
		scanf("%i", &N);
		for (int j=1; j<= N; ++j)
		{
			scanf("%[ \n]", temp);
			scanf("%c", &currBot);
			if (currBot == 'O')
				currBot = OH;
			else
				currBot = BE;

			scanf("%i", &button);

			if (j==1)
				state.whoLast = currBot;

			makeMove(state, currBot, button);
		}

		printf("Case #%i: %li\n", i, max(state.currTime[0],state.currTime[1]));
	};

	return 0;
}

