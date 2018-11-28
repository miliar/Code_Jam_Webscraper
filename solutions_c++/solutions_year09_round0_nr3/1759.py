#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int T, Slen;

const char *S = "welcome to code jam";

void solve(char* curCase, int pos, int elem, int clen, int &result)
{
	for (int i = pos; i < clen - Slen + elem + 1; i++)
		if (curCase[i] == S[elem])
		{
			if (elem == Slen - 1)
				result = (result + 1) % 10000;
			else
				solve(curCase, i + 1, elem + 1, clen, result);
		}
}

int main(int argc, char **argv)
{
	if (argc < 2) { cerr << "Please give input file name as parameter"; return 0; }

	ifstream input(argv[1]);
	if (input.bad()) { cerr << "Please give CORRECT input file name as parameter"; return 0; }
	ofstream output("output.out");
	if (output.bad()) { cerr << "Cannot create output file"; input.close(); return 0; }

	Slen = strlen(S);
	int clen;

	char *curCase = new char[501];
	input.getline(curCase, 501);
	T = atoi(curCase);
	int result;
	char *resStr = new char[5];

	for (int i = 0; i < T; i++)
	{
		result = 0;
		input.getline(curCase, 501);
		int clen = strlen(curCase);
		if (clen < Slen)
			result = 0;
		else
		{
			solve(curCase, 0, 0, clen, result);
		}
		resStr = itoa(result + 10000, resStr, 10);
		cout << "Case " << (i + 1) << " of " << T << endl;
		output << "Case #" << (i + 1) << ": " << resStr[1] << resStr[2] << resStr[3] << resStr[4] << endl;
	}

	input.close();
	output.close();
	cin.get();
	return 0;
}