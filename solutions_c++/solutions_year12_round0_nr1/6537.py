#include <stdio.h>
#include <map>
#include <string.h>

using namespace std;

char source[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
char target[] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	map<char,char> m;
	
	for (int i = 0 ; i < strlen(source); i++)
	{
		m[source[i]] = target[i];
		m[source[i] - 'a' + 'A'] = target[i] - 'a' + 'A';
	}
	m['q'] = 'z';
	m['z'] = 'q';
	int n;
	scanf("%d\n",&n);
	int t = 0;
	while (t++ < n)
	{
		printf("Case #%d: ",t);
		char *s = new char[300];
		gets(s);
		for (int i = 0 ; i < strlen(s); i++)
		{		
			printf("%c",m[s[i]]);
		}
		printf("\n");
	}
	return 0;
}
