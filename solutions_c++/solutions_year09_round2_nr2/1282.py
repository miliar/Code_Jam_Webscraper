#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main( int argc, char** argv )
{
	ifstream fin;

	fin.open( argv[1] );

	int T;
	
	stringstream line;

	char tmp[1024];
	fin.getline(&tmp[0], 1024);
	line.str(tmp);
	line >> T;

	for (int caseNumber = 0; caseNumber < T; caseNumber++)
	{
		cout << "Case #" << (caseNumber + 1) << ": ";
		
		fin.getline(&tmp[0], 1024);
		int N;
		line.str(tmp);
		line.seekg(0);
		line >> N;
		
		int N2 = N;
		vector<int> digits;
		
		int D[10];
		for (int i = 0; i < 10; i++)
		{
			D[i] = 0;
		}

		while (N2 > 0)
		{
			int digit = N2 % 10;
			N2 /= 10;

			D[digit]++;

			digits.push_back(digit);
		}
		
		int number = N+1;
		while(1)
		{
			int D2[10];
			for (int i = 0; i < 10; i++)
			{
				D2[i] = 0;
			}
			N2 = number;
			
			while (N2 > 0)
			{
				int digit = N2 % 10;
				N2 /= 10;

				D2[digit]++;
			}

			bool fail = false;
			for (int i = 1; i < 10; i++)
			{
				if (D[i] != D2[i])
				{
					fail = true;
					break;
				}
			}

			if (!fail)
			{
				cout << " " << number << endl;
				break;
			}

			number++;
		}

	}

	fin.close();

	return 0;
}