#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

__int64 gcd(__int64 a, __int64 b)
{
	if (a < b) return gcd(b, a);
	int r = a % b;
	if (r == 0) return b;
	return gcd(b, r);
}

__int64 nums[4];

int main()
{
	fstream inputFile("F:/gcj/data2s.in", ios_base::in);
	fstream outputFile("F:/gcj/data2s.out", ios_base::out);
	
	int caseCount;
	inputFile >> caseCount;
	for (int ci = 0; ci < caseCount; ++ ci)
	{
		int n;
		inputFile >> n;
		for (int i = 0; i < n; ++ i) inputFile >> nums[i];
		sort(nums, nums + n);
		int numberCount = 1;
		for (int i = 1; i < n; ++ i)
		{
			if (nums[i] != nums[i - 1]) {
				nums[numberCount ++] = nums[i];
			}
		}
		__int64 T = nums[1] - nums[0];
		for (int i = 2; i < numberCount; ++ i)
		{
			T = gcd(T, nums[i] - nums[i - 1]);
		}
		__int64 ret = nums[0] % T;
		if (ret != 0) ret = T - ret;
		outputFile << "Case #" << ci + 1 << ": " << ret << endl;
	}

	inputFile.close();
	outputFile.close();
	return 0;
}