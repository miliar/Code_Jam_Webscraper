#include <iostream>
using namespace std;
int main()
{
	unsigned long N, K, T, temp, i;
	cin >> T;
	for (i = 0; i < T; i++) {
		cin >> N;
		cin >> K;
		temp = K + 1;
		temp = temp % (1 << N);
		cout << "Case #" << i + 1<< ": " << ((temp == 0) ? "ON" : "OFF") << ((i == (T - 1))? "":"\n");
	}

	return 0;
}
