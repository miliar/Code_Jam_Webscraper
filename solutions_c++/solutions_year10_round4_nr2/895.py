#include <cstdio>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cstring>
#include <cmath>
#include <string>
#include <queue>
#include <cassert>
using namespace std;
#define PB push_back
#define LL long long
#define ULL unsigned LL
#define LD long double

#define MR 5000
int P, pot[20], M[MR], a, p[MR], pos[MR];
bool done[MR], h[MR];

int main()
{
	pot[0] = 1;
	for(int i = 1; i < 11; i++)
		pot[i] = 2*pot[i-1];

	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for(int c = 0; c < tests; c++)
	{
		int res = 0;
		scanf("%d", &P);
		for(int i = 0; i < pot[P]; i++)
			scanf("%d", &M[i]);
		for(int i = P; i; i--)
			for(int j = 0; j < pot[i-1]; j++)
				scanf("%d", &a);
		//wyznacz pozycje zespolow
		int l = 0;
		for(int i = 0; i < P; i++)		
			l += pot[i];
		for(int i = 0; i < pot[P]; i++)
			pos[i] = l + i + 1;
		for(int i = 0; i < pot[P]; i++)
		{
			//wybierz min
			int mn = MR, mnnr = -1;
			for(int j = 0; j < pot[P]; j++)
				if(!done[j] && M[j] < mn)
				{
					mn = M[j];
					mnnr = j;
				}
			done[mnnr] = 1;
			//idz od korzenia i zobacz ile juz jest meczow obejrzanych
			//kazdy zespol gra P meczow
			int wsk = pos[mnnr], o = 0, dl = 0;
			while(wsk > 1)
			{
				wsk /= 2;
				p[dl++] = wsk;
				if(h[wsk])o++;
			}
			int ile = P-o-M[mnnr];	//tyle musi obejrzec
			if(ile > 0)	//zacznij ogladac od korzenia
			{
				for(int j = dl; j; j--)
					if(!h[p[j-1]])
					{
						res++;
						ile--;
						h[p[j-1]] = 1;
						if(!ile)
							break;
					}
			}
		}
		for(int i = 0; i < MR; i++)
			h[i] = 0;
		for(int i = 0; i < pot[P]; i++)
			done[i] = 0;
		printf("Case #%d: %d\n", c+1, res);
	}
	return 0;
}