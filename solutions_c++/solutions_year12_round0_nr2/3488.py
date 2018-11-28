// H.Marihot
// Google Code Jam 2012
// Qualification Round
// 13th April 2012
// Problem B

#include <iostream>

using namespace std;

int main()
{
	unsigned short T,N,S,p,triplet,possibleSurprising,output;
	cin >> T;
	for(unsigned short i = 0; i< T; i++)
	{
		output = 0;
		possibleSurprising = 0;
		cin >> N; // number of Googlers
		cin >> S; // number of surprising triplets
		cin >> p; // pivot
		if (p > 1)
		{
			for (unsigned int j = 0; j< N; j++)
			{
				cin >> triplet;
				if ((triplet >= (((p - 1) * 2) + p) ))
					output++;
				else if (triplet >= (((p - 2) * 2) + p))
					possibleSurprising++;
			}
		}
		else
		{
			for (unsigned int j = 0; j< N; j++)
			{
				cin >> triplet;
				if (triplet >= p)
					output++;
			}
		}
		if (possibleSurprising > S)
			output += S;
		else
			output += possibleSurprising;
			
		cout << "Case #" << i + 1 << ": " << output << endl;
	}
	return 0;
}
