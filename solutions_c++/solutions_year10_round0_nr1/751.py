#include <fstream>

using namespace std;

ifstream fin ("input.txt");
ofstream fout("output.txt");

#define ull unsigned long long

ull power(ull n)
{
	ull ans = 1;
	for (ull i = 0; i < n; ++i)
		ans *= 2;
	return ans;
}

int main()
{
	int t;
	fin >> t;

	ull n;
	ull k;

	for (int it = 0; it < t; it++)
	{
		fout << "Case #" << it+1 << ": ";
		int ok;
		fin >> n >> k;
		n = power(n);
		k = k+1;
		ok = k%n;
		if (!ok) fout << "ON";
		else fout << "OFF";
		fout << endl;
	}

	return 0;
}