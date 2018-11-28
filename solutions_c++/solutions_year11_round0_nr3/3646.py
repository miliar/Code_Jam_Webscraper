#include <iostream>
using namespace std;

unsigned int a[1000];
int b[1000];
int ret;

int main()
{
	int cases;

	cin >> cases;

	for(int c = 0; c < cases; c++)
	{
		int n;

		cin >> n;

		unsigned int res = 0;

		unsigned int sum = 0, minA = INT_MAX;

		for(int i = 0; i < n; i++)
		{
			cin >> a[i];
			res = res ^ a[i];
			sum += a[i];
			minA = min(minA, a[i]);
		}

		if (res)
			cout << "Case #" << c + 1 << ": NO" << endl;
		else
			cout << "Case #" << c + 1 << ": " << sum - minA << endl;
	}

	return 0;
}
