#include <iostream>
#include <map>
#include <set>
#include <vector>

void processLine(int lineNum)
{
	typedef std::pair<std::string, char> combinePair;
	typedef std::map<std::string, char> combineT;
	typedef combineT::iterator combineIt;
	combineT combine;

	typedef std::set<std::string> opposeT;
	typedef opposeT::iterator opposeIt;
	opposeT oppose;

	int numCombine = 0;
	std::cin >> numCombine;
	for(int i = 0; i < numCombine; ++i) {
		std::string combineEntry;
		std::cin >> combineEntry;
		//std::cerr << "Got ce " << combineEntry << std::endl;

		std::string entryA;
		entryA.push_back(combineEntry[0]);
		entryA.push_back(combineEntry[1]);

		std::string entryB;
		entryB.push_back(combineEntry[1]);
		entryB.push_back(combineEntry[0]);

		//std::cerr << "Adding ces " << entryA << ',' << entryB << std::endl;

		combine.insert(combinePair(entryA, combineEntry[2]));
		combine.insert(combinePair(entryB, combineEntry[2]));
	}

	int numOppose = 0;
	std::cin >> numOppose;
	for(int i = 0; i < numOppose; ++i) {
		std::string opposeEntry;
		std::cin >> opposeEntry;
		//std::cerr << "Got oe " << opposeEntry << std::endl;

		std::string entryA;
		entryA.push_back(opposeEntry[0]);
		entryA.push_back(opposeEntry[1]);

		std::string entryB;
		entryB.push_back(opposeEntry[1]);
		entryB.push_back(opposeEntry[0]);

		//std::cerr << "Adding oes " << entryA << ',' << entryB << std::endl;

		oppose.insert(entryA);
		oppose.insert(entryB);
	}

	int sequenceLen;
	std::cin >> sequenceLen;	

	std::string sequence;
	std::cin >> sequence;

	std::vector<char> result;

	for(int i = 0; i < sequenceLen; ++i) {
			int len = result.size();	

			if (len > 0) {
				std::string pairToTest;
				pairToTest.push_back(result[len-1]);
				pairToTest.push_back(sequence[i]);
				//std::cerr << "Testing " << pairToTest << std::endl;

				// Check if this would combine
				combineIt cit = combine.find(pairToTest);
				if(combine.end() != cit) {
					//std::cerr << pairToTest << " combines to: " << cit->second << std::endl;
					result[len-1] = cit->second;
					continue;
				}
	
				// Insert
				result.push_back(sequence[i]);	
			}
			else {
				// First entry
				result.push_back(sequence[i]);
			}

			for(int j = 0; j < result.size()-1; ++j) {
				std::string pairToTest;
				pairToTest.push_back(result[j]);
				pairToTest.push_back(sequence[i]);

				// Check if this new item opposes anything in the list
				opposeIt oit = oppose.find(pairToTest);
				if (oppose.end() != oit) {
					//std::cerr << pairToTest << " clears" << std::endl;
					result.clear();
					break;
				}
			}
	}

	// Output results
	std::cout << "Case #" << lineNum+1 << ": [";
	for(int i = 0; i < result.size(); ++i) {
		std::cout << result[i];
		
		if (i < result.size()-1) {
			std::cout << ", ";
		}
	}
	std::cout << ']' << std::endl;
	
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
