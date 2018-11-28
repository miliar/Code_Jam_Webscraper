#include<iostream>
using namespace std;

int caseID;

void deal(long long N, long long K)
{
	long long period = (1 << N);
	if ((K + 1) % period == 0)
		printf("Case #%d: ON\n", caseID);
	else
		printf("Case #%d: OFF\n", caseID);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (caseID = 1; caseID <= T; ++caseID)
	{
		long long N, K;
		scanf("%lld%lld", &N, &K);
		deal(N, K);
	}
	return 0;
}
