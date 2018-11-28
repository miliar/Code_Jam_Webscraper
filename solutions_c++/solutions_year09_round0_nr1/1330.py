#include<queue>

char m[5005][500];
char in[500];
int l, d, n;

bool match(int I)
{
	int pos = 0;
	for(int i = 0; i < l; i++, pos++)
	{
		if(in[pos] == '(')
		{
			bool found = 0;
			while(in[pos] != ')')
			{
				if(in[pos] == m[I][i])
					found = 1;
				pos++;
			}
			if(found == 0)
				return 0;
		}
		else if(in[pos] != m[I][i])
			return 0;
	}
	return 1;
}

int main()
{	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d%d%d\n", &l, &d, &n);
	for(int i = 0; i < d; i++)
		gets(m[i]);
	for(int i = 0; i < n; i++)
	{
		gets(in);
		int col = 0;
		for(int i = 0; i < d; i++)
			if(match(i))
				col++;
		printf("Case #%d: %d\n", i + 1, col);
	}
	return 0;
}