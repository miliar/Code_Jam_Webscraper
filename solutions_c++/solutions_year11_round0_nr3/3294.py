#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <cctype>
#include <set>
#include <iostream>
#include <sstream>
#include <ctime>
#include <numeric>

using namespace std;

int T, N, ans;
vector<int> input;

void go(int idx, vector<int> left, vector<int> right)
{
	if(idx == input.size())
	{
		if(left.size() == 0 || right.size() == 0)
			return;
		int xor1 = 0, xor2 = 0;
		for(int i = 0; i < left.size(); i++)
			xor1 ^= left[i];
		for(int i = 0; i < right.size(); i++)
			xor2 ^= right[i];
		if(xor1 == xor2)
		{
// 			printf("Contents of left : ");
// 			for(int i = 0; i < left.size(); i++)
// 				printf("%d ", left[i]);
// 			putchar('\n');
// 			printf("Contents of right : ");
// 			for(int i = 0; i < right.size(); i++)
// 				printf("%d ", right[i]);
// 			putchar('\n');
			ans = max(ans, max(accumulate(left.begin(), left.end(), 0), accumulate(right.begin(), right.end(), 0)));
		}
		return;
	}
	left.push_back(input[idx]);
	go(idx+1, left, right);
	left.pop_back();
	right.push_back(input[idx]);
	go(idx+1, left, right);
}

int main()
{
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d", &N);
		input.clear();
		ans = -1;
		for(int i = 0; i < N; i++)
		{
			int k;
			scanf("%d", &k);
			input.push_back(k);
		}
		vector<int> left;
		vector<int> right;
		go(0, left, right);
		printf("Case #%d: ", t);
		if(ans == -1)
			printf("NO\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}