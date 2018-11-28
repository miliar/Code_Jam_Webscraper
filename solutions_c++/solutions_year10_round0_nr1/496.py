#include <iostream>
#include <vector>

using namespace std;

int Pow2(int degree)
{
	if (degree == 1)
	{
		return 2;
	}
	int a = Pow2(degree / 2);
	if (degree % 2 == 0)
	{
		return a * a;
	}
	return 2 * a * a;
}

int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	int NumberOfTests;
	cin >> NumberOfTests;
	for (int i = 1; i <= NumberOfTests; ++i)
	{
		int N;
		long long int K;
		cin >> N >> K;
		cout << "Case #" << i << ": ";
		if ((K + 1) % Pow2(N) == 0)
		{
			cout << "ON";
		}
		else
		{
			cout << "OFF";
		}
		cout << endl;
		
	}
	return 0;
}
