#include <vector>
#include <string>
#include <iostream>
#include <memory.h>
#include <assert.h>
using namespace std;

int main()
{
	int l, d, n;
	cin >> l >> d >> n;
	vector<string> words;
	for(int i = 0; i < d; ++i)
	{
		string s;
		while(s.empty())
			getline(cin, s);
		words.push_back(s);
	}

	for(int i = 0; i < n; ++i)
	{
		string s;
		getline(cin, s);
		bool ok[16][256];
		bool inparen = false;
		int pos = -1;
		memset(ok, 0, sizeof(ok));
		for(unsigned j = 0; j < s.size(); ++j)
		{
			if(s[j] == '(')
			{
				inparen = true;
				++pos;
			}
			else if(s[j] == ')')
				inparen = false;
			else
			{
				if(!inparen)
					++pos;
				ok[pos][(unsigned char)s[j]] = true;
			}
		}
		assert(pos == (l - 1));
		int matches = 0;
		for(int k = 0; k < d; ++k)
		{
			for(int j = 0; j < l; ++j)
			{
				if(!ok[j][(unsigned char)words[k][j]])
					goto fail;
			}
			++matches;
			fail:;
		}

		cout << "Case #" << (i + 1) << ": " << matches << endl;
	}
	return 0;
}
