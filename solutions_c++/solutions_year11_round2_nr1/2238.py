
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

char s[MR][MR];

pair < int, int > t[MR];

double wp[MR], owp[MR], oowp[MR];

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int c = 0; c < tests; c++)
	{
		printf("Case #%d:\n", c+1);
		int n;
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
			scanf("%s", s[i]);
		for(int i = 0; i < n; i++)
		{			
			t[i].first = t[i].second = 0;
			for(int j = 0; j < n; j++)
			{
				if(s[i][j] != '.')
					t[i].second++;
				if(s[i][j] == '1')
					t[i].first++;
			}			
		}
		for(int i = 0; i < n; i++)
		{
			wp[i] = t[i].first / (double) t[i].second;
			owp[i] = 0;			
			for(int j = 0; j < n; j++)
				if(s[i][j] != '.')
					owp[i] += (t[j].first-(s[i][j] == '0')) / (double) (t[j].second - 1);
			owp[i] = owp[i] / (double) t[i].second;	//dzielimy srednie przez liczbe oponentow
		}
		for(int i = 0; i < n; i++)
		{
			oowp[i] = 0;
			for(int j = 0; j < n; j++)
				if(s[i][j] != '.')
					oowp[i] += owp[j];
			oowp[i] = oowp[i] / (double) t[i].second;
		}
		for(int i = 0; i < n; i++)
			printf("%.10lf\n", 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);
	}
	return 0;
}