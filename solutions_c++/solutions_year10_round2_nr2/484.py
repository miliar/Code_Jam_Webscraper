#include <iostream>
#include <fstream>
#include <algorithm>
#include <string.h>
#include <vector>
#include <string>
using namespace std;

int pos[200];
int v[200];
bool can[200];

int calc(int n, int k)
{
	int ret = 0;
	for (int i = 0; i < k; ++ i)
	{
		if (!can[i]) {
			int j = i + 1;
			for (; !can[j] && j < n; ++ j);
			if (j == n) return -1;
			swap(can[i], can[j]);
			ret += (j - i);
		}
	}
	return ret;
}

int main()
{
	fstream inputFile("F:/gcj/data2s.in", ios_base::in);
	fstream outputFile("F:/gcj/data2s.out", ios_base::out);

	int caseCount;
	inputFile >> caseCount;
	int caseIndex = 0;
	while (caseCount -- > 0)
	{
		++ caseIndex;
		int n, k, b, t;
		inputFile >> n >> k >> b >> t;
		for (int i = 0; i < n; ++ i)
		{
			inputFile >> pos[i];
		}
		for (int i = 0; i < n; ++ i)
		{
			inputFile >> v[i];
		}
		for (int i = 0; i < n; ++ i)
		{
			can[i] = (b - pos[i] <= v[i] * t);
		}
		for (int b = 0, e = n - 1; b < e; ++ b, -- e) swap(can[b], can[e]);
		int ret = calc(n, k);
		outputFile << "Case #" << caseIndex << ": ";
		if (ret == -1) outputFile << "IMPOSSIBLE" << endl;
		else outputFile << ret << endl;
	}

	inputFile.close();
	outputFile.close();
	return 0;
}