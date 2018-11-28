// A.cpp : Defines the entry point for the console application.
//

#include <fstream>

std::ifstream in("A-large.in");
//std::ifstream in("A.in");
std::ofstream out("A.out");

int solve()
{
	int N;
	int A[1001], B[1001];

	in >> N;
	for (int i = 0; i < N; ++i)
		in >> A[i] >> B[i];

	if (1 == N)
		return 0;

	int r = 0;
	for (int i = 0; i < N; ++i)
		for (int j =  i + 1; j < N; ++j)
		{
			//int d = A[i]*(B[j] - A[j]) - A[j]*(B[i] - A[i]);
			int d = 1*(A[i] - B[i]) - 1*(A[j] - B[j]);
			if (0 != d)
			{
				int d1 = 1*A[i] - 1*A[j];
				double x = double(d1)/d;
				if (0 <= x && x <= 1)
					++r;
			}
		}

	return r;
}


int main()
{
	int T;
	in >> T;
	for (int i = 0; i < T; ++i)
		out << "Case #" << (i + 1) << ": " << solve() << "\n";

	return 0;
}

