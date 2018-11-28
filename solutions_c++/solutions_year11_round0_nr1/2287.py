
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


int main()
{
	int tests;
	scanf("%d", &tests);
	for(int c = 0; c < tests; c++)
	{
		int n, prevO = 1, prevB = 1, prevTB = 0, prevTO = 0;
		int res = 0;	//ile czasu minelo
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
		{
			char s[2];
			int pos;
			scanf("%s%d", s, &pos);
			if(s[0] == 'B')
			{				
				prevTB += abs(prevB-pos)+1;
				prevB = pos;
				if(prevTB <= res)
					prevTB = res+1;
				res = max(res, prevTB);
			}
			else
			{
				prevTO += abs(prevO-pos)+1;
				prevO = pos;
				if(prevTO <= res)
					prevTO = res+1;
				res = max(res, prevTO);
			}
		}
		printf("Case #%d: %d\n", c+1, res);
	}
	return 0;
}