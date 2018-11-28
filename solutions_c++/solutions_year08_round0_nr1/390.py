#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

const int SL = 100;
const int QL = 1000;

int main()
{
	int N;


	scanf("%d\n", &N)	;
	for (int i = 1; i <= N; ++i)
	{
		int ret = 0;
		int flags[SL + 2] = {0};

		vector<string> engines;
		int S;
		scanf("%d\n",&S);
		int t = S;
		while (t--)
		{
			char input[103] = {0};
			fgets(input, 101, stdin);
			engines.push_back(string(input));
		}

		int Q;
		scanf("%d\n",&Q);
		t = Q;

		while(t--)
		{
			char input[102] = {0};
			fgets(input, 101, stdin);

			int j;
			for ( j = 0; j < S; ++j)
			{
				string temp(input);
				if (engines[j] == temp)
					break;
			}

			flags[j + 1] = 1;

			bool ok = false;

			int kk;
			for ( kk = 1; kk <= S ; ++kk )
			{
				if (flags[kk] == 0)
				{
					break;
				}
			}

			if (kk > S)
			{
				ok = true;
			}

			if (ok)
			{
				for (int k = 1; k <= S ; ++k )
				{
					flags[k] = 0;
				}

				flags[j+1] = 1;

				++ret;
			}

		}
		fprintf(stdout, "Case #%d: %d\n", i, ret);
	}
}


