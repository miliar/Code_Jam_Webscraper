#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int C;
	cin >> C;
	
	for (int c = 1; c <= C; c++)
	{
		int R, k, N;
		cin >> R >> k >> N;
		vector<int> group(N);
		vector<int> sum(N, 0);
		vector<int> next(N);
		
		for (int i = 0; i < N; i++)
			cin >> group[i];
			
		for (int i = 0; i < N; i++)
		{
			next[i] = i+1;
			if ( group[i] <= k) 
			{
				int amount = group[i];
			
				int j = (i + 1) % N;
				while (i != j && amount + group[j] <= k)
				{
					amount += group[j];
					j = (j + 1) % N;
				}
				next[i] = j;
				sum[i]  = amount;
			}
		}
	
		int actual = 0;
		long long res = 0;
		for (int i = 0; i < R; i++)
		{
			res += sum[actual];
			actual = next[actual];
		}
		
		cout << "Case #" << c << ": " << res << endl;
	}
}
