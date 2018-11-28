#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
	int C;
	cin >> C;
	for(int No = 1; No <= C; No++)
	{
		int N, K, B, T;
		cin >> N >> K >> B >> T;
		vector<int> X(N), V(N);
		for(int i = 0; i < N; i++)
			cin >> X[i];
		for(int i = 0; i < N; i++)
			cin >> V[i];
		reverse(X.begin(), X.end());
		reverse(V.begin(), V.end());
		
		int ans = 0;
		int count = 0;
		for(int j = 0; j < N; j++)
		{
			if(B <= X[j] + V[j] * T)
			{
				ans += j - count;
				if(++count >= K)
					break;
			}
		}
		if(count >= K)
			cout << "Case #" << No << ": " << ans << endl;
		else
			cout << "Case #" << No << ": " << "IMPOSSIBLE" << endl;
	}
	return 0;
}
