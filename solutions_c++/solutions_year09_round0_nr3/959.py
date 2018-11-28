#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int N, L;

char s[1000];
int d[1000][20];

char z[] = "!welcome to code jam";

int main()
{
	scanf("%d\n", &N);

	for(int t = 1; t <= N; t++)
	{
		printf("Case #%d: ", t);

		gets(s + 1);
		L = strlen(s + 1);

		memset(d, 0, sizeof d);
		d[0][0] = 1;

		for(int i = 1; i <= L; i++)
		for(int j = 1; j <= 19; j++)
		if (s[i] == z[j])
		for(int k = 0; k < i; k++) d[i][j] = (d[i][j] + d[k][j - 1]) % 10000;

		int res = 0;
		for(int i = 1; i <= L; i++) res = (res + d[i][19]) % 10000;

		printf("%04d\n", res);
	}

	return 0;
}