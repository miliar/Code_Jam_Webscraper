#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

const string TESTSTR = "welcome to code jam";

int main(int argc, char* argv[])
{
	int N = 0;
	string firstLine;
	getline(cin, firstLine);
	stringstream ss(firstLine);
	ss >> N;
	for (int test = 1; test <= N; ++test)
	{
		string text;
		getline(cin, text);

		vector<vector<long long> > d(text.length(), vector<long long>(TESTSTR.length(), 0));
		for (int i = 0; i < d.size(); ++i)
		{
			for (int j = 0; j < TESTSTR.length(); ++j)
				if (TESTSTR[j] == text[i])
				{
					if (j == 0)
						d[i][j] = 1;
					else
					{
						for (int k = 0; k < i; ++k)
							if (TESTSTR[j - 1] == text[k])
								d[i][j] += d[k][j-1];
					}
				}
		}

		long long ans = 0;
		for (int i = 0; i < d.size(); ++i)
			ans += d[i][TESTSTR.length() - 1];

		stringstream ss;
		ss << ans;
		string ansStr;
		if (ss.str().length() < 4)
			ansStr = string(4 - ss.str().length(), '0') + ss.str();
		else
			ansStr = ss.str().substr(ss.str().length() - 4);

		cout << "Case #" << test << ": " << ansStr << endl;
	}

	return 0;
}
