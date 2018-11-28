#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <algorithm>

using namespace std;

unsigned int to_int(string s)
{
	stringstream ss(s);
	int result;
	ss >> result;
	return result;
}

void allRecycledNumbers(unsigned int x, set<unsigned int> & result)
{
	stringstream ss;
	ss << x;
	string temp;
	ss >> temp;
	for (unsigned int i = temp.length() - 1; i > 0; --i)
	{
		string s = temp.substr(i, temp.length() - i) + temp.substr(0, i) ;
		if (s[0] != '0')
			result.insert(to_int(s));
	}
}

unsigned int recycledNumbers(unsigned int A, unsigned int B)
{
	if (A < 10)
		A = 10;

	if (A >= B)
		return 0;

	unsigned int result = 0;
	stringstream ssi;

	for (unsigned int i = A; i < B; ++i)
	{
		set<unsigned int> recycleds;
		allRecycledNumbers(i, recycleds);
		for(set<unsigned int>::const_iterator it(recycleds.begin()); it != recycleds.end(); ++it)
		{
			result += (*it <= B && *it > i);
		}
	}
	return result;
}

int main(int argc, char* argv[])
{
	if (argc != 3)
	{
		cout << "Usage: " << argv[0] << " <in-file> <out-file>" << endl;
		return 0;
	}

	ifstream ifs(argv[1]);
	ofstream ofs(argv[2]);

	string line;
	unsigned int nbTests = 0;
	// read nb tests
	ifs >> nbTests;
	getline(ifs, line);

	//solve each test cases
	for (unsigned int i = 0; i < nbTests; ++i)
	{
		line.clear();
		getline(ifs, line);
		stringstream sst(line);
		unsigned int A, B;
		sst >> A;
		sst >> B;

		ofs << "Case #" << (i+1) << ": " << recycledNumbers(A, B) << endl;
	}
	ifs.close();
	ofs.close();

	return 0;
}

