#include <fstream>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	ifstream dataF("input.in");
	ofstream output("Ouput.out");
	int Nwires;
	int cases;
	if (dataF.is_open())
	{
		while (! dataF.eof() )
		{
			cases = 0;
			dataF >> cases;
			for(long i = 1; i <= cases; i++)
			{
				dataF>>Nwires;
				int left[4];
				int right[4];
				for(int k = 0; k < Nwires; k++)
				{
					dataF >> left[k];
					dataF >> right[k];
				}
				int result = 0;
				for(int f = 0; f < Nwires; f++)
				{
					for(int k = f+1; k< Nwires; k++)
					{
						if(left[k] > left[f] && right[k] < right[f])
							result++;
					}
				}


				output << "Case #" << i << ": " << result << endl;

			}
		}
		dataF.close();
	}
	else cout << "Unable to open file"; 
}
