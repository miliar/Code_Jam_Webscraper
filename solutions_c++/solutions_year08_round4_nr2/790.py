// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>

std::ifstream in("A.in");
std::ofstream out("A.out");

void solve(long long N, long long M, long long A)
{
	for (long long a1 = 0; a1 <= N; ++a1)
		for (long long a2 = 0; a2 <= M; ++a2)
			for (long long b1 = 0; b1 <= N; ++b1)
				for (long long b2 = 0; b2 <= M; ++b2)
				{
					if ((a1*b2 - a2*b1) == A)
					{
						for (long long x3 = N; x3 >= 0; --x3)
							if ((x3 - (b1 - a1) <= N) && (x3 - (b1 - a1) >= 0) && (x3 - b1 >= 0))
							{
								for (long long y3 = M; y3 >= 0; --y3)
									if ((y3 - (b2 - a2) <= M) && (y3 - (b2 - a2) >= 0) && (y3 - b2 >= 0))
									{
										out << (x3 - (b1 - a1)) << " " << (y3 - (b2 - a2)) << " "
											<< (x3 - b1) << " " << (y3 - b2) << " "
											<< x3 << " " << y3 << "\n";

										return;
									}
							}
					}
				}

	out << "IMPOSSIBLE\n";
}

int _tmain(int argc, _TCHAR* argv[])
{
	int C;
	in >> C;

	for (int i = 0; i < C; ++i)
	{
		long long N, M, A;
		in >> N >> M >> A;

		out << "Case #" << (i + 1) << ": ";
		solve(N, M, A);
	}
	return 0;
}

