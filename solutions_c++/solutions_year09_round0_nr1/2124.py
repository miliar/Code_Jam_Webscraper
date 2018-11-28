#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>


#define MAX(a,b) ((a)>(b))?(a):(b)

using namespace std;

typedef struct _LetterGroup
{
	vector<char> letters;
} LetterGroup;

void main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out", "w", stdout);

	int L, D, N;
	cin >> L >> D >> N;
	vector<string> words;
	
	for (int d = 0; d < D; d++)
	{
		string word;
		cin >> word;
		words.push_back(word);
	}

	for (int n = 0; n < N; n++)
	{
		string pattern;
		cin >> pattern;
		vector<LetterGroup> ptn;

		bool inGroup = false;
		LetterGroup lg;
		for (int i = 0; i < pattern.size(); i++)
		{
			if (pattern[i] == '(')
			{
				inGroup = true;
				lg.letters.clear();
			}
			else if (pattern[i] == ')')
			{
				inGroup = false;
				ptn.push_back(lg);
				lg.letters.clear();
			}
			else
			{
				if (!inGroup)
				{
					lg.letters.clear();
					lg.letters.push_back(pattern[i]);
					ptn.push_back(lg);
					lg.letters.clear();
				}
				else
				{
					lg.letters.push_back(pattern[i]);
				}
			}
		}

		int matchTimes= 0;
		for (int d = 0; d < D; d++)
		{
			bool match = true;
			for (int l = 0; l < L; l++)
			{
				bool pass = false;
				for (int k = 0; k < ptn[l].letters.size(); k++)
				{
					if (words[d][l] == ptn[l].letters[k])
					{
						pass = true;
						break;
					}
				}
				if (!pass)
				{
					match = false;
					break;
				}
			}
			if (match)
				matchTimes++;
		}
		cout << "Case #" << n+1 << ": " << matchTimes << endl;
		cerr << "Case #" << n+1 << ": " << matchTimes << endl;
	}

}