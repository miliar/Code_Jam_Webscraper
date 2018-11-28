
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

const int MAX_N =  501;

const int MAX_L = 200001;


void Work ()
{
	// freopen ("data.in", "r", stdin);
	// freopen ("data.out", "w", stdout);
	
	int T = 0;
	int H = 0;
	int W = 0;

	int i = 0;
	int j = 0;
	int k = 0;
	int t = 0;


	scanf ("%d", &T);

	int f[MAX_N][20] = {0};

	string word;
	string codejam = "welcome to code jam";
	char temp[MAX_N];

	const int MOD = 10000;
	gets (temp);
	for (t = 1; t <= T; ++t)
	{
		gets (temp);
		word = temp;

		memset (f, 0, sizeof(f));

		if (word[0] == codejam[0])
		{
			f[0][0] = 1;
		}

		for (i = 1; i < word.size(); ++i)
		{
			for (j = 0; j < codejam.size(); ++j)
			{
				f[i][j] = f[i - 1][j] % MOD;
				if (j > 0 && word[i] == codejam[j])
				{
					f[i][j] += f[i - 1][j - 1] % MOD;
				}

				if (j == 0 && word[i] == codejam[j])
				{
					f[i][j] += 1;
					f[i][j] %= MOD;
				}
			}
		}
		printf ("Case #%d: %04d\n", t, f[word.size() - 1][codejam.size() - 1] % MOD);
	}

	
	
}



int main()
{
	Work ();

	return 0;
}

