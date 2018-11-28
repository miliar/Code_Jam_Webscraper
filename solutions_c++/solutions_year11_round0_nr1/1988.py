#include "stdafx.h"
#include <iostream>
#include <cstdlib>
using namespace std;

// Usage: BotTrust < input.in
int main(int argc, char* argv[])
{
	int T; // Number of test cases
	cin >> T;
	
	// For each test case / line in file
	for(int t=0; t<T; t++)
	{
		int moves = 0;           // Current number of moves
		int pos[2] = {1,1};      // Current position of robots
		int lastMove[2] = {0,0}; // last time of robots moves

		int N; // Number of buttons to be pressed
		cin >> N;
		for(int i=0; i<N; i++)
		{
			char Ri; // Robot: 'O' or 'B'
			int Pi;  // Button position
			cin >> Ri;
			cin >> Pi;

			int R = Ri=='O' ? 0 : 1; // Should add validity check...

			// Robot R needs to move to button Pi
			int distance = abs(Pi - pos[R]);
			distance -= moves - lastMove[R]; // Move done while other robot was moving
			distance = max(0, distance);
			moves += distance + 1;
			pos[R] = Pi;
			lastMove[R] = moves;
		}

		cout << "Case #" << t+1 << ": " << moves << endl;
	}

	return 0;
}

