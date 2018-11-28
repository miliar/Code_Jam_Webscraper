// Task A
// MS Visual Studio 2008 Express Edition
// Snapper Chain


#include <iostream>

using namespace std;


bool snap_k_tymes(int N, int K)
{	
	if (K < N) return false;

	int cycle = (0x01 << N);
	return (K % cycle) == (cycle - 1);
}



int main()
{
	int T = 0;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{		
		int N = 0, K = 0;
		cin >> N >> K;
		cout << "Case #" << (i+1) << ": ";
		cout << (snap_k_tymes(N, K) ? "ON" : "OFF") << "\n";
	}
	
	return 0;
}
