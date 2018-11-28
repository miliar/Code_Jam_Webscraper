#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <deque>
#include <utility>
#include <algorithm>
#include <functional>

using namespace std;

//#define TAB_SIZ 31622777
//#define SEQ_SIZ 1951959	/* check stop if TAB_SIZ change */

/*
inline bool dbeq(const double a, const double b)
{
	return fabs(a-b) < 1e-7;
}
*/

int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	for(int ts=1;ts<=T;ts++){
		int n, pd, pg;
		scanf("%d%d%d", &n, &pd, &pg);
		if( pd == 0 && pg <= 99 )
			printf("Case #%d: Possible\n", ts);
		else if( pd == 0 && pg == 100 )
			printf("Case #%d: Broken\n", ts);
		else if( pd != 0 && pg == 0 )
			printf("Case #%d: Broken\n", ts);
		else{
			int valid = pd;
			int cnt = 1;
			while(valid % 100 != 0){
				valid += pd;
				++cnt;
			}
			if(n<cnt)
				printf("Case #%d: Broken\n", ts);
			else if( pd!=100 && pg==100 )
				printf("Case #%d: Broken\n", ts);
			else
				printf("Case #%d: Possible\n", ts);
		}
	}
	return 0;
}

