#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int groups[1010];
__int64 groupCounts[1010];
__int64 personCounts[1010];
int times[1010];
__int64 earns[1010];

void init(int n, int k)
{
	for (int i = 0; i < n; ++ i)
	{
		int left = k - groups[i];
		groupCounts[i] = 1;
		personCounts[i] = groups[i];
		for (int j = (i + 1) % n; j != i; j = (j + 1) % n)
		{
			if (left >= groups[j]) {
				++ groupCounts[i];
				personCounts[i] += groups[j];
				left -= groups[j];
			} else {
				break;
			}
		}
	}
	memset(times, 0xff, sizeof(times));
	memset(earns, 0, sizeof(earns));
}

int main()
{
	fstream inputFile("F:/gcj/data3s.in", ios_base::in);
	fstream outputFile("F:/gcj/data3s.out", ios_base::out);
	
	int caseCount;
	inputFile >> caseCount;
	for (int ci = 0; ci < caseCount; ++ ci)
	{
		int r, k, n;
		inputFile >> r >> k >> n;
		for (int i = 0; i < n; ++ i) inputFile >> groups[i];
		init(n, k);
		int last = 0;
		int cnt = 0;
		times[0] = earns[0] = 0;
		__int64 ret = 0;
		bool circleFound = false;
		while (r > 0)
		{
			int next = (last + groupCounts[last]) % n;
			-- r;
			++ cnt;
			ret += personCounts[last];

			if (!circleFound) {
				if (times[next] != -1) {
					int circleLength = cnt - times[next];
					int circleTimes = r / circleLength;
					__int64 circleEarn = ret - earns[next];
					r %= circleLength;
					ret += (__int64)circleTimes * circleEarn;
					circleFound = true;
				} else {
					earns[next] = ret;
					times[next] = cnt;
				}
			}

			last = next;
		}

		outputFile << "Case #" << ci + 1 << ": " << ret << endl;
	}

	inputFile.close();
	outputFile.close();
	return 0;
}