// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int testNumber = 1;

	//Eat line specifying total number of testcases
	string input;
	getline(cin, input);
	
	while (cin.good()) {
		string input;
		getline(cin, input);
		//Ignore blank line (at end of file)
		if (input.length() == 0) continue;

		istringstream instream(input);
		
		int googlers;
		int surprising;
		int p;

		instream >> googlers >> surprising >> p;
		
		int output = 0;

		while(instream.good()) {
			int score;
			instream >> score;			

			int best = score/3;
			if (score%3 > 0) best++;
			if (best == p-1 && surprising > 0 && score > 1 && score%3 != 1) {
				best++;
				surprising--;
			}

			if (best >= p) output++;
		}

		cout << "Case #" << testNumber << ": " << output << endl;
		testNumber++;
	}
	
	return 0;
}

