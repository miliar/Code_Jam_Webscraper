
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
		int N;
		scanf("%d", &N);
		int val = 0;
		for(int i = 0; i < N; i++)
		{
			scanf("%d", &t[i]);
			val ^= t[i];
		}
		if(val)
		{
			printf("NO\n");
			continue;
		}
		sort(t, t+N);
		int sum = 0;
		for(int i = 1; i < N; i++)
			sum += t[i];
		printf("%d\n", sum);
	}
	return 0;
}