#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>

using namespace std;

const int NMAX = 1000;

int A[NMAX], B[NMAX];

int main()
{
	freopen("input.txt",  "r", stdin);
	freopen("output.txt", "w", stdout);

	int counttest;
	cin >> counttest;
	for (int test = 0; test < counttest; ++test)
	{
		int n;
		cin >> n;
		for (int i = 0; i < n; ++i)
			cin >> A[i] >> B[i];

		int cnt = 0;
		for (int i = 0; i < n - 1; ++i)
			for (int j = i + 1; j < n; ++j)
				if (A[i] > A[j] && B[i] < B[j] || A[i] < A[j] && B[i] > B[j])
					++cnt;

		cout << "Case #" << test + 1 << ": " << cnt << endl;
	}

	return 0;
}