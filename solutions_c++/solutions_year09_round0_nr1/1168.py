#include <cstdio>
#include <cstring>

using namespace std;

int L, D, N, len, t, i, j, k, ok, ret;
char rijec[5010][20], pattern[1000], moze[20][30];

int main(void)
{
	scanf("%d %d %d", &L, &D, &N);

	for (i = 0; i < D; ++i) scanf("%s", rijec[i]);

	for (i = 1; i <= N; ++i) 
	{
		scanf("%s", pattern);
		len = strlen(pattern);

		memset(moze, 0, sizeof moze);

		for (j = t = 0; j < len; ++j, ++t) 
			if (pattern[j] == '(') {
				for (++j; pattern[j] != ')'; ++j) moze[t][pattern[j] - 'a'] = 1;
			} else 
				moze[t][pattern[j] - 'a'] = 1;

		for (j = ret = 0; j < D; ++j) {
			ok = 1;
			for (k = 0; k < L; ++k) ok &= moze[k][rijec[j][k] - 'a'];
			ret += ok;
		}

		printf("Case #%d: %d\n", i, ret);
	}

	return 0;
}
