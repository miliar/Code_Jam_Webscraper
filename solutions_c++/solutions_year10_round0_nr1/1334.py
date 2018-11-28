#include <iostream>
using namespace std;

int main()
{
	int T, N, i, j;
	int K;

	cin >> T;
	for(i = 0; i < T; ++i)
	{
		cin >> N >> K;
		for(j = 0; j < N; ++j)
			if(((1<<j) & K) != (1<<j)) break;
		cout << "Case #" << i+1 << ": ";
		if(j < N) cout << "OFF";
		else cout << "ON";
		cout << endl;
	}
	return 0;
} 