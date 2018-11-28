#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	ifstream ifs("b.in");
	ofstream ofs("b.out");
	int t;
	ifs >> t;
	for (int test = 0; test < t; ++test)
	{
		string s;
		ifs >> s;
		if (!next_permutation(s.begin(), s.end()))
		{
			s.insert(s.begin(), '0');
			sort(s.begin(), s.end());
			int j = 0;
			while (s[j] == '0') ++j;
			swap(s[j], s[0]);
		}
		ofs << "Case #"<< test+1 << ": " << s << endl;
	}
	return 0;
}