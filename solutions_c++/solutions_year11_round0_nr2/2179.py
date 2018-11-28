
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

#define MR 200

char t[MR][MR], s[MR];
bool opposed[MR][MR];

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int c = 0; c < tests; c++)
	{
		memset(opposed, 0, sizeof(opposed));
		memset(t, 0, sizeof(t));
		int C, D, N;
		scanf("%d", &C);
		for(int i = 0; i < C; i++)
		{
			char str[4];
			scanf("%s", str);			
			t[str[0]][str[1]] = t[str[1]][str[0]] = str[2];
		}
		scanf("%d", &D);
		for(int i = 0; i < D; i++)
		{
			char str[3];
			scanf("%s", str);
			opposed[str[0]][str[1]] = opposed[str[1]][str[0]] = 1;
		}
		scanf("%d%s", &N, s);
		vector < char > v;
		for(int i = 0; i < N; i++)
		{
			v.PB(s[i]);
			while(v.size() > 1 && t[v.back()][v[v.size()-2]])
			{
				char a = v.back(), b = v[v.size()-2];
				v.pop_back();
				v.pop_back();
				v.PB(t[a][b]);
			}
			for(int i = 0; i < (int)v.size(); i++)
				if(opposed[v[i]][v.back()])
				{
					v.clear();
					break;
				}
		}
		printf("Case #%d: [", c+1);
		for(int i = 0; i < (int)v.size()-1; i++)
			printf("%c, ", v[i]);
		if(!v.empty())
			printf("%c", v.back());
		printf("]\n");
	}
	return 0;
}