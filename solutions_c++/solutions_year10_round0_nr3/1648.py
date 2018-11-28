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
/* C++ */
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <climits>
#include <ctime>
using namespace std;


int g[1024];
int main()
{
	int Case , cases = 1;
	int n , k , r;
	int i;
	long long ans , total;
	scanf("%d" , &Case);

	while( Case-- )
	{
		
		map< vector<int>,int > cycle;
		vector<long long> round;
		total = ans = 0;
		scanf("%d%d%d" , &r, &k,&n);
		for(i=0;i<n;i++)
		{
			scanf("%d" , &g[i]);
			total += g[i];
		}
		if( total <= k )
		{
			ans = total*(long long)r;
		}
		else
		{
			i = 0;
			int rd = 0;
			total = 0; //accumlate
			while( r )
			{
				vector<int> as;
				int t = k;
				int rt = 0;
				int previ = i;
				while( t >= g[i] )
				{
					t -= g[i];
					rt += g[i];
					as.push_back(i);
					i++; i%=n;
					if( i == previ ) break;
				}
				if( (t = cycle[ as ]) )
				{
					int cStart = t-1;
					int cEnd = rd;
					long long haha;
					if( cStart )
						haha = total - round[cStart-1];
					else
						haha = round[ cEnd-1];

					ans +=  ((long long)(r/( cEnd - cStart )) ) *( haha );

					if( r%( cEnd - cStart ) )
					{
						int middle = cStart + r%( cEnd - cStart ) -1;
						ans += round[middle] ;//- round[cStart];
						if( cStart ) ans -= round[cStart-1];
					}


					r = 0;
				}
				else
				{
					cycle[ as ] = ++rd;
					total += rt;
					round.push_back(total);
					

					ans += rt;

					r--;
				}

			}
			


		}

		

		printf("Case #%d: %lld\n" , cases++ ,  ans);

	}

	return 0;
}


//int g[1024];
//int main()
//{
//	int Case , cases = 1;
//	int n , k , r;
//	int i;
//	long long ans , total;
//	scanf("%d" , &Case);
//
//	while( Case-- )
//	{
//		total = ans = 0;
//		scanf("%d%d%d" , &r, &k,&n);
//		for(i=0;i<n;i++)
//		{
//			scanf("%d" , &g[i]);
//			total += g[i];
//		}
//
//		i = 0;
//		while( r )
//		{
//			int t = k;
//			int pi = i;
//			while( t >= g[i] )
//			{
//				t -= g[i];
//				ans +=g[i];
//
//				i++; i%=n;
//				if( i == pi ) break;
//			}
//
//
//			r--;
//		}
//
//		
//
//		printf("Case #%d: %lld\n" , cases++ ,  ans);
//
//	}
//
//	return 0;
//}
