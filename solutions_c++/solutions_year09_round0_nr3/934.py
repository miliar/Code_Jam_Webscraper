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

int main()
{
	freopen("data/C-large.in", "r", stdin);
	freopen("data/C-large.out", "w", stdout);
	//freopen("data/C-small-attempt0.in", "r", stdin);
	//freopen("data/C-small-attempt0.out", "w", stdout);
//	freopen("data/test.in", "r", stdin);
//	freopen("data/test.out", "w", stdout);

	int numTestCases;

	scanf_s("%d", &numTestCases);
	
	char google [] = "welcome to code jam";
	//char google [] = "wee";

	for (int caseId = 1; caseId <= numTestCases; caseId++)
	{
		char source[5000];
		bool ok = true;
		int ch = 0;
		bool inited = false;
		while (ok)
		{
			char c;
			scanf("%c", &c);
			if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || c == ' ' || c == '.'  || c == ',' || c == '"'  || c == '\'' )
			{
				inited = true;
				source[ch++] = c;
			}
			else
			{
				if (inited) ok = false;
			}
		}
		source[ch] = 0;

		//scanf("%[^\t\n]", &source);

		int count[5000];
		for (int i = 0; i < strlen(source); i++) count[i] = 0;

		int c = 0;
		for (int i = 0; i < strlen(source); i++)
		{
			if (source[i] == google[0])
			{
				c++;
				c %= 10000;
			}
			count[i] = c;
		}

		//for (int i = 0; i < strlen(source); i++) printf("%d,", count[i]);printf("\n");

		
		for (int j = 1; j < strlen(google); j++)
		{
			c = 0;
			int prevCount = 0;

			for (int i = 0; i < strlen(source); i++)
			{
				if (source[i] == google[j])
				{
					c += prevCount;
					c %= 10000;
				}
				prevCount = count[i];
				count[i] = c;
			}
			//for (int i = 0; i < strlen(source); i++) printf("%d,", count[i]);printf("\n");
		}

		printf("Case #%i: %04d\n", caseId, count[strlen(source) - 1]);
	}

	fflush(stdout);
}
