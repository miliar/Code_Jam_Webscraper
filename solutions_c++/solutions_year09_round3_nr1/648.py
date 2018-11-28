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

#define MAX 64

using namespace std;

int main()
{

	FILE *streamIn;
	FILE *streamOut;

	//freopen_s(&streamIn, "data/test.in", "r", stdin);
	//freopen_s(&streamOut, "data/test.out", "w", stdout);
	freopen_s(&streamIn, "data/A-small-attempt1.in", "r", stdin);
	freopen_s(&streamOut, "data/A-small-attempt1.out", "w", stdout);
	//freopen_s(&streamIn, "data/A-large.in", "r", stdin);
	//freopen_s(&streamOut, "data/A-large.out", "w", stdout);
	
	int numTestCases;
	scanf_s("%d", &numTestCases);

	for (int caseId = 1; caseId <= numTestCases; caseId++)
	{
		char num[MAX];
		scanf_s("%s", num, MAX);

		int digitsUsed[256];
		memset(digitsUsed, 0, sizeof(digitsUsed));
		int minBase = 0;
		for (int i=0;i<strlen(num);i++)
		{
			digitsUsed[num[i]]++;
		}
		for (int i=0;i<256;i++)
		{
			if (digitsUsed[i])minBase++;
		}

		if (minBase<=1)minBase=2;

		int digits[256];
		memset(digits,0,sizeof(digits));
		digits[0]=1;
		digits[1]=0;
		for (int i=2;i<minBase;i++)
		{
			digits[i]=i;
		}

		int assignment[256];
		for (int i=0;i<256;i++)assignment[i]=-1;
		
		unsigned long long ret=0;
		int a=0;

		for (int i=0;i<strlen(num);i++)
		{
			if (assignment[num[i]]==-1)
			{
				assignment[num[i]] = digits[a++];
			}

			ret = ret * minBase + assignment[num[i]];
		}

		printf("Case #%d: %d\n", caseId, ret);
	}

	fflush(stdout);
}
