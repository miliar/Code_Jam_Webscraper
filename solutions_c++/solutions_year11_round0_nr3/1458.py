#include <iostream>
using namespace std;

int main(void)
{
	int N;
	cin >> N;
	for (int t = 1; t <= N; t++)
	{
		int m = 10000000, s = 0, l, r;
		long long T = 0;
		cin >> l;
		for (int i = 0; i<l; i++)
		{
			cin >> r;
			s ^= r, m = min(m,r), T += (long long)r;
		}
		cout << "Case #" << t << ": ";
		if ( s != 0)
			cout << "NO\n";
		else
			cout << (T - m) << endl;
	}
	return 0;
}
