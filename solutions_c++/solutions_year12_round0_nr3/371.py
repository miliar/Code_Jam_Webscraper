#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

void solve(istream& input, ostream& output)
{
	int A, B;
	input >> A >> B;

	int count = 0;

	vector<int> mem;

	for (int a = A; a < B; ++a)
	{
		mem.clear();
		for (int p = 10, q = pow(10, (int)log10(a)); p <= a; p *= 10, q /= 10)
		{
			int b = a % p * q + a / p;
			if (b > a && b <= B && find(begin(mem), end(mem), b) == end(mem))
			{
				++count;
				mem.push_back(b);
			}
		}
	}

	output << count;
}

int main()
{
	int n;

	ifstream fin("C-large.in");
	fin >> n;

	ofstream fout("output.txt");

	for (int i = 1; i <= n; ++i)
	{
		fout << "Case #" << i << ": ";
		solve(fin, fout);
		fout << '\n';
	}
}