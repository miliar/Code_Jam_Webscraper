#include <iostream>

using namespace std;

int main()
{
	int* g, R, k, N, T, num;
	g = new int[1000];
	int head;
	int result;
	int remain;
	int round;
	int i;

	cin >> T;
	for(num = 1; num <= T; num++)
	{
		cin >> R >> k >> N;
		for(head = 0; head < N; head++)
		{
			cin >> g[head];
		}
		for(round = 0, result = 0, head = 0; round < R; round++)
		{
			for(remain = k, i=0; remain >= g[head] && i < N; head = (head+1) % N, i++)
			{
				result += g[head];
				remain -= g[head];
			}
		}
		cout << "Case #" << num << ": "<< result << endl;
	}
	delete[] g;
	return 0;
}
