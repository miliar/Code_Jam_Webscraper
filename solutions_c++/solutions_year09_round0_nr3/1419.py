#include <fstream>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
	ifstream ifstr("C-large.in");

	char buf[1024];
	ifstr.getline(buf, 1024);
	int N = atoi(buf);

	ofstream ofstr("C-large.out");
	string pat = "welcome to code jam";
	for (int i = 0; i < N; ++i)
	{
		ifstr.getline(buf, 1024);
		string text = buf;
		vector<vector<int> > cache(pat.size(), vector<int>(text.size(), 0));
		cache[0][0] = text[0] == pat[0] ? 1 : 0;
		for (int j = 1; j < (int)text.size(); ++j)
		{
			for (int k = 0; k < (int)pat.size(); ++k)
			{
				if (pat[k] == text[j])
					if (k > 0)
						cache[k][j] = cache[k][j - 1] + cache[k - 1][j - 1];
					else
						cache[k][j] = cache[k][j - 1] + 1;
				else
					cache[k][j] = cache[k][j - 1];
				cache[k][j] %= 10000;
			}
		}
		int count = cache[pat.size() - 1][text.size() - 1];
		ofstr << "Case #" << i + 1 << ": " << count / 1000 << count % 1000 / 100 << count % 100 / 10 << count % 10 << "\n";
		cout  << "Case #" << i + 1 << ": " << cache[pat.size() - 1][text.size() - 1] <<  "\n";
	}

	return 0;
}