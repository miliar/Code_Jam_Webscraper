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

#define MR 10010

pair < int, int > t[MR];
int dp[MR];	//max zasieg z danego pola

int main()
{
	int T;
	scanf("%d", &T);
	REP(c,T)
	{
		int N, D;
		scanf("%d", &N);
		REP(i,N) scanf("%d%d", &t[i].ST, &t[i].ND);
		scanf("%d", &D);		
		memset(dp,-1,sizeof(dp));
		dp[0] = t[0].ST;
		REP(i,N)
		{
			if(dp[i] == -1) continue;
			FOR(j,i+1,N)
			{
				if(t[j].ST > t[i].ST + dp[i]) break;
				dp[j] = max(dp[j], min(t[j].ND, t[j].ST-t[i].ST));
			}
		}
		bool ok = 0;
		REP(i,N)
			if(t[i].ST + dp[i] >= D)
			{
				ok = 1;
				break;
			}
		printf("Case #%d: ", c+1);
		if(ok) printf("YES\n"); else printf("NO\n");
	}
	return 0;
}