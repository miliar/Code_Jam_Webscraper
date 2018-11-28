
#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		int N;
		cin >> N;

		int price, cheap = -1, sum = 0, xsum = 0;

		for (int j = 0; j < N; j++)
		{
			cin >> price;
			if (cheap == -1) cheap = price;
			if (price < cheap) cheap = price;

			sum += price;
			xsum ^= price;
		}

		cout << "Case #" << (i+1) << ": ";
		if (xsum == 0)
		{
			cout << sum - cheap;
		} else
		{
			cout << "NO";
		}
		cout << endl;
	}
}
