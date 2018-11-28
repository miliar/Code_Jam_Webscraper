#include <iostream>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

typedef long long lint;

map<char,int> codetab;
int nextdig;

int decode(char c)
{
	if (codetab.count(c))
		return codetab[c];

	codetab[c] = nextdig++;

	if (nextdig == 1) nextdig = 2;

	return codetab[c];
}

int main()
{
	int tc;
	cin >> tc;

	for (int casecnt = 1; casecnt <= tc; ++casecnt)
	{
		string n;
		cin >> n;

		string t = n;

		sort(t.begin(),t.end());

		int b = unique(t.begin(), t.end()) - t.begin();

		b = max(b,2);

		codetab.clear();
		nextdig = 0;
		codetab[n[0]] = 1;

		lint val = 0;

		for (size_t c = 0; c < n.size(); ++c)
		{
			val *= b;
			val += decode( n[c] );
		}

		cout << "Case #" << casecnt << ": " << val << endl;
	}

	return 0;
}
