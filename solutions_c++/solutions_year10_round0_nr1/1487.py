#include <stdio.h>
#include <vector>
#include <string.h>
#include <string>
using namespace std;

int main()
{
	// freopen("A-small-attempt0.in", "r", stdin);
	// freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large-out.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int test = 1; test <= T; ++test)
	{
		int N, K;
		scanf("%d %d", &N, &K);
		int req = 1 << N;
		printf("Case #%d: ", test);
		if((K + 1) % req == 0)
			printf("ON\n");
		else
			printf("OFF\n");
	}

	return 0;
}