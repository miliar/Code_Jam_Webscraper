#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <cassert>
#include <map>
#include <string.h>
#include <ctime>
#include <iostream>

using namespace std;

const char* FILE_NAME_IN = "input.txt";
const char* FILE_NAME_OUT = "output.txt";

const int size = 1000 + 5;
const int inf = 1000 * 1000 * 1000 + 5;
double const eps = 1e-8;

char magic[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
char s[200];

int main ()
{
	freopen(FILE_NAME_IN, "r", stdin);
	freopen(FILE_NAME_OUT, "w", stdout);

	int i, it, t;

	scanf("%d\n", &t);
	
	for (it = 1; it <= t; it++)
	{
		printf("Case #%d: ", it);
		fgets(s, 150, stdin);
		for (i = 0; i < strlen(s); i++)
			printf("%c", magic[s[i] - 'a']);
		printf("\n");
	}
	
	return 0;
}