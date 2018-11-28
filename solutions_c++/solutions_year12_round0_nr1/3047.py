#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
using namespace std;

char mp[] = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("lowesy_A.out", "w", stdout);
	map <char, char> mapping;
	for (int i = 0; i < 26; i++)
		mapping['a' + i] = mp[i];
	mapping[' '] = ' ';
	int _, cases = 1;
	char str[1000];
	scanf("%d", &_);
	gets(str);
	while (_--)
	{
		gets(str);
		int L = strlen(str);
		printf("Case #%d: ", cases++);
		for (int i = 0; i < L; i++)
			printf("%c", mapping[str[i]]);
		puts("");
	}
	return 0;
}