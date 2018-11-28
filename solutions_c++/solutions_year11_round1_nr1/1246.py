
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

int n, pd, pg;

bool check(int x)
{		
	for(int i = 1; i <= min(n, x); i++)
		for(int j = 0; j <= i; j++)
			if(j*100/i == pd && !((j*100) % i))
				for(int k = j; k <= x; k++)
					if(k*100/x == pg && !((k*100) % x) && k-j <= x-i)
						return 1;
	return 0;
}//check

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int c = 0; c < tests; c++)
	{
		printf("Case #%d: ", c+1);		
		scanf("%d%d%d", &n, &pd, &pg);		
		bool ok = 0;
		for(int i = 1; i < 20001; i++)
			if(check(i))
			{
				printf("Possible\n");		
				ok = 1;
				break;
			}
		if(!ok)
			printf("Broken\n");
	}
	return 0;
}