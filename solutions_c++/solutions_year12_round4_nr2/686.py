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

#define FOR(i,b,e) for(int i=(b);i<(e);++i)
#define FORQ(i,b,e) for(int i=(b);i<=(e);++i)
#define FORD(i,b,e) for(int i=(b)-1;i>=(e);--i)
#define REP(x, n) for(int x = 0; x < (n); ++x)

#define ST first
#define ND second
#define PB push_back
#define MP make_pair
#define LL long long
#define ULL unsigned LL
#define LD long double

const double pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342;

#define MR 1010

int t[MR], wsk[MR];

pair < int, int > res[MR], pr[MR];

LL sqr(LL x) { return x*x; }

bool done[MR];

bool go(int N, int W, int L)
{
		bool found = 0;
		sort(t,t+N);		
		do{			
			bool ok = 1;
			res[0] = MP(0,0);
			int akt = t[0];	//wysokosc
			int start = 0;
			FOR(i,1,N)
			{
				if(akt + t[i] > L)	//wystaje poza obszar
				{
					res[i].ND = 0;
					res[i].ST = res[start].ST+t[start]+t[i];
					akt = 0;					
					FOR(j,start,i) if(sqr(res[i].ST-res[j].ST)+sqr(res[j].ND) < sqr(t[j]+t[i]))
						res[i].ST = res[j].ST+t[j]+t[i];													
					if(res[i].ST > W)	//wystaje poza obszar
					{
						ok = 0;
						break;
					}
					start = i;	//to bedzie pierwszy element na poczatek - do sprawdzania kolejnej kolumny
				}
				else
				{
					akt += t[i];
					res[i].ND = akt;
					akt += t[i];	//dotad jest zabroniona wysokosc
					//znajdz szerokosc
					res[i].ST = res[start].ST+t[start]+t[i];
					FOR(j,start,i) if(sqr(res[i].ST-res[j].ST)+sqr(res[j].ND) < sqr(t[j]+t[i]))
						res[i].ST = res[j].ST+t[j]+t[i];
					if(res[i].ST > W)	//wystaje poza obszar
					{
						ok = 0;
						break;
					}
				}
			}
			if(ok)	//spr
			{
				REP(i,N)FOR(j,i+1,N)
					if(sqr(res[i].ST-res[j].ST)+sqr(res[i].ND-res[j].ND) < sqr(t[i]+t[j]))
						ok = 0;
			}
			if(ok) { found = 1; break; }
		}while(next_permutation(t,t+N));
		return found;
}//go

int main()
{
	int T;
	scanf("%d", &T);
	REP(c,T)
	{
		int N, W, L;
		scanf("%d%d%d", &N, &W, &L);
		REP(i,N) scanf("%d", &t[i]);
		REP(i,N) wsk[i] = t[i];
		if(!go(N,W,L))
		{
			if(!go(N,L,W)){ printf("ERROR\n"); return 0; }
			REP(i,N) swap(res[i].ST,res[i].ND);
		}		
		printf("Case #%d:", c+1);
		memset(done,0,sizeof(done));
		REP(i,N)REP(j,N) if(t[i] == wsk[j] && !done[j])
		{			
			done[j] = 1;
			pr[j] = res[i];
			break;
		}
		REP(i,N) printf(" %d %d", pr[i].ST, pr[i].ND); printf("\n");
	}
	return 0;
}