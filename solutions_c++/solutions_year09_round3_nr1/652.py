#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <math.h>

using std::ifstream;
using std::cout;
using std::endl;
using std::string;
using std::map;

int main(int argc, char **argv)
{
	ifstream infile(argv[1]);

	int t;

	infile >> t;

	for (int i = 0; i < t; i++)
	{
		map<char, int> dict;
		string l;
		int curnum = -1;
		int minval = 0;

		infile >> l;

		for (int j = 0; j < l.length(); j++)
		{
			char c = l[j];

			if (dict.find(c) == dict.end())
			{
				if (curnum == -1) curnum = 1;
				else if (curnum == 1) curnum = 0;
				else if (curnum == 0) curnum = 2;
				else curnum++;

				dict[c] = curnum;
			}

		}

		if (curnum < 2) curnum = 2;
		else if (curnum >= 2) curnum++;

		for (int j = 0; j < l.length(); j++)
		{
			char c = l[j];
			//cout << c << " is " << dict[c] << " of " << curnum << endl;
			minval += pow(curnum, (l.length() - j - 1)) * dict[c];
			//cout << "minval is now " << minval << endl;

			//cout << dict[c];
		}

		cout << "Case #" << i + 1 << ": ";
		//cout << "\t" << l << "\t";
		cout << minval;

		//cout << "\t" << curnum;

		cout << endl;
	}

	infile.close();
}
