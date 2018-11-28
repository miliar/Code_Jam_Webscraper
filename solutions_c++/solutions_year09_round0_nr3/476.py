#include <iostream>

using namespace std;

const int MOD = 10000;

const char *pattern = "welcome to code jam";
int pattLen;

int N;
char text[512];
int textLen;
int cache[512][32];

int getAmount(int textAt, int pattAt)
{
	int &res = cache[textAt][pattAt];
	if (res != -1)
		return res;
	if (pattAt >= pattLen)
		res = 1;
	else if (textAt >= textLen)
		res = 0;
	else {
		res = getAmount(textAt + 1, pattAt);
		if (text[textAt] == pattern[pattAt]) {
			res += getAmount(textAt + 1, pattAt + 1);
			if (res >= MOD)
				res -= MOD;
		}
	}
	return res;
}

int main()
{
	pattLen = strlen(pattern);
	scanf("%d\n", &N);
	for (int casenum = 1; casenum <= N; ++casenum) {
		gets(text);
		textLen = strlen(text);
		memset(cache, -1, sizeof(cache));
		printf("Case #%d: %04d\n", casenum, getAmount(0, 0));
	}
	return 0;
}
