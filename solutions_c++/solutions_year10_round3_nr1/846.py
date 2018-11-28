#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair <int, int> pii;

int main()
{
	int C;
	cin >> C;
	for (int _case = 1; _case <= C; _case++)
	{
		int N, res = 0;
		cin >> N;
		vector<pii> w(N);
		
		for (int i = 0; i < N; i++)
			cin >> w[i].first >> w[i].second;
		
		sort(w.begin(), w.end());
		
		for (int i = 0;	i < N; i++)
		{
			for (int j = i + 1; j < N; j++)
			{
				if (w[i].second > w[j].second)
					res++;
			}			
		}
		
		cout << "Case #" << _case << ": " << res << endl;
	}
}
