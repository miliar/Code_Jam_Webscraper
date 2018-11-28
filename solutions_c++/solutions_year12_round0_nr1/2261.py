#include <stdio.h>

char* strange[3] = 
	{"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"};



char* good[3] = {"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"};

char mapping[128];

int main()
{
	for (int i = 0; i < 3; i++)
	{
		for (int x = 0; strange[i][x]; x++)
		{
			mapping[strange[i][x]] = good[i][x];
		}
	}

		mapping['e'] = 'o';
	mapping['q'] = 'z';
	mapping['z'] = 'q';

	/*for (int k = 'a'; k <= 'z'; k++)
	{
		printf("mapping %c -> %c\n", k, mapping[k]);
	}*/

	int T;
	char tlf[255];
	scanf("%d\n", &T);

	for (int k = 0; k < T; k++)
	{
		gets(tlf);
		char* tlf2 = tlf;
		printf("Case #%d: ", k + 1);
		while (*tlf2)
		{
			putc(mapping[*tlf2], stdout);
			tlf2++;
		}
		printf("\n");
	}
}
