// Alien.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string.h>
#include <vector>
using namespace std;

const int MAXL = 20;

int L, D, N;
vector<string> words;
bool hash[MAXL][26];

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("d:/in.txt", "r", stdin);
	freopen("d:/out.txt", "w", stdout);
	scanf("%d%d%d", &L, &D, &N);
	char tmp[555]; gets(tmp);
	int i;
	words.clear();
	for (i = 0; i < D; i++)
	{
		gets(tmp);
		words.push_back(tmp);
	}

	int j, k;
	bool mk;
	for (i = 0; i < N; i++)
	{
		int count = 0;
		gets(tmp);
		int len = strlen(tmp);
		memset(hash, 0, sizeof(hash));
		k = 0;
		mk = 0;
		for (j = 0; j < len; j++)
		{
			if (tmp[j] == '(')
				mk = 1;
			if (tmp[j] == ')')
			{
				mk = 0;
				k++;
			}
			if (tmp[j] >= 'a' && tmp[j] <= 'z')
			{
				hash[k][tmp[j] - 'a'] = 1;
				if (!mk)
					k++;
			}
		}

		for (j = 0; j < D; j++)
		{
			mk = true;
			for (k = 0; k < L && mk; k++)
			{
				if (!hash[k][words[j][k] - 'a'])
					mk = false;
			}
			if (mk)
				count++;
		}

		printf("Case #%d: %d\n", i + 1, count);
	}

	return 0;
}

