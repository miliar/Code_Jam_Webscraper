
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <string>
#include <queue>
#include <bitset>		//UWAGA - w czasie kompilacji musi byc znany rozmiar wektora - nie mozna go zmienic
#include <cassert>
#include <iomanip>		//do setprecision
#include <ctime>
#include <complex>
using namespace std;
#define PB push_back
#define LL long long
#define ULL unsigned LL
#define LD long double

#define MR 100

char s[MR][MR];

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int c = 0; c < tests; c++)
	{
		printf("Case #%d: \n", c+1);
		int R, C;
		scanf("%d%d", &R, &C);
		for(int i = 0; i < R; i++)
			scanf("%s", s[i]);
		for(int i = 0; i < R-1; i++)
			for(int j = 0; j < C-1; j++)
				if(s[i][j] == '#' && s[i][j+1] == '#' && s[i+1][j] == '#' && s[i+1][j+1] == '#')
				{
					s[i][j] = '/';
					s[i][j+1] = 92;
					s[i+1][j] = 92;
					s[i+1][j+1] = '/';
				}
		bool ok = 1;
		for(int i = 0; i < R; i++)
			for(int j = 0; j < C; j++)
				if(s[i][j] == '#')
					ok = 0;
		if(ok)
			for(int i = 0; i < R; i++)
				printf("%s\n", s[i]);
		else
			printf("Impossible\n");
	}
	return 0;
}