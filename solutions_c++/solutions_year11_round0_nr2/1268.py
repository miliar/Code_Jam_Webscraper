#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cctype>

using namespace std;
template <class T> T sqr(T a) { return a * a; }

char trans[30][30];
int opp[30][30];
char stk[500];
char s[500];
int stks, len;

int main()
{
#ifdef impetus
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int testnum;
	scanf("%d", &testnum);
	for (int tc = 0; tc < testnum; tc++)
	{
		memset(trans, -1, sizeof(trans));
		memset(opp, 0, sizeof(opp));
		int k;
		scanf("%d", &k);
		for (int i = 0; i < k; i++)
		{
			char ss[5];
			scanf("%s", ss);
			trans[ss[0] - 'A'][ss[1] - 'A'] = trans[ss[1] - 'A'][ss[0] - 'A'] = ss[2];
		}
		scanf("%d", &k);
		for (int i = 0; i < k; i++)
		{
			char ss[5];
			scanf("%s", ss);
			opp[ss[0] - 'A'][ss[1] - 'A'] = opp[ss[1] - 'A'][ss[0] - 'A'] = 1;
		}
		scanf("%d%s", &len, s);
		stks = 0;
		for (int i = 0; i < len; i++)
		{
			stk[stks++] = s[i];
			while (stks > 1 && trans[stk[stks - 1] - 'A'][stk[stks - 2] - 'A'] + 1)
				stk[stks - 2] = trans[stk[stks - 1] - 'A'][stk[stks - 2] - 'A'], stks--;
			int coll = 0;
			for (int j = 0; j < stks; j++)
				for (int k = j + 1; k < stks; k++)
					if (opp[stk[j] - 'A'][stk[k] - 'A'])
						coll = 1;
			if (coll)
				stks = 0;
		}
		printf("Case #%d: [", tc + 1);
		if (stks > 0)
			printf("%c", stk[0]);
		for (int i = 1; i < stks; i++)
			printf(", %c", stk[i]);
		printf("]\n");
	}
	return 0;
}