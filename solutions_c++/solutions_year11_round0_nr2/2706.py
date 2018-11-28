// Magic.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <cstdio>
#include <cstring>
#include <cassert>

using namespace std;

const int NumBase = 8;
const int NumLetter = 26;
const int MaxLen = 1000;
void PrintList(int lst[], int n);
int GetIndex(char c);

int _tmain(int argc, _TCHAR* argv[])
{
	vector<char> list;
	vector<char> list2;
	
	int T, C, D, N;
	char str[1000];

	scanf("%d", &T);
	
	for (int t = 1; t <= T; t++)
	{
		int combine[26][26];
		int oppose[28][2];

		memset(combine, 255, sizeof(combine));
		memset(oppose, 0, sizeof(oppose));
		
		printf("Case #%d: ", t);

		scanf("%d", &C);

		for (int i = 0; i < C; i++)
		{
			scanf("%s", str);
			assert(strlen(str) == 3);
			int a = str[0] - 'A';
			int b = str[1] - 'A';
			int r = str[2] - 'A';

			combine[a][b] = r;
			combine[b][a] = r;
		}

		scanf ("%d", &D);

		for (int i = 0; i < D; i++)
		{
			scanf("%s", str);
			assert(strlen(str) == 2);

			int a = str[0] - 'A';
			int b = str[1] - 'A';

			oppose[i][0] = a;
			oppose[i][1] = b;
		}

		scanf ("%d", &N);
		scanf("%s", str);
		assert(N == strlen(str));

		int lst[1000];
		int idx = 0;
		memset(lst, 0, sizeof(lst));

		int count[26];
		memset(count, 0, sizeof(count));

		for (int i = 0; i < N; i++)
		{
			int c = str[i] - 'A';

			count[c]++;
			lst[idx++] = c;
			
			if (idx == 1)
			{
//				printf("- %d ", i);
//				PrintList(lst, idx);
				continue;
			}

			int a = lst[idx-2];
			int b = lst[idx-1];

			if (combine[a][b] != -1)
			{
				count[a]--;
				count[b]--;
				lst[idx-2] = combine[a][b];
				idx--;
//				printf("C %d ", i);
//				PrintList(lst, idx);
				continue;
			}
			
			// check for opposing elements
			for (int j = 0; j < D; j++)
			{
				if ((count[oppose[j][0]] != 0) &&
					(count[oppose[j][1]] != 0))
				{
					idx = 0;
					memset(count, 0, sizeof(count));
				//printf("C %d ", i);
				//PrintList(lst, idx);
				}
			}
		}

		PrintList(lst, idx);
	}

	return 0;
}

void PrintList(int lst[], int n)
{
	printf("[");

	for (int i = 0; i < n; )
	{
	    putchar(lst[i] + 'A');
		i++;
		if (i != n)
			printf(", ");
	}
	printf("]\n");
}
