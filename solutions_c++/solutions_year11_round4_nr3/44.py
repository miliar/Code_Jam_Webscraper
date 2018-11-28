#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;


int TRIALS;

bool comp[1000001] = {0};

void trial(int T)
{
	printf("Case #%d: ", T);
	long long N;
	int ans = 1;
	scanf("%lld", &N);
	if (N == 1) {printf("0\n"); return;}
	for (long long i = 2; i*i <= N; i++)
	{
		if (comp[i]) continue;
		ans += (int)floor(log((double)N + 0.5) / log(i)) - 1;
	}
	printf("%d\n", ans);
}

int main(int argc, char* argv[])
{
	for (int i = 2; i <= 1000000; i++)
	{
		if (comp[i]) continue;
		for (int j = i*2; j <= 1000000; j += i)
			comp[j] = true;
	}
	scanf("%d", &TRIALS);
	for (int T = 1; T <= TRIALS; T++)
	{
		trial(T);
	}
	
	return 0;
}