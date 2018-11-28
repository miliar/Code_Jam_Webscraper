#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

#define FOR(i, n) for( int i = 0; i < (int)(n); i++)

//					{ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };
char dict[26] =		{ 'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q' };
char revdict[26] =	{ 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };

void tongues()
{
	int testCaseNum = 0;

	FILE* input = fopen("..\\..\\Input\\A-small-attempt0.in", "rt");
	FILE* output = fopen("..\\..\\Output\\A-small-attempt0.out", "wt");	

	fseek(input, 0, SEEK_END); // seek to end of file
	int size = ftell(input); // get current file pointer
	fseek(input, 0, SEEK_SET); // seek back to beginning of file

	fscanf(input, "%d\r\n", &testCaseNum);

	for (int i = 1; i <= testCaseNum; i++)
	{
		char c = '\0';
		char out[101] = { '\0' };

		int temp = ftell(input) ;
		
		for (int j = 0; j < 101 && temp < size-1; j++)
		{
			temp = ftell(input);
			fscanf(input, "%c", &c);

			if (c == 10)
			{
				break;
			}
			else if (c == ' ')
			{
				out[j] = c;
			}
			else
			{
				out[j] = revdict[c - 'a'];
			}
		}

		fprintf(output, "Case #%d: %s\r\n", i, out);
	}
}