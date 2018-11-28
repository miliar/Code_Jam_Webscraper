#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <numeric>

using namespace std;

void makeseq(vector <long long> & seq, long long m, long long n, long long x, long long y, long long z, vector <long long> & a)
{
	int i;

	for(i = 0; i < n; ++i)
	{
		seq.push_back(a[i % m]);
		a[i % m] = (((x % z) * (a[i % m] % z)) % z + ((y % z) * ((i + 1) % z)) % z) % z;
	}
}


int main()
{
	ifstream fin("c.in");
	ofstream fout("c.out");

	int T, N;

	fin >> N;

	for(T = 1; T <= N; ++T)
	{
		int i, j;
		long long m, n, x, y, z;

		fout << "Case #" << T << ": ";
		fin >> n >> m >> x >> y >> z;

		vector <long long> a(m);
		vector <long long> seq;

		for(i = 0; i < m; ++i)
			fin >> a[i];
		makeseq(seq, m, n, x, y, z, a);

		/*for(i = 0; i < seq.size(); ++i)
			cout << seq[i] << " ";
		cout << endl;*/

		vector <long long> res(n, 1);

		for(i = n - 2; i >= 0; --i)
		{
			for(j = i + 1; j < n; ++j)
				if (seq[i] < seq[j]) res[i] = ((res[i] % 1000000007) + (res[j] % 1000000007)) % 1000000007;
		}

		long long ans = 0;
		for(i = 0; i < n; ++i)
			ans = ((ans % 1000000007) + (res[i] % 1000000007)) %1000000007;

		fout << ans << endl;
	}
	return 0;
}