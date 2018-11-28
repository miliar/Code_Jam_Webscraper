#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#define MAX_LONG_LONG 9223372036854775807
#define MAX_INT  2147483647
#define MAX_LONG 2147483647
using namespace std;


int main() {
	unsigned long x[31];
	memset(x, 0, sizeof(x));
	x[0] = 2;
	for(int i = 1; i <= 30; i ++)
	{
		x[i] = x[i-1] * 2;
	//	printf("%lu ",x[i]);
	}	

	freopen("..//input.txt", "rt", stdin);
	freopen("..//output.txt", "wt", stdout);
	int tc; 
	scanf("%d", &tc);
	for(int t = 1; t <= tc; t ++)
	{
		unsigned long N, K;
		scanf("%d %d", &N, &K);
		unsigned num = x[N - 1] - 1;
		if((num & K) == num )
			printf("Case #%d: ON\n", t);
		else
			printf("Case #%d: OFF\n", t);
	}

}