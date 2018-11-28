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

int main()
{
	int Case , cases = 1;
	int n , k;
	scanf("%d" , &Case);

	while( Case-- )
	{
		char flag = 0;
		scanf("%d%d" , &n,&k);

		flag =  ( k & ((1<<n)-1) ) == ((1<<n)-1);

		printf("Case #%d: %s\n" , cases++ ,  flag?"ON" :"OFF");

	}

	return 0;
}