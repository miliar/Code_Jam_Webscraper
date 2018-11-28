#include <iostream>
#include <vector>

typedef unsigned long long int64;

struct GroupInfo
{
	int numPeople;
	int64 eurosMade;
	int nextStart;
};

void printResult(int caseNum, int64 eurosMade)
{
	std::cout << "Case #" << caseNum << ": " << eurosMade << std::endl;
}

int main()
{
	int numCases;
	std::cin >> numCases;

	for (int i = 0; i < numCases; ++i) {
		int64 r;
		int k;
		int n;
		std::cin >> r >> k >> n;

		std::vector<GroupInfo> info(n);
		for (int j = 0; j < n; ++j)
			std::cin >> info[j].numPeople;	

		for (int j = 0; j < n; ++j) {
			int x = k;
			int l = j;
			int eurosMade = 0;
			while (true) {
				if (x - info[l].numPeople < 0)
					break;

				x -= info[l].numPeople;
				eurosMade += info[l].numPeople;

				l++;	
				if (l >= n)
					l = 0;
				if (l == j)
					break;
			}	

			info[j].eurosMade = eurosMade;
			info[j].nextStart = l;
		}

		// RUNS
		int start = 0;
		int64 eurosMade = 0;
		for (int64 j = 0; j < r; j++) {
			eurosMade += info[start].eurosMade;	
			start = info[start].nextStart;
		}
		printResult(i + 1, eurosMade);
	}
}

