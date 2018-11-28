#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

using namespace std;


int main()
{
	freopen("output.txt", "w", stdout);
	char s[100];
	int T;
	scanf("%d", &T);
	int mas[256];
	for (int  t = 0; t < T; t++)
	{
		scanf("%s", s);
		for (int i = 0; i < 256; i++)
			mas[i] = -1;
		int base = 2;
		int index = 0;
		mas[s[index]] = 1;
		index++;		
		while (s[index] && mas[s[index]] != -1)
			index++;
		if (s[index])
		{
			mas[s[index]] = 0;
			index++;
		}
		while (s[index] && mas[s[index]] != -1)
			index++;
		while (s[index])
		{
			if (mas[s[index]] == -1)
			{
				mas[s[index]] = base;
				base++;
			}
			index++;
		}
		long long res = 0;
		for (int i = 0; s[i]; i++)
		{
			res = res * base + mas[s[i]];
		}
		printf("Case #%d: %lld\n", t + 1, res);

	}
	fclose(stdout);
	return 0;
}