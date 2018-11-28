#include <iostream>

void processLine(int lineNum)
{
	int maxPlayedToday;
	std::cin >> maxPlayedToday;

	int pWonToday;
	std::cin >> pWonToday;

	int pWonGlobal;
	std::cin >> pWonGlobal;

	bool isValid = false;

	if (pWonToday == 0
			|| pWonToday == 100) {
		isValid = true;
	}
	else {
		for (uint64_t i = 1; i <= maxPlayedToday; ++i) {
			double numWon = (double)i * (double)pWonToday / 100.0;

			uint64_t numWonInt = numWon;
			double numWonIntDouble = numWonInt;

			if (numWon == numWonIntDouble) {
				isValid = true;
			}
		}
	}

	if (isValid) {
		// Check Global

		if (pWonGlobal == 100
				&& pWonToday != 100) {
			isValid = false;
		}
		else if (pWonGlobal == 0
						&& pWonToday != 0) {
			isValid = false;
		}
	}

	// Output results
	std::string result = isValid ? "Possible" : "Broken";
	std::cout << "Case #" << lineNum+1 << ": " 
		<< result << std::endl;
	
}

int main()
{
	int numLines = 0;
	std::cin >> numLines;

	for(int i = 0; i < numLines; ++i) {
		processLine(i);		
	}

	return 0;
}
