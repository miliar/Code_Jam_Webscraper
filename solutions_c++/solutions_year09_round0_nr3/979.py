#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>

using namespace std;

char pat[] = "welcome to code jam";
char line[1000];
int cc[1000][21];

int main()
{
	int n, i, j, k;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &n);
	gets(line);

	int ss = strlen(pat);

	for(i = 0; i < n; i++)
	{
		gets(line);
		int len = strlen(line);
		for(j = 0; j < 21; j++)
		{
			cc[0][j] = 0;
		}
		cc[0][0] = 1;
		for(j = 0; line[j]; j++)
		{
			cc[j + 1][0] = 1;
			for(k = 0; k < ss; k++)
			{
				cc[j + 1][k + 1] = cc[j][k + 1];
				if(line[j] == pat[k])
				{
					cc[j + 1][k + 1] = (cc[j + 1][k + 1] + cc[j][k]) % 10000;
				}
			}
		}
		printf("Case #%d: %04d\n", i + 1, cc[j][k]);
	}
	return 0;
}