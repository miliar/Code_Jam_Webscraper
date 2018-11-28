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


char buf[1024];

int seq[1024];
int main()
{
	int cases , Case = 1;
	scanf("%d" , &cases);
	
	while( cases-- )
	{
		printf("Case #%d: " , Case++);
		int n;
		scanf("%d" , &n);
		int totalX = 0;
		int total = 0;
		for(int i =0;i<n;i++)
		{
			scanf("%d" , seq+i);
			totalX ^= seq[i];
			total += seq[i];
		}
		if( totalX )
		{
			puts("NO");
		}
		else
		{
			sort( seq , seq+n);
			int now = 0;
			int ans = 0;
			for(int i = n-1; i > 0 ; i--)
			{
				now ^= seq[i];
				if( now == 0 ) break;
				ans += seq[i];
			}
			int left = total - ans;
			if( left > ans ) ans = left;
			
			printf("%d\n" , ans);
		}
	}







	return 0;
}