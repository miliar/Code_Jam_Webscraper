/*
Problem

Pontius: You know, I like this number 127, I don't know why.
Woland: Well, that is an object so pure. You know the prime numbers.
Pontius: Surely I do. Those are the objects possessed by our ancient masters hundreds of years ago. Oh, yes, why then? 127 is indeed a prime number as I was told.
Woland: Not... only... that. 127 is the 31st prime number; then, 31 is itself a prime, it is the 11th; and 11 is the 5th; 5 is the 3rd; 3, you know, is the second; and finally 2 is the 1st.
Pontius: Heh, that is indeed... purely prime.

The game can be played on any subset S of positive integers. A number in S is considered pure with respect to S if, starting from it, you can continue taking its rank in S, and get a number that is also in S, until in finite steps you hit the number 1, which is not in S.

When n is given, in how many ways you can pick S, a subset of {2, 3, ..., n}, so that n is pure, with respect to S? The answer might be a big number, you need to output it modulo 100003.
Input

The first line of the input gives the number of test cases, T. T lines follow. Each contains a single integer n.
Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the answer as described above.
Limits
T <= 100.
Small dataset

2 <= n <= 25.
Large dataset

2 <= n <= 500.
Sample

Input

2
5
6

Output

Case #1: 5
Case #2: 8
*/

#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

bool IsPure(const vector<int>& nums)
{
	int i = nums.back();
	for ( ;; )
	{
		vector<int>::const_iterator it = find(nums.begin(), nums.end(), i);
		if ( it == nums.end() )
			return false;
		if ( it == nums.begin() )
			return true;
		i = (it - nums.begin()) + 1;
	}
	return true;
}

int TestOne(vector<int>& nums, size_t idx)
{
	if ( idx == nums.size()-1 )
		return IsPure(nums) ? 1 : 0;
	int val = nums[idx];
	int cnt = TestOne(nums, idx+1);
	nums.erase(nums.begin()+idx);
	cnt += TestOne(nums, idx);
	nums.insert(nums.begin()+idx, val);
	return cnt;
}

void main()
{
	int T, n;
	vector<int> nums;

	scanf("%d\n", &T);
	for ( int t = 0; t < T; ++t )
	{
		scanf("%d\n", &n);
		nums.resize(n-1);
		for ( int i = 2; i <= n; ++i )
			nums[i-2] = i;
		printf("Case #%d: %d\n", t+1, TestOne(nums, 0) % 100003);
	}
}