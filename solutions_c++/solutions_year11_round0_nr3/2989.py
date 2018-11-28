#include <algorithm>
#include <stdio.h>
#include <vector>
#include <assert.h>
#include <functional>

// patrick addition
unsigned int
patrick(unsigned int a, unsigned int b)
{
	//int result = 0;
	//for (int i = 0; i < sizeof(int)*8; ++i)
	//{
	//	unsigned int mask = 0x1 << i;
	//	result |= (a & mask) ^ (b & mask);
	//}
	//return result;
	return a ^ b;
}

int
patrician_sum(std::vector<int> &input)
{
	int sum = 0;
	for (auto i : input)
		sum = patrick(sum, i);
	return sum;
}

int
solve(std::vector<int> &input)
{
	//int sean = 0;

	/* iff candies can be patricially equi-
	 * dividable, it mean patrician sum of
	 * whole candies is 0 */
	/* patrician-add is just a bitwise XOR */
	if (patrician_sum(input) != 0)
		return -1;

	std::sort(input.begin(), input.end(), std::greater<int>());

	//int len = input.size();
	//int cur = 0;
	//for (int i = sizeof(int) * 8 - 1; i >= 0; --i)
	//{
	//	//printf("%d th bit\n", i);
	//	unsigned int mask = 1 << i;
	//	while (cur < len)
	//	{
	//		// if bit is set.
	//		if ((input[cur] & mask)
	//				// if next candy is also set
	//				&& (cur+1 < len && (input[cur+1] & mask)))
	//		{
	//			// then its seans
	//			sean += input[cur];
	//			sean += input[cur+1];
	//			//printf("%d %d ", input[cur], input[cur+1]);
	//			cur += 2;
	//		}
	//		else
	//		{
	//			// if first condition was met.
	//			if (input[cur] & mask)
	//			{
	//				//printf("aa\n");
	//				cur += 1;
	//			}
	//			//printf("bb\n");
	//			break;
	//		}
	//	}
	//}

	int sum = 0;
	for (auto i : input)
		sum += i;

	// if patrick gets 0 candies,
	//if (sean == sum)
	//{
		// just give up the smallest one. sorry patrick!!!
		sum -= input[input.size()-1];
	//}

	return sum;
}

void
run_test(int test_id)
{
	std::vector<int> candies;

	int n_candies;
	scanf("%d", &n_candies);
	for (int i = 0; i < n_candies; ++i)
	{
		int value = 0; // value of the candy
		scanf("%d", &value);
		candies.push_back(value);
	}

	int sean = solve(candies);

	printf("Case #%d: ", test_id);
	if (sean != -1)
		printf("%d\n", sean);
	else
		printf("NO\n");
}

int
main(int argc, char const **argv)
{
	// run some patrick tests
	assert(patrick(4, 5) == 1);
	assert(patrick(7, 9) == 14);
	assert(patrick(50, 10) == 56);

	int n_tests;
	scanf("%d", &n_tests);
	for (int i = 0; i < n_tests; ++i)
		run_test(i + 1);
	
	return 0;
}
