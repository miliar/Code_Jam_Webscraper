#include <iostream>
#include <vector>
#include <map>
using namespace std;

int caseID;

void deal()
{
	long long capacity;
	long long run;
	long long groups;

	scanf("%lld%lld%lld", &run, &capacity, &groups);
	vector<long long> gi(groups);
	for (int i = 0; i < groups; ++i)
		scanf("%lld", &gi[i]);

	long long total = 0;
	for (int i = 0; i < groups; ++i)
		total += gi[i];
	if (total <= capacity)
	{
		printf("Case #%d: %lld\n", caseID, total * run);
		return;
	}

	map<long long, long long> posiApp;
	vector<long long> sum(2000);
	long long ans = 0;

	sum[0] = 0;
	posiApp[0] = 0;


	int nextPosi = 0;
	for (long long i = 1; i <= run; ++i)
	{
		long long now = 0;
		long long remain = capacity;
		bool cycle = false;
		while (remain >= gi[nextPosi])
		{
			remain -= gi[nextPosi];
			now += gi[nextPosi];
			nextPosi++;
			if (nextPosi == groups)
			{
				cycle = true;
				nextPosi = 0;
			}
		}

		sum[i] = sum[i - 1] + now;
		if (cycle)
		{
			if (posiApp.find(nextPosi) != posiApp.end())
			{
				int lastRun = posiApp[nextPosi];
				int period = i - lastRun;
				long long periodSum = sum[i] - sum[lastRun];
				long long remainRun = run - i;
				long long remainPeriod = remainRun / period;
				remainRun = remainRun % period;
				ans = sum[i] + remainPeriod * periodSum;
				ans += sum[lastRun + remainRun] - sum[lastRun];
				printf("Case #%d: %lld\n", caseID, ans);
				return;
			}
			else
				posiApp[nextPosi] = i;
		}
	}
	printf("Case #%d: %lld\n", caseID, sum[run]);

}

int main()
{
	int T;
	scanf("%d", &T);
	for (caseID = 1; caseID <= T; ++caseID)
		deal();
	return 0;
}
