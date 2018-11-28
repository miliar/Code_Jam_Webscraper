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

#define MR 110

int t[MR];

int process(int v, int p, int &S)
{
	int sub = 0;
	REP(j,11)REP(k,11)REP(l,11)
	{
		if(max(j,max(k,l)) - min(j,min(k,l)) > 2) continue;
		if(j+k+l != v) continue;
		if(max(j,max(k,l)) - min(j,min(k,l)) < 2 && max(j,max(k,l)) >= p)
			return 1;
		if(max(j,max(k,l)) - min(j,min(k,l)) == 2 && max(j,max(k,l)) >= p)
			sub = 1;
	}
	if(sub && S)
	{
		S--;
		return 1;
	}
	return 0;
}//process

int main()
{
	int T;
	scanf("%d", &T);
	REP(c,T)
	{
		int N, S, p;
		scanf("%d%d%d", &N, &S, &p);
		int res = 0;
		REP(i,N) 
		{
			scanf("%d", &t[i]);
			res += process(t[i],p,S);
		}
		printf("Case #%d: %d\n", c+1, res);
	}
	return 0;
}