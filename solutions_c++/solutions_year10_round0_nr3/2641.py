#include <iostream>
#include <queue>

using namespace std;

typedef queue<int> QUEUE;

int NextBatch(QUEUE& q, int k, int N)
{
	int batch = 0, i = 0;
	while(batch < k && i < N)
	{
		int temp = q.front();
		if(batch + temp <= k)
		{
			batch += temp;
			q.pop();
			q.push(temp);
		}
		else
			break;
		++i;
	}
	return batch;
}

unsigned __int64 Solve()
{
	QUEUE q;

	unsigned __int64 money = 0;
	int R, k, N;
	cin >> R >> k >> N;

	int g;
	for(int i = 0; i < N; ++i)
	{
		cin >> g;
		q.push(g);
	}

	if(N == 1) return g*R;

	for(int i = 0; i < R; ++i)
	{
		money += NextBatch(q, k, N);
	}

	return money;
}

void main()
{
	int T;
	
	cin >> T;

	for(int i = 1; i <= T; ++i)
	{
		cout << "Case #" << i << ": " << Solve() << endl;
	}
}