//compiled in vc
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <complex>
// C++
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <climits>
#include <ctime>
using namespace std;

int gcd(int a, int b){ int t; while ( b > 0 ) { a %= b; t = a; a = b; b =t; } return a; }


int main()
{
	int cases , Case = 1;
	scanf("%d" , &cases);

	while( cases-- )
	{
		printf("Case #%d: " , Case++);
		long long n , pd , pg;

		scanf("%lld%lld%lld" , &n , &pd ,&pg);
		if( pg == 0 && pd)
		{
			puts("Broken");
			continue;
		}
		
		int dd = gcd(pd , 100);
		int gg = gcd(pg , 100);
		pd = pd/dd;
		pg = pg/gg;
		long long  smallestpdT = 100/dd ;
		long long smallestpdG = 100/gg ;

		if( pd > pg )
		{
			int need = ceil(double(pd)/pg);
			pg *= need;
			smallestpdG *=need;
		}
		

		if( smallestpdT > smallestpdG )
		{
			int need = ceil(double(smallestpdT)/smallestpdG);
			pg *= need;
			smallestpdG *=need;
		}
		if( smallestpdT - pd > smallestpdG - pg)
		{
			puts("Broken");
			continue;
		}

		if( smallestpdT  > n )
			{
			puts("Broken");
			continue;
		}

		puts("Possible");



	}

	return 0;
}