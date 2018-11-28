#include <stdio.h>
#include <stdlib.h>

#include <vector>
#include <list>
#include <map>

using namespace std;

char *alphabet   = "abcdefghijklmnopqrstuvwxyz ";
char *googlerese = "ynficwlbkuomxsevzpdrjgthaq ";

int main(int argc, char **argv)
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int T;
	char buf[128];
	scanf("%d", &T);
	gets(buf);

	map<char, char> mp;
	for(int i = 0; i < 27; i++)
	{
		mp.insert(make_pair(googlerese[i], alphabet[i]));
	}

	for(int i = 0; i < T; i++)
	{		
		gets(buf);
		char *c = buf;
		printf("Case #%d: ", i + 1);
		while(*c)
		{
			printf("%c", mp[*c++]);
		}
		printf("\n");
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}