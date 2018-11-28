#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	ifstream ifs("a.in");
	ofstream ofs("a.out");
	int l, d, t;
	ifs >> l >> d >> t;
	vector<string> words(d);
	for (int i= 0; i < d; ++i)
	{
		ifs >> words[i];
	}
	for (int test = 0; test < t; ++test)
	{
		string s;
		ifs >> s;
		int res = 0;
		int pos = 0;
		vector<vector<int> > v;
		for (int i = 0; i < l; ++i)
		{
			vector<int> tmp(26, 0);
			if (s[pos] == '(')
			{
				++pos;
				while (s[pos] != ')')
				{
					tmp[s[pos]-'a'] = 1;
					++pos;
				}
			}
			else 
			{
				tmp[s[pos]-'a'] = 1;
			}
			v.push_back(tmp);
			++pos;
		}
		for (int i = 0; i < d; ++i)
		{
			bool ok = true;
			for (int j =0; j < l; ++j)
				if (v[j][words[i][j]-'a'] == 0) {ok = false; break;} 
			if (ok) ++res;
		}
		ofs << "Case #" << test+1 << ": " << res << endl;
	}
	return 0;
} 