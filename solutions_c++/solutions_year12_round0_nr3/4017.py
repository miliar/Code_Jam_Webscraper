#include <iostream>
#include <list>
#include <set>

int getValue(std::list<int> &numAsList)
{
	int ret = 0;

	std::list<int>::iterator it;
	for(it = numAsList.begin(); it != numAsList.end(); ++it) {
		ret = ret*10 + *it;
	}

	return ret;
}

void rotate(std::list<int> &numAsList)
{
	// Debugging
	//std::cout << "Rotated " << getValue(numAsList);
	
	numAsList.push_front(numAsList.back());
	numAsList.pop_back();

	// Debugging
	//std::cout << " to " << getValue(numAsList) << std::endl;
}

void processLine(int lineNum)
{
	std::string AStr, BStr;
	std::cin >> AStr;
	std::cin >> BStr;

	int A,B;
	A = atoi(AStr.c_str());
	B = atoi(BStr.c_str());

	int numDigits = AStr.length();

	// Use a set so we only get unique pairs
	std::set< std::pair<int,int> > pairs;

	for(int i = A; i <= B; ++i) {
		// Decompose digits into list
		int numberToDecompose = i;
		std::list<int> testCase;

		for(int j = 0; j < numDigits; ++j) {
			testCase.push_front(numberToDecompose % 10);
			numberToDecompose = numberToDecompose / 10;
		}

		// For each rotation combo
		for(int j = 0; j < numDigits-1; ++j) {
			rotate(testCase);
			
			int rotatedValue = getValue(testCase);

			if (A <= rotatedValue
					&& i < rotatedValue
					&& rotatedValue <= B) 
			{
				pairs.insert(std::pair<int,int>(i,rotatedValue));
			}
		}

	}

	std::cout << "Case #" << lineNum+1 << ": " 
		<< pairs.size() << std::endl;
	
}

int main()
{
	int numLines = 0;
	std::cin >> numLines;

/*
	std::pair<int,int> p1(10,11);
	std::pair<int,int> p2(10,12);
	std::pair<int,int> pDupe(10,11);

	if(p1 == p2)
		std::cout << "wtf?" << std::endl;

	if (p1 == pDupe)
		std::cout << "Detected pair match" << std::endl;
*/

	for(int i = 0; i < numLines; ++i) {
		processLine(i);		
	}

	return 0;
}
