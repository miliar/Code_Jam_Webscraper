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
	FILE *streamIn;
	FILE *streamOut;

	//freopen_s(&streamIn, "data/test.in", "r", stdin);
	//freopen_s(&streamOut, "data/test.out", "w", stdout);
	//freopen_s(&streamIn, "data/B-small-attempt0.in", "r", stdin);
	//freopen_s(&streamOut, "data/B-small-attempt0.out", "w", stdout);
	freopen_s(&streamIn, "data/B-large.in", "r", stdin);
	freopen_s(&streamOut, "data/B-large.out", "w", stdout);
	
	int numTestCases;

	scanf_s("%d", &numTestCases);

	for (int caseId = 1; caseId <= numTestCases; caseId++)
	{
		char str[30];
		scanf_s("%s", str, 30);

		char num[30];
		memset(num, '0', sizeof(num));

		char ret[31];
		ret[30] = 0;

		char out[31];

		for (int i = 30 - strlen(str); i < 30; i++)
		{
			num[i] = str[i - 30 + strlen(str)];
		}

		for (int i = 28; i >= 0; i--)
		{
			if (num[i] < num[i+1])
			{
				char v = num[i];

				char n = 127;
				char idx;

				for (int j = i + 1; j < 30; j++)
				{
					if (num[j] > v && num[j] <= n)
					{
						n = num[j];
						idx = j;
					}
				}

				num[i] = n;
				num[idx] = v;

				//memset(ret, '0', sizeof(ret));

				for (int k = 0; k < i; k++)
				{
					ret[k] = num[k];
				}

				ret[i] = n;
				
				for (int k = i + 1; k < 30; k++)
				{
					ret[k] = num[30 - (k - i)];
				}

				int l =0;
				while (ret[l] == '0')
				{
					l++;
				}

				int m = 0;
				while (l < 30)
				{
					out[m++] = ret[l++];
				}
				out[m] = 0;

				break;
			}
		}

		printf("Case #%i: %s\n", caseId, out);
	}

	fflush(stdout);
}
