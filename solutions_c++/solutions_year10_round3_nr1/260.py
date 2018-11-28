#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <deque>
#include <math.h>

using namespace std;

int main()
{
	freopen("A.in", "rt", stdin);
	freopen("A.out", "wt", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		int N;
		cin >> N;
		vector <int> A(N), B(N);
		for (int j = 0; j < N; ++j)
		{
			cin >> A[j] >> B[j];
		}
		int points = 0;
		for (int j = 0; j < N; ++j)
		{
			for (int k = j + 1; k < N; ++k)
			{
				if ((A[j] < A[k]) && (B[j] > B[k]))
				{
					++points;
				}
				if ((A[j] > A[k]) && (B[j] < B[k]))
				{
					++points;
				}
			}
		}
		cout << "Case #" << i + 1 << ": " << points << endl;	
	}
	return 0;
}
	
	
