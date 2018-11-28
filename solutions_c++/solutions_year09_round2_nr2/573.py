#include <string.h>
#include <algorithm>
#include <stdio.h>
using  namespace std;

int  main()
{
	int  T, CAS = 1;
	char  s[100], ts[100];
	int  i;
	//freopen("B2.in", "r", stdin);
	//freopen("B2.out", "w", stdout);
	scanf("%d", &T);
	while(T--)
	{
		printf("Case #%d: ", CAS++);
		scanf("%s", &s);
		if(strcmp(s, "0") == 0)
		{
			printf("10\n");
			continue;
		}
		strcpy(ts, s);
		int  len = strlen(s);
		if(next_permutation (s,s+len))
		{
			printf("%s\n", s);
		}
		else
		{
			strcpy(s, ts);
			for(i = 0; i < len; i++)
				if(s[i] != '0' && s[i] < s[0])
					swap(s[i], s[0]);
			printf("%c", s[0]);
			putchar('0');
			if(len > 1)
			{
				sort(s+1, s+len);	
				printf("%s\n", s+1);
			}
			else puts("");
		}
	}
	return 0;
}
