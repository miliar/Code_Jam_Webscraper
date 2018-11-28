#include <iostream>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int C = 1; C <= T; C++)
	{
		int N, K;
		cin >> N >> K;
		cout << "Case #" << C << ": ";
		if ((K + 1) % (1 << N))
			cout << "OFF";
		else
			cout << "ON";
		cout << endl;
	}
}