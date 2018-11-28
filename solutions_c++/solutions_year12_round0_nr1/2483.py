
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cassert>

using namespace std;


char *a = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
char *b = "our language is impossible to understand there are twenty six factorial possibilitiesso it is okay if you want to just give up";

int main(int argc, char* argv[])
{
	int T;
	vector<char> map;
	map.resize(26);

	char *c = a;
	char *d = b;
	while (*c)
	{
		if ((*c >= 'a') && (*c <= 'z'))
			map[*c - 'a'] = *d;
		c++;
		d++;
	}
	//map['z' - 'a'] = 'q';
	//map['q' - 'a'] = 'z';
	map['z' - 'a'] = 'q';
	map['q' - 'a'] = 'z';


	//for(int i = 0; i < 26; i++)
	//	printf("%c = %c\n", 'a' + i, map[i]);

	char line[200] = {0};
	scanf( " %d ", &T);
	for(int t = 1; t <= T; t++)
	{

		printf("Case #%d: ", t);
		line[0] = 0;
		fgets(line, 200, stdin);
		char *x = line;
		while(*x)
		{
			if ((*x >= 'a') && (*x <= 'z'))
			{
				printf("%c", map[*x - 'a']);
			}
			else if (*x == ' ')
				printf("%c", *x);
			x++;
		}
		printf("\n");

	}


	return 0;
}

