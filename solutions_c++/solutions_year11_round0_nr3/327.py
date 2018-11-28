#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
#define PB push_back
#define MP make_pair

typedef long long LL;

int n, T, tst;
int c[1010], mi, sum;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	cin>> T;
	int tst=0;
	while(tst < T){
		printf("Case #%d: ", ++tst);
		cin>> n;
		int res = 0; mi = 1000000000;
		sum = 0;
		for(int i = 0; i < n; ++i) {
			int x; cin>> x;
			res ^= x;
			mi = min(mi, x);
			sum += x;
		}
		if(res != 0) puts("NO");
		else {
			printf("%d\n", sum-mi);
		}
	}
	
	return 0;
}
