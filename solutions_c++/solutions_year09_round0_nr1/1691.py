#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>

using namespace std;

int main(int argc, char **argv)
{
	if (argc < 1) { cerr << "Please give input file name as parameter"; return 0; }

	ifstream input(argv[1]);

	if (input.bad()) { cerr << "Please give CORRECT input file name as parameter"; return 0; }

	int L, D, N;
	input >> L >> D >> N;
	// read input words;
	string *words = new string[D];
	for (int i = 0; i < D; i++)
		input >> words[i];
	// read patterns
	string *patterns = new string[N];
	for (int i = 0; i < N; i++)
		input >> patterns[i];
	input.close();

	ofstream output("output.out");
	if (output.bad()) { cerr << "Cannot create output file"; return 0; }

	// patterns cycle
	bool isPar = false;
	vector<set<char> > checkVector;
	set<char> *cur;
	bool confirmed;
	int count;
	for (int i = 0; i < N; i++)
	{
		cout << "case " << (i + 1) << " of " << N << endl;
		count = 0;
		// build check vector
		checkVector.clear();
		for (unsigned int j = 0; j < patterns[i].length(); j++)
		{
			if (patterns[i][j] == '(') { isPar = true; cur = new set<char>; }
			else if (patterns[i][j] == ')') { isPar = false; checkVector.insert(checkVector.end(), *cur); }
			else 
			{
				if (isPar)
					cur->insert(patterns[i][j]);
				else
				{
					cur = new set<char>;
					cur->insert(patterns[i][j]);
					checkVector.insert(checkVector.end(), *cur);
				}
			}
		}

		// checking words
		for (int j = 0; j < D; j++)
		{
			confirmed = true;
			for (unsigned int k = 0; k < words[j].length(); k++)
			{
				if (checkVector[k].find(words[j][k]) == checkVector[k].end())
				{
					confirmed = false;
					break;
				}
			}
			if (confirmed) count++;
		}

		output << "Case #" << (i + 1) << ": " << count << endl;
	}

	output.close();
	cin.get();
	return 0;
}