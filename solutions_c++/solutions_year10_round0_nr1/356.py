#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++)
	{
		int N, K;
		cin >> N >> K;
		cout << "Case #" << i << ": " << ((((1 << N) - 1) & (K+1)) == 0 ? "ON" : "OFF") << endl;
	}
	return 0;
}
