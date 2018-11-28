#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int L, D, N;

int main()
{
	
	//freopen("data/test.in", "r", stdin);
	//freopen("data/test.out", "w", stdout);
	//freopen("data/A-small-attempt0.in", "r", stdin);
	//freopen("data/A-small-attempt0.out", "w", stdout);
	freopen("data/A-large.in", "r", stdin);
	freopen("data/A-large.out", "w", stdout);

	int numTestCases;

	scanf("%d%d%d", &L, &D, &numTestCases);

	vector<string> dict(D);

	for (int d = 0; d < D; d++)
	{
		char word[15];
		scanf("%s", &word);

		string strword = word;
		dict[d] = strword;
	}

	//numTestCases = 1;

	for (int caseId = 1; caseId <= numTestCases; caseId++)
	{
		char testWord[65536];
		scanf("%s", &testWord);
	
		// make a copy
		vector<string> dictCopy(D);

		for (int d = 0; d < D; d++)
		{
			dictCopy[d] = dict[d];
		}
		
		int charPos = 0;
		char pattern[65536];
		char patternPos = 0;
		bool isGroup = false;

		for (int i = 0; i < strlen(testWord); i++)
		{
			char c = testWord[i];
			if (c == '(')
			{
				patternPos = 0;
				isGroup = true;
			}
			else if (isGroup && c >= 'a' && c <= 'z')
			{
				pattern[patternPos++] = c;
				pattern[patternPos] = 0;
			}
			else 
			{
				if (c == ')')
				{
					isGroup = false;
				}
				else
				{
					pattern[0] = c;
					pattern[1] = 0;
				}
			
				//cout << "pat=" << pattern << charPos << "\n";

				// eliminate
				for (vector<string>::iterator it = dictCopy.begin(); it != dictCopy.end();)
				{
					char dictChar = it->at(charPos);
					bool found = false;

					for (int pat = 0; pat < strlen(pattern); pat++)
					{
						if (dictChar == pattern[pat])
						{
							found = true;
							break;
						}
					}

					if (found == false)
					{
						//cout << "erasing " << *it << "\n";
						it = dictCopy.erase(it);
					}
					else
					{
						it++;
					}
				}

				patternPos = 0;
				isGroup = false;
				charPos++;

			}
		}
/*		for (vector<string>::iterator it = dictCopy.begin(); it != dictCopy.end(); it++)
		{
			cout << *it << "\n";
		}
		cout << "\n\n";*/

		printf("Case #%i: %i\n", caseId, dictCopy.size());
	}

	fflush(stdout);
}
