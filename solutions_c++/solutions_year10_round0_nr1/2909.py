#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <iostream>
using namespace std;

int main(){

	int T;
	long long n, k;
	//freopen("A-small.in","r",stdin); freopen("A-small.out", "w", stdout);
	freopen("A-large.in","r",stdin); freopen("A-large.out", "w", stdout);

	scanf("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		scanf("%lld %lld", &n, &k);
		long long p = (1LL << n);

		printf("Case #%d: ", i);
		if ((k % p) == p - 1)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	
	return 0;
}