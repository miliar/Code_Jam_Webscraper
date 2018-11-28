
#include <stdio.h>

#include <algorithm>

#include <memory.h>

#include <math.h>

#include <string>

#include <functional>

#include <iostream>

#include <set>

#include <vector>

#include <list>

#include <map>

#include <queue>

#include <stack>

using namespace std;

const int MAX_N =  256;

const int MAX_L = 200001;

bool match (int L, string word, vector<string>& pattern)
{
	for (int i = 0; i < L; ++i)
	{
		if (pattern[i].find(word[i]) == -1)
		{
			return false;
		}
	}

	return true;
}

void Work ()
{
	freopen ("A-large.in", "r", stdin);
	freopen ("data.out", "w", stdout);

	int L = 0;
	int D = 0;
	int N = 0;
	int i = 0;
	int j = 0;
	int k = 0;

	scanf ("%d%d%d", &L, &D, &N);
	vector <string> dict(D);

	char t[450];

	getchar();
	for (i = 0; i < D; ++i)
	{
		gets (t);
		dict[i] = t;
	}

	
	for (i = 1; i <= N; ++i)
	{
		gets(t);
		int len = strlen(t);
		bool start = false;
		vector <string> pattern(L);
		k = -1;
		for (j = 0; j < len; ++j)
		{
			
			if (t[j] >= 'a' && t[j] <= 'z')
			{
				if (!start)
				{
					++k;
				}
				
				pattern[k] += t[j];
			}
			else
			{
				if (t[j] == '(')
				{
					start = true;
					++k;
				}
				else if (t[j] == ')')
				{
					start = false;
				}
			}
		}

		int res = 0;
		for (j = 0; j < D; ++j)
		{
			if (match (L, dict[j], pattern))
			{
				++res;
			}
		}

		printf ("Case #%d: %d\n", i, res);
	}
	
}



int main()
{
	Work ();

	return 0;
}

