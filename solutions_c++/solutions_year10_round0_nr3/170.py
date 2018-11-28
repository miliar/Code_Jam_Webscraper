//cykl bedzie po maksymalnie n^2 kursach, zatem algorytm dziala w czasie O(n^2)
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

#define MR 1010
int n, r, k, t[MR], akt, wsk, ile, beg, end, ilepocz, beg1, end1;
LL pom, sum, res0, res1, sumpocz;
bool done[MR][MR];	//ktore przedzialy juz byly

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for(int c = 0; c < tests; c++)
	{
		scanf("%d%d%d", &r, &k, &n);
		for(int i = 0; i < n; i++)
			scanf("%d", &t[i]);
		//spr czy wszyscy nie zmieszcza sie do jednego przejazdu
		pom = 0;
		for(int i = 0; i < n; i++)
			pom += t[i];
		if(pom <= k)
		{
			printf("Case #%d: %lld\n", c+1, r*pom);
			continue;
		}
		//wylicz liczbe przejazdow, po ktorej zakonczy sie na ostatniej grupie - potem bedzie tak samo
		sum = 0;	//ile, za taka liczbe przejazdow wezmie
		wsk = 0; ile = 0; akt = 0; beg = wsk;
		while(true)
		{
			
			if(t[wsk] + akt <= k)
			{
				akt += t[wsk];
				sum += t[wsk];
				end = wsk;
				wsk = (wsk+1)%n;
			}
			else
			{				
				if(done[beg][end])	//taka grupa juz jechala
				{
					sum -= akt;		//tej grupy nie liczymy 2 razy
					break;
				}
				else
					done[beg][end] = 1;
				ile++;	//zakonczyl kolejny kurs
				akt = 0;	//kurs jest znow pusty
				beg = wsk;	//nowa grupa				
			}
		}
		//od tej sumy odejmij poczatek, ktory nie musi nalezec do cyklu
		sumpocz = 0;	//ile, za taka liczbe przejazdow wezmie
		wsk = 0; ilepocz = 0; akt = 0; beg1 = wsk;
		while(true)
		{
			
			if(t[wsk] + akt <= k)
			{
				akt += t[wsk];
				sumpocz += t[wsk];
				end1 = wsk;
				wsk = (wsk+1)%n;
			}
			else
			{				
				if(beg1 == beg && end1 == end)	//trafilismy na poczatek cyklu
				{
					sumpocz -= akt;
					break;
				}				
				ilepocz++;	//zakonczyl kolejny kurs
				akt = 0;	//kurs jest znow pusty
				beg1 = wsk;	//nowa grupa				
			}
		}
		res1 = 0;
		if(r <= ilepocz)
		{
			wsk = 0; akt = 0;
			for(int i = 0; i < r;)
			{
				if(t[wsk] + akt <= k)
				{
					res1 += t[wsk];
					akt += t[wsk];
					wsk = (wsk+1) % n;
				}
				else
				{
					i++;	//kolejny kurs
					akt = 0;
				}
			}//wykonuj kursy poczatkowe
			printf("Case #%d: %lld\n", c+1, res1);
			for(int i = 0; i < n; i++)
				for(int j = 0; j < n; j++)
					done[i][j] = 0;
			continue;
		}
		r -= ilepocz;	//nie liczymy kursow, ktore zrobilismy, zeby dojsc do cyklu
		sum -= sumpocz;	//odejmij sume poczatkowa
		ile -= ilepocz;
		res0 = sumpocz + (r/ile)*sum;
		//wykonalismy r/ile takich cykli, teraz zostalo cos na koniec
		wsk = beg;	//od tej pozycji zaczynaj dodawanie ludzi
		r %= ile;
		akt = 0;
		for(int i = 0; i < r;)
		{
			if(t[wsk] + akt <= k)
			{
				res1 += t[wsk];
				akt += t[wsk];
				wsk = (wsk+1) % n;
			}
			else
			{
				i++;	//kolejny kurs
				akt = 0;
			}
		}//wykonuj kursy, ktore zostaly
		printf("Case #%d: %lld\n", c+1, res0+res1);
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
				done[i][j] = 0;
	}
	return 0;
}