#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <cmath>

using namespace std;

__int64 find(const char *text, const char *phrase)
{
	if (*phrase == 0) return 1;

	__int64 num = 0;
	while (*text) {
		if (*text == *phrase) {
			num += find(text+1, phrase+1);
		}
		++text;
	}
	return num;
}

int main()
{
	const char *phrase = "welcome to code jam";
	int N;
	scanf("%d\n",&N);
	for (int i = 0;i<N;i++)
	{
		char line[512];
		gets(line);

		printf("Case #%d: %04d\n", i+1, (int)(find(line, phrase) % 1000));
	}

	return 0;
}
