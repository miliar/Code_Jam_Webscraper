#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <deque>
#include <map>

using namespace std;

void solve()
{
	int n;
	int total = 0;
	int test = 0;
	int min_one =  1234567890;
	scanf("%d",&n);

	for(int i = 0; i < n; ++i) {
		int m;
		scanf("%d",&m);
		test = test ^ m;
		total += m;
		if(min_one > m) min_one = m;
	}
	if(test) printf("NO\n");
	else {
		printf("%d\n",total - min_one);
	}
}

int main(int argc, char *argv[])
{
	int kase;
	scanf("%d",&kase);
	for(int i = 1; i <= kase; ++i) {
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
