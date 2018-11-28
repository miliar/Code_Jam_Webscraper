#include <fstream>

using namespace std;


int main()
{
	int numberCases;
	ifstream in("C-large.in");
	ofstream out("C-large.out");
	in >> numberCases;
	for(int i = 0; i < numberCases; i++)
	{
		int numberCandies, sumCandiesValues = 0, xorCandiesValues = 0, smallestCandiesValue = 1000000;
		in >> numberCandies;
		while(numberCandies-- > 0)
		{
			int candyValue = 0;
			in >> candyValue;
			sumCandiesValues += candyValue;
			xorCandiesValues ^= candyValue;
			if(smallestCandiesValue > candyValue)
			{
				smallestCandiesValue = candyValue;
			}
		}
		if(xorCandiesValues == 0)
		{
			out << "Case #" << (i + 1) << ": " << (sumCandiesValues - smallestCandiesValue) << endl;
		}
		else
		{
			out << "Case #" << (i + 1) << ": NO" << endl;
		}
	}
	return 0;
}
