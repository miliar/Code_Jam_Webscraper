#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <algorithm>
#include <cassert>

using namespace std;

const int L = 19;
const char w[L + 1] = "welcome to code jam";
const int nmax = 501;

char s[nmax + 10];
int a[nmax + 1][L + 1];
int n;

int main()
{
	int test_cnt;
	scanf("%d\n", &test_cnt);
	for (int test_id = 1; test_id <= test_cnt; ++test_id)
	{
		fgets(s, nmax + 10, stdin);
        memset(a, 0, sizeof(a));
        int n = (int)strlen(s);
        for (int i = 0; i < n; ++i)
        {
        	a[i][0] = 1;
        	for (int j = 1; j <= L; ++j)
        	{
        		a[i + 1][j] = (a[i][j] + a[i][j - 1]*(int)(s[i] == w[j - 1])) % 10000;
        	}
        }
        printf("Case #%d: %04d\n", test_id, a[n][L]);
	}

	return 0;
}
