#include <iostream>

using namespace std;

const int MaxN = 31;

int runs, N, K;
int opt[MaxN];

int main()
{
	opt[0] = 0;
	for (int i = 1; i < MaxN; ++i)
		opt[i] = opt[i-1] * 2 + 1;
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);
	cin >> runs;
	for (int run = 1; run <= runs; ++run)
	{
		cin >> N >> K;
		K = K % (opt[N] + 1);
		string ans = "";
//		cout << N << " " << opt[N-1] << " " << K << endl;
		if (K == opt[N])
			ans = "ON";
		else
			ans = "OFF";
		cout << "Case #" << run << ": " << ans << endl;
	}
}
