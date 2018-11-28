#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <map>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

#define inf 2000000001
#define ll long long
#define minim(a, b) ((a < b) ? a : b)
#define maxim(a, b) ((a > b) ? a : b)
#define pii pair<int, int>
#define x first
#define y second
#define pb push_back
#define mp make_pair

int N, C, D, opp[32][32];
char comb[32][32];

char str[128], c, st[128];
int vf;

int main()
{
	int T, test, i, j;
	
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	scanf("%d", &T);
	for (test = 1; test <= T; ++test)
	{
		memset(comb, 0, sizeof(comb));
		memset(opp, 0, sizeof(opp));
		memset(st, 0, sizeof(st));		
		vf = -1;
		
		scanf("%d", &C);		
		for (i = 1; i <= C; ++i)
		{
			scanf("%s", str);
			comb[str[0]-'A'][str[1]-'A'] = str[2];
			comb[str[1]-'A'][str[0]-'A'] = str[2];
		}
		
		scanf("%d", &D);
		for (i = 1; i <= D; ++i)
		{
			scanf("%s", str);
			opp[str[0]-'A'][str[1]-'A'] = 1;
			opp[str[1]-'A'][str[0]-'A'] = 1;		
		}
		
		scanf("%d", &N);
		scanf("%s", str);
		for (i = 0; i < N; ++i)
		{
			c = str[i];
			while (vf >= 0 && comb[c-'A'][st[vf]-'A'])
				c = comb[c-'A'][st[vf--]-'A'];
			st[++vf] = c;
			
			for (j = 0; j < vf; ++j)
				if (opp[st[j]-'A'][c-'A'])
				{
					vf = -1;
					break;
				}
		}
		
		printf("Case #%d: [", test);
		if (vf < 0)
		{
			printf("]\n");
			continue;
		}
		
		for (i = 0; i < vf; ++i)
			printf("%c, ", st[i]);
		printf("%c]\n", st[vf]);
	}
	
	return 0;
}
