#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	for (int i=0; i<t; i++)
	{
		char s[100];
		scanf("%s", s);
		static int ca = 0;
		printf("Case #%d: ", ++ca);
		int len = strlen(s);
		if (next_permutation(s, s+len))
		{
			printf("%s\n", s);
		}
		else
		{
			sort(s, s+len);
			bool first = true;
			for (int i=0; i<len; i++)
				if (s[i] != '0')
				{
					putchar(s[i]);
					if (first)
					{
						first = false;
						putchar('0');
						for (int j=0; j<len; j++)
							if (s[j] == '0')
								putchar('0');
					}
				}
			putchar(10);
		}
	
	}
}
