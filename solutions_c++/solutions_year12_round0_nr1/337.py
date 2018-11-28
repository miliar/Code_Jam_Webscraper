#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

char dict0[] = {'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q'};
char dict[26];

void solve(istream& input, ostream& output)
{
	string line;
	getline(input, line);

	for (int i = 0; i < line.length(); ++i)
	{
		char ch = line[i];
		if (ch != ' ')
			ch = dict[ch - 'a'];
		output << ch;
	}
}

int main()
{
	for (int i = 0; i < 26; ++i)
		dict[dict0[i] - 'a'] = 'a' + i;

	int n;

	ifstream fin("A-small-attempt0.in");
	fin >> n;

	string dummy;
	getline(fin, dummy);

	ofstream fout("output.txt");

	for (int i = 1; i <= n; ++i)
	{
		fout << "Case #" << i << ": ";
		solve(fin, fout);
		fout << '\n';
	}
}