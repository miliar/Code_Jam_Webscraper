#include <iostream>

#define N 1010

using namespace std;

int num[N], rouRec[N];
int r, k, n;
long long sumRec[N];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int caseID = 1;
	while (caseID <= t)
	{
		printf("Case #%d: ", caseID++);
		memset(sumRec, 0, sizeof(sumRec));
		scanf("%d %d %d", &r, &k, &n);
		int i;
		for (i = 0; i < n; i++)
			scanf("%d", &num[i]);
		__int64 sum = 0;
		int curR = 0, curP = 0, curSum;
		do 
		{
			curSum = num[curP];
			i = (curP + 1) % n;
			while (i != curP && curSum + num[i] <= k)
			{
				curSum += num[i++];
				i %= n;
			}
			sum += (__int64) curSum;
			curR++;
			curP = i;
			if (sumRec[curP] == 0)
			{
				sumRec[curP] = sum;
				rouRec[curP] = curR;
			}
		} 
		while (curR != r && sumRec[curP] == sum);
		if (curR < r)
		{
			sum += (sum - sumRec[curP]) * ((r - curR) / (curR - rouRec[curP]));
			r = (r - curR) % (curR - rouRec[curP]);
			curR = 0;
			while (curR != r)
			{
				curSum = num[curP];
				i = (curP + 1) % n;
				while (i != curP && curSum + num[i] <= k)
				{
					curSum += num[i++];
					i %= n;
				}
				sum += (__int64) curSum;
				curR++;
				curP = i;
			}
		}
		printf("%I64d\n", sum);
	}
	return 0;
}