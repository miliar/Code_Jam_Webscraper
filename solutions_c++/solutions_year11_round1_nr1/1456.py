#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <stack>
using namespace std;

long long  GCD(long long x,long long y)
{
	return y == 0 ? x : GCD ( y, x%y );
}

int main()
{
	freopen("A-small-attempt3.in","rt",stdin);
	freopen("A-small-attempt3.out","wt",stdout);
	int tt;
	scanf("%d",&tt);
	for ( int t = 1; t<=tt ; t++)
	{
		long long N,Pd,Pg,h = 100LL;
		cin >> N >> Pd >> Pg;
		long long gcd = GCD(Pd,h);
		Pd /= gcd;
		h /= gcd;
		//Pg /= GCD(Pg,100LL);

		bool f = 1;
		if ( h > N)
			f = 0;
		if ( (100LL - Pg) < (h-Pd))
			f = 0;
		//if ((double)Pd / (double) h > (double) Pg / 100.0)
		//	f = 0;

		if ( Pd > Pg)
			f = 0;
		printf("Case #%d: ",t);
		if ( f )
			printf("Possible\n");
		else
			printf ("Broken\n");
	}
	return 0;
}
