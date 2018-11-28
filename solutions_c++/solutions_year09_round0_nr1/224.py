#include <stdio.h>
#include <cstring>
#define maxl 5010

char str[maxl][20], s[5000];
int n, m, l, len;

bool match(char a[], char b[])
{
	int p = 0;
	for(int i=0; i<l; ++i)
	{
		if(p >= len) return 0;
		if(b[p]!='(')
		{
			if(a[i] != b[p]) return 0;
		}
		else
		{
			p++;
			int flag = 0;
			while(b[p]!=')')
			{
				if(a[i] == b[p]) flag = 1;
				p++;
			}
			if(!flag) return 0;
		}
		p++;
	}
	return 1;
}

void solve(int tc)
{
	printf("Case #%d: ", tc);

	scanf("%s", s);

	len = strlen(s);

	int ans = 0;
	for(int i=0; i<m; ++i)
	{
		if(match(str[i], s)) ans++;
	}
	printf("%d\n", ans);
}

int main()
{
	while(scanf("%d%d%d", &l, &m, &n) != EOF)
	{
		for(int i=0; i<m; ++i) scanf("%s", str[i]);
		for(int i=1; i<=n; ++i) solve(i);
	}
	return 0;
}

