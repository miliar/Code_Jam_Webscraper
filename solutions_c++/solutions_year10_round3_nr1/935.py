#include <cassert>
#include <cmath>
#include <cctype>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <functional>

using namespace std;
typedef vector<int> vi_t;
typedef vector<string> vs_t;
typedef long long i64_t;

bool IsIntersec(int a1, int b1, int a2, int b2)
{
	return (a1 > a2 == b1 < b2);
}

int main(int ac, char const* av[])
{
    ifstream cin(av[1]);
    int T; cin >> T; cin.ignore();

    for (int t = 1; t <= T; ++t)
    {
		int N;
		cin >> N;
		vi_t  A(N), B(N);
		for (int i = 0; i < N; ++i)
		{
			cin >> A[i] >> B[i];
		}
		int res = 0;
		for (int i = 0; i < N - 1; ++i)
			for (int j = i + 1; j < N; ++j)
			{
				if (IsIntersec(A[i], B[i], A[j], B[j]))
					++res;
			}
      cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}
