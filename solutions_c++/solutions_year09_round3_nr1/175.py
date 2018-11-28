//============================================================================
// Name        : gcj-1.cpp
// Author      : Thomas 'nickers' Wsuł
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <map>
#include <string>
#include <string.h>
#include <vector>
#include <set>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

unsigned long long getDigits(char *T, unsigned char *v)
{
	int cnt = 2, p = 0;

	memset(v, 255, 255 * sizeof(v[0]));

	v[T[0]] = 1;
	while (T[0]==T[p]) p++;
	v[T[p]] = 0;

	while (T[p] != 0)
	{
		if (v[T[p]] == 255)
		{
			v[T[p]] = cnt;
			cnt++;
		}
		p++;
	}

	return cnt;
}

int main()
{
	int N;
	char T[100];
	unsigned char vals[255];
	long long result = 0;
	scanf("%d", &N);

	for (int i = 1; i <= N; i++)
	{
		scanf("%s", T);
		unsigned long long base = getDigits(T, vals);
		if (base == 1) base = 2;
		int p = 0;
		result = 0;
		while (T[p]!=0) {
			result = result * base + (unsigned long long)vals[T[p]];
			p++;
		}

		printf("Case #%d: %lld\n", i, result);
	}

	return 0;
}
