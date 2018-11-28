#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

typedef long long LL;

int ta, tb, now, T, tst, A, B;
int n;
char rob[110];
int x[110];

void work()
{
	cin>> n;
	ta = tb = now = 0;
	A = B = 1;
	for(int i = 0; i < n; ++i) {
		char rob; int x;
		cin>> rob>> x;
		if(rob == 'O') {
			ta += abs(A-x);
			A = x;
			if(ta < now) ta = now;
			ta++;
			now = ta;
		} else {
			tb += abs(B-x);
			B = x;
			if(tb < now) tb = now;
			tb++;
			now = tb;
		}
	}
	printf("%d\n", now);
}

int main()
{
	//freopen("a.in", "r", stdin);
	//freopen("a.out", "w", stdout);
	cin>> T;
	while(tst < T) {
		printf("Case #%d: ", ++tst);
		work();
	}
	return 0;
}
