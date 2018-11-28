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
#include <algorithm>
#include <functional>

using namespace std;

typedef long long int int64_t;
typedef long long unsigned int uint64_t;

long long int best;
long long int real, cala, calb;
long long int n, bag[15], sum;

void solve(int now)
{
	if(now == n){
		if(cala == calb && real != 0 && real != sum){
			//printf("cand: %d %d\n", real, sum-real);
			best = max(best, max(real, sum-real));
		}
		return ;
	}
	calb ^= bag[now];
	solve(now+1);
	calb ^= bag[now];

	cala ^= bag[now];
	real += bag[now];
	solve(now+1);
	real -= bag[now];
	cala ^= bag[now];
}

int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	for(int ts=1;ts<=T;ts++){
		scanf("%lld", &n);
		sum = 0;
		for(int i=0;i<n;i++){
			scanf("%lld", bag+i);
			sum += bag[i];
		}
		best = -1, real = 0, cala = 0, calb = 0;
		solve(0);
		printf("Case #%d: ", ts);
		if(best == -1)
			puts("NO");
		else
			printf("%lld\n", best);
	}
	return 0;
}

