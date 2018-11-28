#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

const char key[] = "welcome to code jam";
int N;
char inString[1000];

int table[1000][20];

int solve(void)
{
	int result = 0;

	int length = strlen(inString);

	for (int i = 0 ; i < length ; ++i)
	{
		if (inString[i] == key[0])
		{
			table[i][0] = 1;
		}
		else
		{
			table[i][0] = 0;
		}
		for (int j = 1 ; j < 19 ; ++j)
		{
			table[i][j] = 0;
			if (inString[i] == key[j])
			{
				for (int k = 0 ; k < i ; ++k)
				{
					table[i][j] += table[k][j - 1];
					table[i][j] %= 10000;
				}
			}
		}

		result += table[i][18];
		result %= 10000;
	}

	return result;
}

int main(void)
{
	scanf("%d ", &N);

	for (int t = 1 ; t <= N ; ++t)
	{
		fgets(inString, 1000, stdin);

		printf("Case #%d: %04d\n", t, solve());
	}
}
