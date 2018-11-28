#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	ifstream input("input.txt");
	ofstream output("output.txt");

	int nLines;
	input >> nLines;

	for(int i = 0; i <nLines; i++)
	{
		int N;
		int S;
		int p;

		input >> N;
		input >> S;
		input >> p;

		vector<int> scores(N);
		for(int j = 0; j < N; j++)
			input >> scores[j];

		int googlerCount = 0;
		for(int j = 0; j < N; j++)
		{
				int base = (int) scores[j] / 3;
				
				switch (scores[j] % 3) 
				{
					case 0:
					{
						if(base >= p)
							++googlerCount;
						else {
							if(S>0 && base>0 && base+1>=p) {
								++googlerCount;
								--S;
							}
						}
						break;
					}
					
					case 1:
					{
						if(base >= p || base+1 >= p) {
							++googlerCount;
						}
						else {
							if(S > 0 && base + 1 >= p) {
								++googlerCount;
								S--;
							}
						}
						break;
					}
					
					case 2:
					{
						if(base + 1 >= p || base >= p) {
							++googlerCount;
						}
						else {
							if(S > 0 && base + 2 >= p) {
								++googlerCount;
								--S;
							}
						}
						break;
					}
				}
		}

		output << "Case #" << i + 1 << ": " << googlerCount << endl;
	}
}