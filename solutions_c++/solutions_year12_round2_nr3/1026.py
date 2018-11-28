#include <iostream>
#include <fstream>
#include <algorithm>
#include <bitset>
#include <cstdint>

using namespace std;

uint64_t S[20];

const int L = 1024 * 1024; // 2^20
uint64_t sums[L];

void printSet(int a, int n, ostream& output)
{
	bitset<20> bs(a);
	for (int i = 0; i < n; ++i)
		if (bs[i])
			output << S[i] << " ";
}

void solve(istream& input, ostream& output)
{
	int n;
	input >> n;

	for (int i = 0; i < n; ++i)
		input >> S[i];

	for (int i = 0; i < L; ++i)
	{
		uint64_t sum = 0;
		bitset<20> bs(i);
		for (int j = 0; j < n; ++j)
			sum += S[j] * (int)bs[j];

		auto match = find(sums, sums + i, sum);
		if (match != sums + i)
		{
			printSet(distance(sums, match), n, output);
			output << "\n";
			printSet(i, n, output);
			output << "\n";
			return;
		}

		sums[i] = sum;
	}
}

int main()
{
	ifstream fin("C-small-attempt0.in");
	int t;
	fin >> t;

	ofstream cout("output.txt");
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ":\n";
		solve(fin, cout);
	}
}