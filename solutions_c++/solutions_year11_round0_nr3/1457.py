#include<iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for(int t = 1; t <= T; t++)
	{
		int N;
		cin >> N;
		int numbers[N];
		int smallest = 100000000;
		int xor_sum = 0;
		int sum = 0;
		for(int n = 0; n < N; n++)
		{
			int number;
			cin >> number;
			xor_sum = xor_sum ^ number;
			if(number < smallest)
				smallest = number;
			sum += number;
		}

		cout << "Case #" << t << ": ";
		if(xor_sum != 0)
			cout << "NO";
		else
			cout << (sum - smallest);
		cout << endl;
	}
}
