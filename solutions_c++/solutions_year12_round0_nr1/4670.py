#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

char a[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 
			'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't',
			'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

char s[1000];

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	scanf("%d\n", &t);

	for(int tt = 0; tt < t; tt++)
	{
		gets(s);
		printf("Case #%d: ", tt+1);
		for(int i = 0; s[i]; i++)
			if(s[i] != ' ')
				printf("%c", a[s[i] - 'a']);
			else
				printf(" ");
		printf("\n");
	}


	return 0;
}