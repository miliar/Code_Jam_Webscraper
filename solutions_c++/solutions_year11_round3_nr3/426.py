
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

#define MR 110

int t[MR];

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int c = 0; c < tests; c++)
	{
		printf("Case #%d: ", c+1);
		int N, L, H;
		scanf("%d%d%d", &N, &L, &H);
		for(int i = 0; i < N; i++)
			scanf("%d", &t[i]);
		bool ok1 = 0;
		for(int i = L; i <= H; i++)
		{
			bool ok = 1;
			for(int j = 0; j < N; j++)
				if(!(i % t[j] == 0 || t[j] % i == 0))
				{
					ok = 0;
					break;
				}
			if(ok)
			{
				ok1 = 1;
				printf("%d\n", i);
				break;
			}
		}
		if(!ok1)
			printf("NO\n");
	}
	return 0;
}