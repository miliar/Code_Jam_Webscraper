
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

const double inf = 1000000000;
#define MR 1010

int d[MR], pref[MR];

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int c = 0; c < tests; c++)
	{
		printf("Case #%d: ", c+1);
		int L, N, C;
		LL t;
		scanf("%d%lld%d%d", &L, &t, &N, &C);
		for(int i = 0; i < C; i++)
			scanf("%d", &d[i]);
		for(int i = C; i < N; i++)
			d[i] = d[i%C];		
		for(int i = 1; i <= N; i++)
			pref[i] = pref[i-1] + d[i-1];		
		double res = inf;
		if(L == 2)
		for(int i = 0; i < N-1; i++)
			for(int j = i+1; j < N; j++)
			{
				double pom = 2*pref[i];
				if(2*pref[i] >= t)
					pom += d[i];
				else if(2*pref[i+1] > t)
					pom += (t-2*pref[i]) + (d[i]-(t-2*pref[i])/2.0);
				else
					pom += 2*d[i];

				pom += 2*(pref[j] - pref[i+1]);

				if(pom >= t)
					pom += d[j];
				else if(2*d[j]+pom > t)
					pom += (t-pom) + (d[j]-(t-pom)/2.0);
				else
					pom += 2*d[j];

				pom += 2*(pref[N] - pref[j+1]);
				res = min(res, pom);
			}
		else if(L == 1)
			for(int i = 0; i < N; i++)
			{
				double pom = 2*pref[i];
				if(2*pref[i] >= t)
					pom += d[i];
				else if(2*pref[i+1] > t)
					pom += (t-2*pref[i]) + (d[i]-(t-2*pref[i])/2.0);
				else
					pom += 2*d[i];

				pom += 2*(pref[N] - pref[i+1]);
				res = min(res, pom);
			}
		else
			res = 2*pref[N];
		printf("%d\n", (int)res);
	}
	return 0;
}