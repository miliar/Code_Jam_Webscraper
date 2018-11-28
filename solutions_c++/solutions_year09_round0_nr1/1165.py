#include <stdio.h>
#include <string.h>

int l,d,n;
char w[60000][20];
char s[10000];

main() {
	int i,j,k;

	freopen("A-large.in","r",stdin);
	freopen("tmp.out","w",stdout);
	scanf("%d%d%d",&l,&d,&n);
	for (i = 0; i < d; ++i)
	{
		scanf("%s",w[i]);
	}

	for (i = 0; i < n; ++i)
	{
		scanf("%s",s);
		
		int count = 0;
		int end = strlen(s);
		int start;

		for (j = 0; j < d; ++j)
		{
			start = 0;
			for (k = 0; k < l; ++k)
			{
				if (start >= end)
				{
					break;
				}

				if (s[start] == '(')
				{
					++start;
					bool match = false;
					while (s[start]!=')')
					{
						if (s[start] == w[j][k])
						{
							match = true;
						}
						++start;
					}
					if (!match)
					{
						break;
					}
				}
				else 
				{
					if (s[start] != w[j][k])
					{
						break;
					}
				}
				++start;
			}

			if ( (start == end) && (k == l) )
			{
				count++;
			}
		}

		printf("Case #%d: %d\n", i+1, count);
	}
	
	return 0;
}
