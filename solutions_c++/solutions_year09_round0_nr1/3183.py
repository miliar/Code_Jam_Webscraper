//////////////////////////////////////////////////////////
// File:   probA.cpp
// Author: Stephen Pfetsch			spfetsch@gmail.com
// Date:   September 3, 2009
//////////////////////////////////////////////////////////

#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
	int L, D, N, count, n, d, icases, idict, matches;
	bool matchFlag;
	string *dict, *cases;

	ifstream fin(argv[1]);
	fin >> L >> D >> N;
	dict = new string[D];
	cases = new string[N];
	for (count = 0; count < D; count++)
		fin >> dict[count];
	for (count = 0; count < N; count++)
		fin >> cases[count];
	fin.close();
	
	/*for (count = 0; count < D; count++)
		cout << dict[count] << endl;
	for (count = 0; count < N; count++)
		cout << cases[count] << endl;*/
	
	for (n = 0; n < N; n++) // inspect each case
	{
		matches = 0;
		
		for (d = 0; d < D; d++) // compare each dictionary word to the regex
		{
			for (icases = 0, idict = 0; idict < L; icases++) // compare letter-by-letter
			{
				if (cases[n][icases] == '(')
				{
					icases++; // move past the '('
					matchFlag = false;
					while (cases[n][icases] != ')' && !matchFlag)
					{
						if (dict[d][idict] == cases[n][icases])
							matchFlag = true;
						icases++;
					}
					while (cases[n][icases] != ')')
						icases++;	// In case we break early, move the index to the closing paren
					if (!matchFlag)
						break;	// None of the letters matched, so move to the next word
				}
				else
				{
					if (dict[d][idict] != cases[n][icases])
						break;	// Mismatched letter, so move to the next word
				}
				
				idict++;
				if (idict == L)	 // If this word fits the regex,
					matches++;	 // ... we have a match.
			}
		}
		
		cout << "Case #" << n+1 << ": " << matches << endl;
	}
	
	delete[] dict;
	delete[] cases;
	
	return 0;
}
