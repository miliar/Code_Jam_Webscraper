#include <iostream>
using namespace std;
int g[2000];
long long cap[1000];
int link[1000];
bool visited[1000];
int queue[1000];

int main()
{
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++)
	{
		int R, k, N;
		cin >> R >> k >> N;
		for(int j = 0; j < N; j++)
		{
			cin >> g[j];
			g[N + j] = g[j];
		}
		long long sum = 0;
		int start = 0;
		int end = 0;
		while(start < N)
		{
			while(sum + g[end] <= k && end - start < N)
			{
				sum += g[end++];
			}
			cap[start] = sum;
			link[start] = end % N;
			sum -= g[start];
			start++;
		}
		long long amt = 0;
		memset(visited, 0, sizeof(visited));
		int node = 0;
		int pushed = 0;
		while (R > 0)
		{
			if(!visited[node])
			{
				visited[node] = true;
				queue[pushed++] = node;
				R--;
				amt += cap[node];
				node = link[node];
			}
			else
			{
				//chain found
				bool found = false;
				int queue_size = 0;
				long long queue_amt = 0;
				for(int j = 0; j < pushed; j++)
				{
					if(found)
					{
						queue_size++;
						queue_amt += cap[queue[j]];
					}
					else if(queue[j] == node)
					{
						found = true;
						queue_size = 1;
						queue_amt = cap[queue[j]];
					}
				}
				amt += queue_amt * (R / queue_size);
				R = R % queue_size;
				memset(visited, 0, sizeof(visited));
			}
		}

		cout << "Case #" << i << ": " << amt << endl;
	}
	return 0;
}
