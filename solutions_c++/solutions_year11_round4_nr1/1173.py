
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

#define MR 1010
#define EPS 0.000000000000000001

struct walkway
{
	int B, E, w;
}tab[MR];

int pom[MR];	//na ktorych walkway bedziemy biec

bool cmp1(int x, int y)
{
	return tab[x].w < tab[y].w;
}

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int c = 0; c < tests; c++)
	{
		printf("Case #%d: ", c+1);
		int X, S, R, t, N;
		scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
		int sum = 0;	//ile w sumie pokonamy na walkways
		for(int i = 0; i < N; i++)
		{
			scanf("%d%d%d", &tab[i].B, &tab[i].E, &tab[i].w);
			sum += tab[i].E-tab[i].B;
		}		
		for(int i = 0; i <= N; i++)
			pom[i] = i;
		tab[N].E = (X-sum);	//wartownik -> pokonujemy, to czego nie przebiegniemy po walkways
		tab[N].B = 0;
		tab[N].w = 0;
		sort(pom, pom+N+1, cmp1);		
		double left = t;	//tyle czasu mozemy biegac
		double res = 0;		//tyle czasu bedziemy sie poruszac
		for(int i = 0; i <= N; i++)	//musimy wszystko przebiec
		{
			if(left + EPS >= (tab[pom[i]].E-tab[pom[i]].B)/(double)(tab[pom[i]].w+R))	//zdazymy przebiec po tym korytarzu
			{
				left -= (tab[pom[i]].E-tab[pom[i]].B)/(double)(tab[pom[i]].w+R);
				res += (tab[pom[i]].E-tab[pom[i]].B)/(double)(tab[pom[i]].w+R);
			}
			else	//biegnij ile sie da, reszte idz
			{
				res += left;
				double leftS = (tab[pom[i]].E-tab[pom[i]].B)-left*(tab[pom[i]].w+R);	//tyle drogi zostalo do pokonania na piechote
				res += leftS/(double)(tab[pom[i]].w+S);
				left = 0;
			}
		}
		printf("%.10lf\n", res);
	}
	return 0;
}