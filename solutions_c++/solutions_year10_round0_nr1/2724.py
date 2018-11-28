#include <iostream>

using namespace std;

bool Solve()
{
	int N, K;
	cin >> N >> K;

	if(N == 1) return K % 2 > 0;
	int p1 = 1 << N;
	int p = p1 - 1;

	if(K == 0 || K < p) return false;

	if(K == p) return true;

	return K % p1 == p;
}

void main()
{
	int i = 47 % 16;
	int T;
	
	cin >> T;

	for(int i = 1; i <= T; ++i)
	{
		cout << "Case #" << i << ": " << (Solve() ? "ON" : "OFF") << endl;
	}
}