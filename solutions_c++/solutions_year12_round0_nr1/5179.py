#include <iostream>
#include <string>
using namespace std;

int replace[27];

void Learning()
{
	memset(replace, -1, sizeof(replace));
	string testIn[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv"};

	string testOut[3] = {"our language is impossible to understand",
					"there are twenty six factorial possibilities",
					"so it is okay if you want to just give up"};

	for (int i = 0; i < 3; ++i)
	{
		int len = testIn[i].length();
		for (int j = 0; j < len; ++j)
		{
			if (testIn[i][j] != ' ')
				replace[testIn[i][j] - 'a'] = testOut[i][j] - 'a';
		}
	}

	//for (int i = 0; i < 26; ++i)
	//	printf("%c->%c\n", i + 'a', replace[i] + 'a');

}

int main()
{
	int t;

	Learning();
	replace['z' - 'a'] = 'q' - 'a';
	replace['q' - 'a'] = 'z' - 'a';

	char input[110];
	while (scanf("%d", &t) != EOF)
	{
		getchar();
		for (int i = 1; i <= t; ++i)
		{
			gets(input);
			int len = strlen(input);
			for (int j = 0; j < len; ++j)
				if (input[j] != ' ')
					input[j] = replace[input[j] - 'a'] + 'a';
			printf("Case #%d: ", i);
			puts(input);
		}

	}
	return 0;
}


/*
Input
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv


Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
*/