#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <string>
#include <fstream>
#include <algorithm>
#include <stdio.h>
#include <iomanip>
#include <map>
#include <limits>

using namespace std;

class Codejam
{
	int testcaseNum;
	ifstream& input;
	ofstream& output;
	string line;
	int n;
	int k;
	vector<vector<char> > table;
	vector<vector<char> > rotated;
	
public:
	Codejam(ifstream& input, ofstream& output) : input(input), output(output) {}

	bool hasK(char c)
	{
		int x[] = {1, 1, 1, -1, -1, -1, 0, 0};
		int y[] = {0, 1, -1, -1, 0, 1, 1, -1};
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (rotated[i][j] == c)
				{
					for (int l = 0; l < 8; l++)
					{
						int count = 1;
						int row = i;
						int column = j;
						row += x[l];
						column += y[l];
						while (row >= 0 && row < n && column >= 0 && column < n && rotated[row][column] == c)
						{
							count++;
							if (count >= k)
								return true;
							row += x[l];
							column += y[l];
						}
					}
				}
			}
		}
		return false;
	}
		
	void runtc()
	{
		input >> testcaseNum;
		getline(input, line);	// skip new line character
		int lines;
		
		for (int t = 0; t < testcaseNum; t++)
		{
			input >> n >> k;
			getline(input, line);	// skip new line character
			char c;
			table.clear();
			rotated.clear();
			table = vector<vector<char> >(n, vector<char>(n, '.'));
			rotated = vector<vector<char> >(n, vector<char>(n, '.'));
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					
					input >> c;
					table[i][j] = c;
				}
				getline(input, line);	// skip new line character
			}
			
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					rotated[j][n-1-i] = table[i][j];
				}
			}
			for (int i = n - 2; i >= 0; i--)
			{
				for (int j = 0; j < n; j++)
				{
					if (rotated[i][j] != '.' && rotated[i + 1][j] == '.')
					{
						for (int l = i; l < n - 1 && rotated[l+1][j] == '.'; l++)
						{
							swap(rotated[l][j], rotated[l+1][j]);
						}
					}
				}
			}
			
			bool red = hasK('R');
			bool blue = hasK('B');

			string result;
			if (red && blue)
				result = "Both";
			else if (red)
				result = "Red";
			else if (blue)
				result = "Blue";
			else
				result = "Neither";

			output << "Case #" << t+1 << ": " << result << endl;

		}
	}
};

int main(int argc, char* argv[])
{
	ifstream input(argv[1]);
	ofstream output(argv[2]);
	Codejam c(input, output);
	c.runtc();
	cin.get();
}
