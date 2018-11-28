#include <cstdio>
#include <iostream>
#include <string>
#include <set>

#define FOR(I, N) for(int I = 0, end_ = (N); I < end_; ++I)
int ri() { int r; scanf("%d", &r); return r; }
std::string const rs() { std::string r; std::cin >> r; return r; }

bool isInRange(std::string const& A, std::string const& B, std::string const& C, unsigned pos)
{
	for (unsigned i = 0, p = pos, N = A.length(); i < N; ++i, ++p)
	{
		if (C[p] < A[i]) return false;
		if (A[i] < C[p]) break;
	}
	for (unsigned i = 0, p = pos, N = B.length(); i < N; ++i, ++p)
	{
		if (C[p] < B[i]) break;
		if (B[i] < C[p]) return false;
	}
	return true;
}

int stoi(std::string const& S, int pos, int length)
{
	int res = S[pos] - '0', end = pos + length;
	while(++pos < end)
		res = 10*res + S[pos] - '0';
	return res;
}

int main()
{
    FOR(i, ri())
    {
		std::string A = rs(), B = rs(), C = A + A;
		int Z[] = {0, 0, 0, 0, 0, 0, 0, 0};

		do {
			std::set<int> U; int L = A.length();
			for(int pos = 0; pos < L; ++pos)
			{
				if (isInRange(A, B, C, pos))
					U.insert(stoi(C, pos, L));
			}
			++Z[U.size()];

			int index = L - 1;
			while(index >= 0 && C[index] == '9')
				--index;
			if (index < 0)
				break;
			++C[index], ++C[index + L];
			while(++index < L)
				C[index] = '0', C[index + L] = '0';
		}
		while(isInRange(A, B, C, 0));

		printf("Case #%d: %d\n", i + 1, Z[2]/2 + Z[3] + 3*Z[4]/2 + 2*Z[5] + 5*Z[6]/2 + 3*Z[7]);
    }
}