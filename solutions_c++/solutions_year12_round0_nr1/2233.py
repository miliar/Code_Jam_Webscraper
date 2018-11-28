#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <utility>

#define MG 101
#define MC 26

using namespace std;

char input[MG];
char dict[MC]={ 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u',
				'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w',
				'j', 'p', 'f', 'm', 'a', 'q' };

int main()
{
	int t, n;
	scanf("%d", &t);
	gets(input);
	for(int c=1; c<=t; c++)
	{
		gets(input);
		n=strlen(input);
		printf("Case #%d: ", c);
		for(int i=0; i<n; i++)
			if(islower(input[i]))
				putchar(dict[input[i]-'a']);
			else
				putchar(input[i]);
		puts("");
	}
	return 0;
}
