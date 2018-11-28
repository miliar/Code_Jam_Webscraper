#define _CRT_SECURE_NO_WARNINGS
#include "stdio.h"
#include "iostream"
#include "string"
#include "algorithm"
#include "vector"
#include "queue"
#include "map"

using namespace std;

#define all(s) s.begin(), s.end()


int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	typedef vector<char> pat_letter;

	int l, d, n;
	cin >> l >> d >> n;

	vector<string> words;
	vector<vector<pat_letter> > patterns;

	for (int i = 0; i < d ; i++)
	{
		string s;
		cin >> s;
		words.push_back(s);
	}
		

	for (int i = 0; i < n ; i++)
	{
		string s;
		cin >> s;
		bool mult = false;
		pat_letter p;
		vector<pat_letter> pattern;

		for (int j = 0; j < s.length() ; j++)
		{
			char c = s[j];
			switch (c)
			{
			case '(':
				mult = true; break;
			default:
				p.push_back(c);
				if (mult)
				{					
					break;
				}
				
			case ')':
				mult = false;
				sort(all(p));
				pattern.push_back(p);
				p = pat_letter();				
			}
		}


		patterns.push_back(pattern);
	}

	//////////////////////////////////////////////////////////////////////////

	vector<int> res(n);
	
	for (int i = 0; i < d ; i++)
	{
		for (int j = 0; j < n ; j++)
		{
			bool ok = true;
			for (int k = 0; k < l ; k++)
			{
				if (!binary_search(all(patterns[j][k]), words[i][k]))
				{
					ok = false;
					break;
				}
			}

			if (ok)
				res[j]++;
		}
	}

	for (int i = 0; i < n ; i++)
	{
		printf("Case #%d: %d\n", i + 1, res[i]);
	}
}