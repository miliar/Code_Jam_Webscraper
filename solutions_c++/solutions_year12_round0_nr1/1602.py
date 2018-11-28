#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <functional>
using namespace std;

#pragma comment(linker,"/STACK:100000000")

char t[] = "yhesocvxduiglbkrztnwjpfmaq";
char s[150];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int n;
	int i, j;
	scanf("%d\n", &n);
	for (i = 0; i < n; ++i)
	{
		gets(s);
		int l = strlen(s);
		printf("Case #%d: ", i + 1);
		for (j = 0; j < l; ++j)
			if (s[j] != ' ')
				printf("%c", t[s[j] - 'a']);
			else
				printf(" ");
		printf("\n");
	}
	return 0;
}