#include <iostream>
#include <string>
using namespace std;

int l,d,n;
string data[5010];
string pattern;
bool pp[20][30];

int main()
{
	cin >> l >> d >> n;
	for (int i=1; i<=d; ++i)
		cin >> data[i];
	for (int x=1; x<=n; ++x)
	{
		int sum = 0;
		memset(pp, 0, sizeof(pp));
		cin >> pattern;

		int pos = 0;
		bool stay=false;
		for (int i=0; i<pattern.size(); ++i)
		{
			if (pattern[i] == '(')
			{
				++pos;
				stay = true;
			}
			else if (pattern[i] == ')')
			{
				stay = false;
			}
			else
			{
				if (!stay)
					++pos;
				int c2num = pattern[i] - 'a';
				pp[pos][c2num] = true;
			}
		}

		for (int i=1; i<=d; ++i)
		{
			bool f = true;
			for (int j=0; j<l; ++j)
			{
				int c2num = data[i][j] - 'a';
				if (!pp[j+1][c2num])
				{
					f = false;
					break;
				}
			}

			if (f)
				++sum;
		}

		//for (int k=0; k<pattern.length(); ++k)
		//{
		//	if (pattern[k] == '(') pattern[k] = '[';
		//	else if (pattern[k] == ')') pattern[k] = ']';
		//}
		//for (int j=1; j<=d; ++j)
		//{
		//	CRegexpT <char> regexp(pattern.c_str());
		//	MatchResult result = regexp.Match(data[j].c_str());
		//	if (result.IsMatched())
		//		++sum;
		//}
		cout << "Case #" << x << ": " << sum << endl;
	}

	return 0;
}