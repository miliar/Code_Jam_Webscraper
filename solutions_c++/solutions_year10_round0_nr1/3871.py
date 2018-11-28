#include <cstdio>
using namespace std;

static void work()
{
	int N, K;
	scanf("%d%d", &N, &K);
	bool good = true;
	while(N--) {
		if(!(K & 1))
			good = false;
		K >>= 1;
	}
	static int cas = 0;
	printf("Case #%d: %s\n", ++cas, good ? "ON" : "OFF");
}

int main()
{
	int T;
	scanf("%d", &T);
	while(T--)
		work();
	return 0;
}
