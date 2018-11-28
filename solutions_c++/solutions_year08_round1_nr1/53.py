#include <iostream>
#include <algorithm>
using namespace std;

const int maxN = 1000;
long long A[maxN], B[maxN];

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t ++)
	{
		int N;
		cin >> N;
		for (int i = 0; i < N; i ++) cin >> A[i];
		for (int i = 0; i < N; i ++) cin >> B[i];
		sort(A, A + N); sort(B, B + N);
		long long ans = 0;
		for (int i = 0; i < N; i ++)
			ans += (A[i] * B[N - i - 1]);
		cout << "Case #" << t << ": " << ans << endl;
	}
}
