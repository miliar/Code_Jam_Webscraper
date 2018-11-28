#include <iostream>
using namespace std;

int main()
{
	int C, i, N, K, B, T, j, s, count;
	int X[50], V[50];
	bool p;
	cin >> C;
	for (i = 0; i < C; i++)
	{
		count = 0;
		s = 0;
		cin >> N >> K >> B >> T;
		for (j = 0; j < N; j++)
		{
			cin >> X[j];
		}
		for (j = 0; j < N; j++)
		{
			cin >> V[j];
		}
		for (j = N - 1; j >= 0; j--)
		{
			if (K <= 0) break;
			if (X[j] + V[j] * T < B)
			{
				s++;				
			}
			else 
			{
				count +=s;
				K--;
			}
		}
		if (K > 0) cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << i + 1 << ": " << count << endl;
	}
	return 0;
}