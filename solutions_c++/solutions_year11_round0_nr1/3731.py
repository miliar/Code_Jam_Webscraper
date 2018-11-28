#include <iostream>
#include <map>
#include <set>
#include <vector>

void processLine(int lineNum)
{
	std::vector<int> gPress;
	std::vector<int> oPress;
	std::vector<int> bPress;

	int numPresses;
	std::cin >> numPresses;

	// Read in presses
	for(int i = 0; i < numPresses; ++i) {
		std::string color;
		std::cin >> color;

		int point;
		std::cin >> point;

		if ('O' == color[0]) {
			oPress.push_back(point);

			gPress.push_back(-point);	// Use negative for orange in global
		}
		else {
			bPress.push_back(point);

			gPress.push_back(point);
		}
	}

	// Play the game
	int timeSpent = 0;
	int oPos = 1;
	int bPos = 1;
	int gPressPos = 0;
	int oPressPos = 0;
	int bPressPos = 0;
	bool incGPressPos = false;

	while(gPressPos < gPress.size()) {
		// Orange's actions
		if (oPressPos == oPress.size()) {
			// Done
		}
		else if (oPos == oPress[oPressPos]
				&& -oPos == gPress[gPressPos]) {
			// At next press point and it's global press point - press it
			incGPressPos = true;
			++oPressPos;
		}
		else if (oPos == oPress[oPressPos]) {
			// At next press point but not global, wait
		}
		else {
			// Move 1 unit towards next press point
			oPos += (oPos < oPress[oPressPos]) ? 1 : -1;
		}

		// Blue's actions
		if (bPressPos == bPress.size()) {
			// Done
		}
		else if (bPos == bPress[bPressPos]
				&& bPos == gPress[gPressPos]) {
			// At next press point and it's global press point - press it
			incGPressPos = true;
			++bPressPos;
		}
		else if (bPos == bPress[bPressPos]) {
			// At next press point but not global, wait
		}
		else {
			// Move 1 unit towards next press point
			bPos += (bPos < bPress[bPressPos]) ? 1 : -1;
		}

		// Increment global if it was pressed
		if (incGPressPos) {
			++gPressPos;
			incGPressPos = false;
		}

		++timeSpent;
		
		/*std::cout 
			<< timeSpent << '\t'
			<< oPos << '\t'
			<< bPos << '\t'
			<< gPressPos << '\t'
			<< oPressPos << '\t'
			<< bPressPos << '\t'
			<< std::endl;
		*/
	}

	// Output results
	std::cout << "Case #" << lineNum+1 << ": " 
		<< timeSpent << std::endl;
	
}

int main()
{
	int numLines = 0;
	std::cin >> numLines;

	for(int i = 0; i < numLines; ++i) {
		processLine(i);		
	}

	return 0;

/*
	std::cout << numLines << std::endl;

	std::cin >> numLines;
	std::cout << numLines << std::endl;
*/
}
