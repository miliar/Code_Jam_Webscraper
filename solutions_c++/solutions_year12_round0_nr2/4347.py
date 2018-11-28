#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int t, d[105][105], p, n, s, mas[105];
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	for(int tt = 1; tt <= t; ++tt)
	{
		scanf("%d%d%d", &n, &s, &p);
		memset(d, 0, sizeof(d));
		//d[0][0] = 1;
		for(int i = 0; i < n; ++i)
			scanf("%d", &mas[i]);
		for(int i = 0; i < n; ++i)
		{
			for(int j = 0; j <= i; ++j)
			{
				if(mas[i] >= 2 && mas[i] + 4 >= 3 * p 
					|| p == 0 
					|| p == 1 && mas[i] == 1)
					d[i+1][j+1] = max(d[i+1][j+1], d[i][j] + 1);
				else
					d[i+1][j+1] = max(d[i+1][j+1], d[i][j]);
				if(mas[i] >= 1 && mas[i] + 2 >= 3 * p 
					|| p == 0)
					d[i+1][j] = max(d[i+1][j], d[i][j] + 1);
				else
					d[i+1][j] = max(d[i+1][j], d[i][j]);
			}
		}
		printf("Case #%d: %d\n", tt, d[n][s]);
	}
	return 0;
}

/*
1 2 1 1 8 0
*/

/*
int t;
char str[105], ans[105];
string alph;
int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	alph = "yhesocvxduiglbkrztnwjpfmaq";

	scanf("%d", &t);
	gets(str);
	for(int tt = 0; tt < t; ++tt)
	{
		gets(str);
		int l = strlen(str);
		for(int j = 0; j < l; ++j)
			if(str[j] != ' ')
				ans[j] = alph[str[j] - 'a'];
			else
				ans[j] = ' ';
		ans[l] = 0;
		printf("Case #%d: %s\n", tt + 1, ans);
	}
	return 0;
}
*/

/*
yhesocvxduiglbkrztnwjpfma
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
*/