#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char** argv)
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		int N;
		cin >> N;
		vector <int> A(N), B(N);
		for (int j = 0; j < N; ++j)
			cin >> A[j] >> B[j];

		int intersections = 0;

		for (int j = 0; j < A.size(); ++j)
			for (int k = 0; k < A.size(); ++k)
			{
				if (j == k)
					continue;
				if (A[j] > A[k] && B[j] < B[k] || A[j] < A[k] && B[j] > B[k])
					++intersections;
			}

		cout << "Case #" << i << ": " << (intersections / 2) << endl;
	}

	return 0;
}
