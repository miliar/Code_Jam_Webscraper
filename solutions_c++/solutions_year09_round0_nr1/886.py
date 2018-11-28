#include <cstdio>
#include <cstring>

const int maxl = 15;
const int maxd = 5000;

char a[maxd][maxl + 1];
bool b[maxl][26];

int n, d, l;

void readQuery()
{
	int i;
	char ch;
	memset(b, 0, sizeof b);
	for (i = 0; i < l; i++)
	{
		scanf(" %c", &ch);
		if (ch != '(')
			b[i][ch - 'a'] = true;
		else
		{
			scanf(" %c", &ch);
			while (ch != ')')
			{
				b[i][ch - 'a'] = true;
				scanf("%c", &ch);
			}
		}
	}
}

bool match(int k)
{
	for (int i = 0; i < l; i++)
		if (!b[i][a[k][i] - 'a']) return false;
	return true;
}

int main()
{
//	freopen("A-large.in", "r", stdin);
//	freopen("a.out", "w", stdout);
	scanf("%d%d%d", &l, &d, &n);
	
	for (int i = 0; i < d; i++)
		scanf("%s", a[i]);
	
	for (int i = 0; i < n; i++)
	{
		readQuery();
		int k = 0;
		for (int j = 0; j < d; j++)
			if (match(j)) k++;
		printf("Case #%d: %d\n", i + 1, k);
	}
	
	return 0;
}
