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
	int n, k, b, time;
	vector<int> x;
	vector<int> v;
			
public:
	Codejam(ifstream& input, ofstream& output) : input(input), output(output) {}

	void runtc()
	{
		input >> testcaseNum;
		getline(input, line);	// skip new line character
		int lines;
		
		for (int t = 0; t < testcaseNum; t++)
		{
			x.clear();
			v.clear();
			input >> n >> k >> b >> time;
			getline(input, line);	// skip new line character
			int xi;
			for (int i = 0; i < n; i++)
			{
				input >> xi;
				x.push_back(xi);
			}
			getline(input, line);	// skip new line character
			int vi;
			for (int i = 0; i < n; i++)
			{
				input >> vi;
				v.push_back(vi);
			}
			getline(input, line);	// skip new line character

			reverse(x.begin(), x.end());
			reverse(v.begin(), v.end());

			int possible = 0;
			for (int i = 0; i < n; i++)
			{
				if (((double) (b - x[i]))/v[i] <= time)
					++possible;
			}
			
			if (possible < k)
			{
				output << "Case #" << t+1 << ": " << "IMPOSSIBLE" << endl;
				continue;
			}
			
			possible = 0;
			int notPossible = 0;
			int swaps = 0;
			for (int i = 0; possible != k; i++)
			{
				if (((double) (b - x[i]))/v[i] <= time)
				{
					++possible;
					swaps += notPossible;
				}
				else
					++notPossible;
			}

			output << "Case #" << t+1 << ": " << swaps << endl;

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
