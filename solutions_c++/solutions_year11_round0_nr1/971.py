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



char buf[10];
int main()
{
	int cases , Case = 1;
	scanf("%d" , &cases);
	
	while( cases-- )
	{
		printf("Case #%d: " , Case++);

		int n; 
		scanf("%d" , &n);
		int st;
		int snycMove = 0;
		int ans = 0;
		int curPos[2];
		curPos[0] = curPos[1] = 1;
		char prev = 'f';
		while(n--)
		{
			scanf("%s %d" , buf , &st);
			int curIdx = buf[0] == 'O'? 0 : 1;

			int diff = abs(st-curPos[curIdx]) ;
			if( prev != buf[0] )
			{
				int extra = diff - snycMove ;
				if( extra >= 0 )
				{
					ans += extra;
					snycMove = extra+1;
				}
				else
					snycMove = 1;
				
			}
			else
			{
				ans += diff;
				snycMove += diff+1;
			}
			prev = buf[0];
			ans++;
			curPos[curIdx] = st;
			
		}

		printf("%d\n" , ans);
	}







	return 0;
}