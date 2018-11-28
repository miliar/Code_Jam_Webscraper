#include <stdio.h>
#include <atlstr.h>
#include <vector>
#include <algorithm>

const int mod = 1000000007;
int N = 0, n = 0, m = 0, X = 0, Y = 0, Z = 0, numSequences = 0;
std::vector<int> A, limits, seqSum;

void setSeqCount(int pos)
{
	int count = 1;
	for (int c = pos + 1; c < n; ++c)
	{
		if (limits[pos] < limits[c])
			count = int((__int64(count) + seqSum[c]) % mod);
	}

	seqSum[pos] = count;
}

int _tmain()
{
	int res = _ftscanf_s(stdin, _T("%u\n"), &N);
	if (res != 1)
		return -1;

	for (int Nc = 0; Nc < N; ++Nc)
	{
		res = _ftscanf_s(stdin, _T("%u%u%u%u%u\n"), &n, &m, &X, &Y, &Z);
		if (res != 5)
			return -2;

		limits.resize(n);
		seqSum.clear();
		seqSum.resize(n, 0);
		A.resize(m);

		for (int mc = 0; mc < m; ++mc)
		{
			res = _ftscanf_s(stdin, _T("%u\n"), &A[mc]);
			if (res != 1)
				return -3;
		};

		for (int nc = 0; nc < n; ++nc)
		{
			limits[nc] = A[nc % m];
			A[nc % m] = int((__int64(X) * A[nc % m] + __int64(Y) * (nc + 1)) % Z);
		};

		numSequences = 0;
		for (int nc = n - 1; nc >= 0; --nc)
		{
			setSeqCount(nc);
			numSequences = int((__int64(numSequences) + seqSum[nc]) % mod);
		}

		_ftprintf_s(stdout, _T("Case #%u: %u\n"), Nc + 1, numSequences);
	};

	return 0;
}