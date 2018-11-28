#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdint>

using namespace std;

int N, M;
uint64_t a[100];
int A[100];
uint64_t b[100];
int B[100];

uint64_t lcs(uint64_t x0, int n, uint64_t an, int m, uint64_t bm)
{
	if (n == 0 && an == 0 || m == 0 && bm == 0)
		return x0;

	if (A[n] != B[m])
	{
		auto lcs1 = n > 0 ? lcs(x0, n - 1, a[n - 1], m, bm) : x0;
		auto lcs2 = m > 0 ? lcs(x0, n, an, m - 1, b[m - 1]) : x0;
		return max(lcs1, lcs2);
	}

	auto x = min(an, bm);
	if (n == 0 && x == an || m == 0 && x == bm)
		return x0 + x;

	an -= x;
	bm -= x;

	if (an == 0)
		an = a[--n];
	if (bm == 0)
		bm = b[--m];

	return lcs(x0 + x, n, an, m, bm);
}

void solve(istream& input, ostream& output)
{
	input >> N >> M;
	for (int i = 0; i < N; ++i)
		input >> a[i] >> A[i];
	for (int i = 0; i < M; ++i)
		input >> b[i] >> B[i];

	output << lcs(0, N - 1, a[N - 1], M - 1, b[M - 1]);
}

int main()
{
	int t;
	ifstream fin("C-small-attempt0.in");
	fin >> t;

	ofstream cout("output.txt");
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		solve(fin, cout);
		cout << "\n";
	}
}