#include <iostream>
using namespace std;

long long a[10005];

void solve(int cID)
{
	int N;
	long long L, H;
	cin >> N >> L >> H;
	for (int i = 0; i < N; i ++) cin >> a[i];

	cout << "Case #" << cID << ": ";
	bool f = true;
	for (long long i = L; i <= H; i ++)
	{
		f = true;
		for (int j = 0; j < N; j ++)
			if (a[j] % i != 0 && i % a[j] != 0)
			{
				f = false;
				break;
			}
		if (f) {cout << i << endl;
			return;
		}
	}
	cout << "NO\n";

}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t ++)
		solve(t);
}
