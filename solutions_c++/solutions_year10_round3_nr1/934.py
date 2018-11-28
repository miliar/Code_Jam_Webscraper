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
	vector<int> a;
	vector<int> b;
	vector<int> sa;
	vector<int> sb;
			
public:
	Codejam(ifstream& input, ofstream& output) : input(input), output(output) {}

	void runtc()
	{
		input >> testcaseNum;
		getline(input, line);	// skip new line character
		int lines;
		
		for (int t = 0; t < testcaseNum; t++)
		{
			input >> n;
			getline(input, line);	// skip new line character
			a.clear();
			b.clear();
			sa.clear();
			sb.clear();

			int ai, bi;
			for (int i = 0; i < n; i++)
			{
				input >> ai >> bi;
				a.push_back(ai);
				b.push_back(bi);
				getline(input, line);	// skip new line character
			}

			sa = a;
			sb = b;

			sort(sa.begin(), sa.end());
			for (int i = 0; i < n; i++)
			{
				int index = find(a.begin(), a.end(), sa[i]) - a.begin();
				sb[i] = b[index];
			}

			int intersections = 0;
			for (int i = 0; i < n; i++)
			{
				if (i < n - 1)
				{
					for (int j = i + 1; j < n; j++)
					{
						if (sb[j] < sb [i])
							++intersections;
					}
				}
					
			}

			output << "Case #" << t+1 << ": " << intersections << endl;

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
