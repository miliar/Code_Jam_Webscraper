#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	ifstream inFile;
	ofstream outFile;
	inFile.open("input.in", ios::in);
	outFile.open("output.out", ios::out);

	if (inFile.is_open())
	{
		int T;
		string A, B;
		string inputLine;

		getline(inFile, inputLine);
		T = atoi(inputLine.c_str());

		for (int i = 0; i < T; i++)
		{
			getline(inFile, inputLine);
			unsigned int position = inputLine.find_first_of(' ');
			A = inputLine.substr(0, position);
			inputLine.erase(0, position + 1);
			position = inputLine.find_first_of(' ');
			B = inputLine.substr(0, position);
			inputLine.erase(0, position + 1);

			string original, recycled;
			int count = 0;

			original = A;
			int original_int = atoi(A.c_str());

			while (original < B)
			{
				vector<string> recycled_numbers;
				for (unsigned int j = 1; j < A.size(); j++)
				{
					recycled = original.substr(j);
					recycled += original.substr(0, j);
					
					if (recycled > original && recycled <= B && !binary_search(recycled_numbers.begin(), recycled_numbers.end(), recycled))
					{
						recycled_numbers.push_back(recycled);
						sort(recycled_numbers.begin(), recycled_numbers.end());
						count++;
					}
				}
				original_int++;
				ostringstream ss;
				ss << original_int;
				original = ss.str();
			}

			if (outFile.is_open())
			{
				outFile << "Case #" << i + 1 << ": " << count << endl;
			}
		}
		outFile.close();
		inFile.close();
	}
	return 0;
}