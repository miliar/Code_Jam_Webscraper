#include <cstdio>
#include <cstring>
using namespace std;

#define MAX 256

char co[MAX][MAX];
bool op[MAX][MAX];
char res[MAX];
int len;

int main()
{
	int T, caseT, n, i, j, k, c, d;
	char str[MAX];

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	scanf("%d", &T);
	for (caseT=1; caseT<=T; ++caseT)
	{
		memset(co, 0, sizeof(co));
		memset(op, 0, sizeof(op));
		scanf("%d", &c);
		while (c--)
		{
			scanf("%s", str);
			co[str[0]][str[1]] = str[2];
			co[str[1]][str[0]] = str[2];
		}
		scanf("%d", &d);
		while (d--)
		{
			scanf("%s", str);
			op[str[0]][str[1]] = 1;
			op[str[1]][str[0]] = 1;
		}
		scanf("%d%s", &n, str);
		len = 0;
		for (i=0; i<n; ++i)
		{
			if (len > 0)
			{
				if (co[res[len-1]][str[i]] != 0) res[len-1] = co[res[len-1]][str[i]];
				else
				{
					for (j=len-1; j>=0; --j)
						if (op[str[i]][res[j]])
						{
							len = 0;
							break;
						}
					if (j < 0) res[len++] = str[i];
				}
			}
			else res[len++] = str[i];
		}
		printf("Case #%d: [", caseT);
		for (i=0; i<len; ++i)
			if (i == 0) printf("%c", res[i]);
			else printf(", %c", res[i]);
		puts("]");
	}
	return 0;
}