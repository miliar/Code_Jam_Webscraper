#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int T, N;
	vector<int> A;
	vector<int> B;
	int i, j, k, caseCount = 1, ret;

	A.assign(1000, 0);
	B.assign(1000, 0);

	cin >> T;

	for(i = 0; i < T; ++i)
	{
		cin >> N;
		ret = 0;

		for(j = 0; j < N; ++j)
		{
			cin >> A[j] >> B[j];
		}

		for(j = 0; j < N; ++j)
		{
			for(k = j + 1; k < N; ++k)
			{
				if((A[j] < A[k] && B[j] < B[k]) || (A[j] > A[k] && B[j] > B[k])) continue;
				else ++ret;
			}
		}
		printf("Case #%d: %d\n", caseCount++, ret);
	}
	return 0;
} 