#include <fstream>
#include <vector>
#include <iostream>
#include <sstream>
#include <set>

using namespace std;

int main()
{
	ifstream ifstr("a-large.in");

	int T;
	ifstr >> T;

	ofstream ofstr("a-large.out");

	for (int t = 0; t < T; ++t)
	{
		int N;
		ifstr >> N;

		vector<string> rows;
		for (int i = 0; i < N; ++i)
		{
			string row;
			ifstr >> row;
			rows.push_back(row);
		}

		int res = 0;
		for (int i = 0; i < N; ++i)
		{
			int j = i;
			for (; j < N; ++j)
			{
				size_t pos = rows[j].find_last_of('1');
				if (pos == string::npos || pos <= i)
					break;
				++res;
			}
			string str = rows[j];
			for (int k = j; k > i; --k)
				rows[k] = rows[k - 1];
			rows[i] = str;
		}

		cout << "Case #" << t + 1 << ": " << res <<  "\n";
		ofstr << "Case #" << t + 1 << ": " << res <<  "\n";
	}

	return 0;
}