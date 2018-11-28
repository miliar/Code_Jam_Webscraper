#define _CRT_SECURE_NO_WARNINGS

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

#define ASSERT(X) {if (!(X)) {printf("\n assertion failed at line %d\n",__LINE__);exit(0);}}

char line[101];

//             "abcdefghijklmnopqrstuvwxyz"
string galph = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	int testcase;
	scanf("%d\n",&testcase);

	for (int case_id=1;case_id<=testcase;case_id++)
	{
		printf("Case #%d: ",case_id);
		fgets(line, sizeof(line), stdin);
		if (line[0] == 10)
		{
			fgets(line, sizeof(line), stdin);
		}
		for (int i = 0; i < strlen(line); i++)
		{
			char c = line[i];
			if (('a' <= c) && (c <= 'z'))
			{
				printf("%c", galph[c-'a']);
			}
			else
			{
				if (c == ' ')
				{
					putchar(c);
				}
			}
		}
		
			putchar('\n');
	}
	return 0;
}