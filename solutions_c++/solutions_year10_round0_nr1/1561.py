#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	
	for(int i = 1; i <= T; i++)
	{
		int N, K;
		cin >> N >> K;
		
		cout << "Case #" << i << ": ";
		if((K + 1) % ((long long)1 << N) == 0)
			cout << "ON" << endl;
		else
			cout << "OFF" << endl;
	}
	
	return 0;
}
