#include <stdio.h>
#include <algorithm>
using namespace std;

const int N = 110;

int v[N];
int po[N];
int pb[N];
int f[N];
char s[N];

int iabs(int x)
{
	if (x > 0) return x;
	return -x;
}

int main ()
{
	//freopen("A-large (1).in", "r", stdin);
	//freopen("A-large (1).out", "w", stdout);
	int ca;
	scanf("%d", &ca);
	int n;
	for (int k = 1; k <= ca; k++)
	{
		scanf("%d", &n);
		int x;
		int lasto = 0, lastb = 0;
		v[0] = 1;
		char ch[10];
		for (int i = 1; i <= n; i++)
		{
			scanf("%s%d", ch, &v[i]);
			s[i] = ch[0];
			po[i] = lasto;
			pb[i] = lastb;									
			if (ch[0] == 'O') lasto = i;
			else lastb = i;				
		}
		f[0] = 0;
		for (int i = 1; i <= n; i++)
		{
			if (s[i] == 'O')
			{
				f[i] = std::max(f[po[i]] + iabs(v[i] - v[po[i]]) + 1 , f[pb[i]] + i - pb[i]);
			}
			else
			{
				f[i] = std::max(f[pb[i]] + iabs(v[i] - v[pb[i]]) + 1 , f[po[i]] + i - po[i]);
			}
		}
		printf("Case #%d: %d\n", k, f[n]);
	}
	return 0;
}
