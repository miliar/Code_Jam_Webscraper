#include <iomanip>
#include <algorithm>
#include <map>
#include <fstream>
#include <stack>
#include <queue>
#include <vector>
#include <cmath>
#include <iostream>
#include <string>
#include <set>

#include <time.h>
#include <sys/time.h>

using namespace std;

char a[40][40];
int b[40][40];
char ans[110];

int re(int o)
{	
	if (o <= 1) return o;
	int x = ans[o-2] - 'A';
	int y = ans[o-1] - 'A';
	if (a[x][y] != '1') { ans[o-2] = a[x][y]; o--; }
	return o;
};

int main()
{
//	freopen("anarc05b.in","r",stdin);
//	freopen("anarc05b.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int t = 0; t < T; t++)
	{
		printf("Case #%d: [",t+1);

		for (int i = 0; i < 32; i++)
		for (int j = 0; j < 32; j++)
		{
			a[i][j] = '1';
			b[i][j] = 0;
		}

		int n;
		scanf("%d",&n);
		for (int i = 0; i < n; i++)
		{
			string s;
			cin >> s;
			int x = s[0] - 'A';
			int y = s[1] - 'A';
			a[x][y] = s[2];
			a[y][x] = s[2];
		}

		int m;
		scanf("%d",&m);
		for (int i = 0; i < m; i++)
		{
			string s;
			cin >> s;
			int x = s[0] - 'A';
			int y = s[1] - 'A';
			b[x][y] = 1;
			b[y][x] = 1;
		}

		int p;

		scanf("%d",&p);

		string s;
		cin >> s;

		int o = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (o == 0) { ans[o++] = s[i]; continue; }

			ans[o++] = s[i];
			o = re(o);
			for (int j = o-1; j >= 0; j--)
			{
				int x = ans[o-1] - 'A';
				int y = ans[j] - 'A';
				if (b[x][y] == 1)
				{
					o = 0;
					break;
				}
			}
		}

		for (int i = 0; i < o-1; i++)
			printf("%c, ",ans[i]);

		if (o != 0) printf("%c",ans[o-1]);
		printf("]\n");
	}
//	in.getline(s);

	return 0;	
}
