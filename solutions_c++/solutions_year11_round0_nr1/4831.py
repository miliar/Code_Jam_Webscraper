/*
 *  gcjB.cpp
 *  TopCoder
 *
 *  Created by Michelangelo Partipilo on 5/7/11.
 *  Copyright 2011. All rights reserved.
 *
 */

#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

typedef vector<char> robotsCollection;
typedef vector<int> buttonsCollection;

class gcjB
{
public:
	map<char, int> botLocation;
	map<char, int> botNextLocation;
	
	int findNextLocation(char bot, unsigned int start, robotsCollection R, buttonsCollection B)
	{
		for (unsigned int P=start; P<R.size(); ++P)
		{
			if (R[P] != bot) continue;
			if (R[P] == bot) return B[P];
		}
		return 0;
	}
	
	void moveBot(char bot)
	{
		if (botLocation[bot] == botNextLocation[bot])
		{
			// bot is waiting for the other robot to push button, or robot has to push button
			return;
		}
		
		if (botLocation[bot] < botNextLocation[bot])
		{
			// bot has to move ahead
			botLocation[bot] = botLocation[bot] + 1;
		}
		else {
			botLocation[bot] = botLocation[bot] - 1;
		}

	}
	
	unsigned int getSolution(int N, robotsCollection R, buttonsCollection B)
	{
		unsigned int result = 0;

		botLocation['B'] = 1;
		botLocation['O'] = 1;

		unsigned int nextButton = 0;

		botNextLocation['B'] = findNextLocation('B', nextButton, R, B);
		botNextLocation['O'] = findNextLocation('O', nextButton, R, B);

		for (result=0; nextButton<N; ++result) 
		{
			// Bot Next Button
			char bnb = R[nextButton];
			
			if (botLocation[bnb] == botNextLocation[bnb])
			{
				botNextLocation[bnb] = findNextLocation(bnb, nextButton+1, R, B);
				++nextButton;
				if (bnb == 'B')
				{
					moveBot('O');
				}
				else {
					moveBot('B');
				}

				continue;
			}
			
			moveBot('B');
			moveBot('O');
		}
				
		return result;
	}
};

int main (int argc, char * const argv[]) 
{
	gcjB program;

	int N = 0;
	
	cin >> N;

	for (int C=1; C<=N; ++C)
	{
		robotsCollection R;
		buttonsCollection B;
		
		int T = 0;
		
		cin >> T;
		
		for (int i=0; i<T; ++i) {
			char bot;
			int button;
			cin >> bot;
			cin >> button;
			R.push_back(bot);
			B.push_back(button);
		}

		cout << "Case #" << C << ": " << program.getSolution(R.size(), R, B) << endl;
	}
	
    return 0;
}
