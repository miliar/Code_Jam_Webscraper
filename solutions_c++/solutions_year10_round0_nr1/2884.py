
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	long long T, N, K;
	scanf("%lld", &T);
	for(long long c = 1 ; c <= T ; c++)
	{
		scanf("%lld %lld", &N, &K);
		long long req = 0;
		for(long long i = 0 ; i < N ; i++)
		{
			req += powl(2, i);
		}
		
		bool ON;
		if(K < req)
			ON = false;
		else if(K == req)
			ON = true;
		else
		{
			long long diff = K - req;
			req++;
			if(diff % req == 0)
				ON = true;
			else
				ON = false;
		}

		if(ON)
			printf("Case #%lld: ON\n", c);
		else
			printf("Case #%lld: OFF\n", c);
	}
	return 0;
}