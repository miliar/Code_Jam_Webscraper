#include <iostream>

using namespace std;

const int MaxN = 1005;

int runs, R, K, N;
int group[MaxN], income[MaxN], nextState[MaxN];
bool visited[MaxN];

int main()
{
	freopen("small_3.in", "r", stdin);
	freopen("small_3.out", "w", stdout);
	cin >> runs;
	for (int run = 1; run <= runs; ++run)
	{
		cin >> R >> K >> N;
		for (int i = 0; i < N; ++i)
			cin >> group[i];

		for (int i = 0; i < N; ++i)
		{
			int j = i;
			int sum = 0;
			while (true)
			{
				if (sum + group[j] <= K)
				{
					sum += group[j];
					j++;
					if (j == N) j = 0;
					if (j == i) break;
				}
				else 
					break;
			}
			income[i] = sum;
			nextState[i] = j;
		}

		memset(visited, 0, sizeof visited);
		int pos = 0;
		int circleSum = 0, preSum = 0;
		int circleLen = 0, preLen = 0;
		int circleBeginPos = -1;
		while (true)
		{
			visited[pos] = true;
			if (circleBeginPos != -1)
			{
				circleSum += income[pos];
				circleLen++;
			}
			else
			{
				preLen++;
				preSum += income[pos];
			}
			pos = nextState[pos];
			if (visited[pos])
				if (circleBeginPos == -1)
					circleBeginPos = pos;			
				else if (circleBeginPos == pos)
					break;
		}
		preLen -= circleLen;
		preSum -= circleSum;
		R -= preLen;
		int total = preSum + R / circleLen * circleSum;
		pos = circleBeginPos;
		for (int i = 0; i < R % circleLen; ++i)
		{
			total += income[pos];
			pos = nextState[pos];
		}

		cout << "Case #" << run << ": " << total << endl;
	}
}
