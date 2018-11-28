#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
#define PB push_back
#define MP make_pair

typedef long long LL;
const int N = 1010;

double res;
int n, tst, T;

void work()
{
	scanf("%d", &n);
	res = n;
	for(int i = 1; i <= n; ++i) {
		int x;
		scanf("%d", &x);
		if(x == i) res-=1;
	}
	printf("%.6f\n", res);
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &T);
	while(tst<T) {
		printf("Case #%d: ", ++tst);
		work();
	}
	
	return 0;
}
