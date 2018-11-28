#include <iostream>
#include <cassert>

struct Snapper
{
	enum State { On, Off };
	State state;
};

void printCase(int caseNum, Snapper::State state)
{
	std::cout << "Case #" << caseNum << ": ";
	if (state == Snapper::On)
		std::cout << "ON";
	else if (state == Snapper::Off)
		std::cout << "OFF";
	std::cout << std::endl;
}

Snapper::State runCase(int n, int k)
{
	// Index of last powered snapper in chain
	int lastPowered = 0;

	Snapper* snappers = new Snapper[n];
	for (int i = 0; i < n; ++i) {
		snappers[i].state = Snapper::Off;	
	}

	// SNAP
	for (int j = 0; j < k; ++j) {
		// All powered snappers switch state
		// NOTE: lastPowered is an index, so use <=
		for (int i = 0; i <= lastPowered; ++i) {
			if (snappers[i].state == Snapper::On)
				snappers[i].state = Snapper::Off;
			else
				snappers[i].state = Snapper::On;
		}

		// New powered index
		for (int r = 0; r < n; ++r) {
			lastPowered = r;
			if (snappers[r].state == Snapper::Off)
				break;
		}
	}

	Snapper::State res = lastPowered == n - 1 && snappers[lastPowered].state == Snapper::On ? 
		Snapper::On : Snapper::Off;
	delete[] snappers;
	return res;
}

int main()
{
	int numCases = 0;
	std::cin >> numCases;

	for (int i = 0; i < numCases; ++i) {
		int n = 0;
		int k = 0;
		std::cin >> n >> k;

		Snapper::State light = runCase(n, k);
		printCase(i + 1, light);
	}	

	return 0;
}

