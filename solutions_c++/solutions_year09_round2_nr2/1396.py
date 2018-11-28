#include <fstream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

ifstream fin ("input.txt");
ofstream fout("output.txt");

const int MAX = 520;

int l;
int v[MAX];
string s;
int n;

int main()
{
	fin >> n;

	for (int i = 0; i < n; ++i)
	{
		fin >> s;		

		if (!next_permutation(s.begin(), s.end()))
		{
			char c, t;
			c = '0';
			for (int i = 1; i < s.length(); ++i)
				swap(s[i], c);
			s += c;
		}
		
		fout << "Case #" << i+1 << ": ";

		while (s[0] == '0')
			next_permutation(s.begin(), s.end());
		fout << s;

		fout << endl;
	}

	return 0;
}