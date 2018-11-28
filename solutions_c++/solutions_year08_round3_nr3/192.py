#include <cstdio>
#include <cstring>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

#define MOD 1000000007

long long n, m, X, Y, Z;
vector<long long> A;
vector<long long> sign;
vector<long long> D;
long long result;

void solve(void)
{
	D.clear();
	result = 0;

	for (int i = 0 ; i < n ; ++i)
	{
		int d = 1;

		for (int j = 0 ; j < i ; ++j)
		{
			if (sign[j] < sign[i])
			{
				d += D[j];
				d %= MOD;
			}
		}

		D.push_back(d);
		result += d;
		result %= MOD;
	}
}

int main(void)
{
	ifstream fin("c.in");
	ofstream fout("c.out");

	int T;
	fin >> T;

	for (int t = 1 ; t <= T ; ++t)
	{
		A.clear();
		sign.clear();

		fin >> n >> m >> X >> Y >> Z;

		for (int i = 0 ; i < m ; ++i)
		{
			long long a;
			fin >> a;
			A.push_back(a);
		}

		for (int i = 0 ; i < n ; ++i)
		{
			sign.push_back(A[i%m]);
			A[i%m] = (X*A[i%m] + Y*(i + 1))%Z;
		}

		solve();

		fout << "Case #" << t << ": " << result << endl;
	}

	fin.close();
	fout.close();
}
