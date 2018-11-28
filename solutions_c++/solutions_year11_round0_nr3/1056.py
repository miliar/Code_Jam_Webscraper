#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <string>

using namespace std;

int main(int argc, char **argv)
{
	int T;
	freopen("C-large.in", "rb", stdin);
	freopen("C-large.out", "wb", stdout);

	scanf("%d", &T);

	for(int t = 0; t < T; t++)
	{
		int N;
		scanf("%d", &N);
		vector<int> nums(N);
		for(int i = 0; i < N; i++)
		{
			scanf("%d", &nums[i]);
		}

		sort(nums.begin(), nums.end());

		int xor = 0, sum = 0;
		for(int i = 0; i < nums.size(); i++)
		{
			xor ^= nums[i];
			sum += nums[i];
		}

		if(xor != 0)
		{
			printf("Case #%d: NO\n", t + 1);
		}
		else
		{
			printf("Case #%d: %d\n", t + 1, sum - nums[0]);
		}
	}

	return 0;
}