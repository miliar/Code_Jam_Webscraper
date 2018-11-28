#include <stdio.h>
#include <string.h>

char c[256][256], o[256][256];

int main()
{
	int cases;
	scanf(" %d", &cases);
	for(int cs=1; cs<=cases; cs++)
	{
		int n, pos=0;
		char s[101];
		memset(c, 0, sizeof(c));
		memset(o, 0, sizeof(o));
		scanf(" %d", &n);
		for(int i=0; i<n; i++)
		{
			char c1, c2, c3;
			scanf(" %c%c%c", &c1, &c2, &c3);
			c[c1][c2]=c3;
		}
		scanf(" %d", &n);
		for(int i=0; i<n; i++)
		{
			char c1, c2;
			scanf(" %c%c", &c1, &c2);
			o[c1][c2]=1;
		}
		scanf(" %d", &n);
		for(int i=0; i<n; i++)
		{
			scanf(" %c", s+(pos++));
			if ((pos>=2) && (c[s[pos-2]][s[pos-1]]))
			{
				s[pos-2]=c[s[pos-2]][s[pos-1]];
				pos--;
			}
			else if ((pos>=2) && (c[s[pos-1]][s[pos-2]]))
			{
				s[pos-2]=c[s[pos-1]][s[pos-2]];
				pos--;
			}
			for(int j=0; j<pos-1; j++)
				if ((o[s[pos-1]][s[j]]) || (o[s[j]][s[pos-1]]))
					pos=0;
		}
		printf("Case #%d: [", cs);
		for(int i=0; i<pos; i++)
			printf("%s%c", ((i)?(", "):("")), s[i]);
		printf("]\n");
	}
	return 0;
}
