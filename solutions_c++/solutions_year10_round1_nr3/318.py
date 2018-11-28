#include <iostream>
using namespace std;

bool goodgcd(int a, int b)
{
	if (a < b) swap(a, b);
	if (a > 2 * b) return true;
	else return !(goodgcd(b, a - b));
}

int main()
{
	int T;
	cin >> T;
	for (int C = 1; C <= T; C++)
	{
		int A1, A2, B1, B2;
		cin >> A1 >> A2 >> B1 >> B2;

		int ans = 0;
		for (int i = A1; i <= A2; i++)
		{
			for (int j = B1; j <= B2; j++)
			{
				if (goodgcd(i, j))
					ans++;
			}
		}

		cout << "Case #" << C << ": " << ans << endl;
	}
}