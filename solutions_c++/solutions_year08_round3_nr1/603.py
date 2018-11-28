#include <iostream>
#include <vector>
#include <algorithm>

//#include <assert.h>

using std::cin;
using std::cout;
using std::vector;

int main()
{
	int nCases = 0;

	cin >> nCases;
	for (int icase = 0; icase < nCases; ++icase)
	{
		int nCapacity = 0, nKeys = 0, nLetters = 0;

		cin >> nCapacity >> nKeys >> nLetters;

		vector<int> vFreqs;
		vFreqs.reserve(nLetters);
		for (int il = 0; il < nLetters; ++il)
		{
			int frq = 0;
			cin >> frq;
			vector<int>::iterator place = std::lower_bound(vFreqs.begin(), vFreqs.end(), frq);
			vFreqs.insert(place, frq);
		}

		int nPresses = 0;

		int nOnKeyNum = 1;
		int nKey = 1;
		for (vector<int>::reverse_iterator i = vFreqs.rbegin(); i != vFreqs.rend(); ++i)
		{
//			assert(nKey <= nCapacity);
			
			nPresses += ((*i) * nOnKeyNum);
			if (nKey == nKeys)
			{
				++nOnKeyNum;
				nKey = 1;
			}
			else
				++nKey;
		}

		cout << "Case #" << (icase+1) << ": " << nPresses << std::endl;
	}

	return 0;
}