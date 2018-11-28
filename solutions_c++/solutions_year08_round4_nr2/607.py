
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>

using namespace std;

#define PATH "c:\\jam3\\jam3\\"

int main(void)
{
    ifstream fin(PATH "s.in");
    ofstream fout(PATH "s.out");

    int count;
    fin >> count;

    for (int c = 1; c <= count; ++c)
    {
		long long N, M, A;
		fin >> N >> M >> A;

		int ans = -1;

		int x[3], y[3];

		if (N * M < A) ans = -1;
		else
		{
			x[0] = 0;
			y[0] = 0;
			for (x[1] = 0; x[1] <= N; x[1]++)
				for (y[1] = 0; y[1] <= M; y[1]++)
					for (x[2] = 0; x[2] <= N; x[2]++)
						for (y[2] = 0; y[2] <= M; y[2]++)
						{
							long long s = x[1] * y[2] - y[1] * x[2];
							if (s == A || s == -A)
							{
								ans = 1;
								goto END;
							}
						}
		}
END:;

		if (ans < 0)
			fout << "Case #" << c << ": IMPOSSIBLE\n";
		else
			fout << "Case #" << c << ":"
			<< " " << x[0] << " " << y [0]
			<< " " << x[1] << " " << y [1]
			<< " " << x[2] << " " << y [2]
			<< "\n";
    }

    return 0;
}

