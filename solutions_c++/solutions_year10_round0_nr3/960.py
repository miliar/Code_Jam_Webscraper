#include <cstdio>
#include <cstring>
#include <queue>

using namespace std;

int R, k, N;
queue<int> g;

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("Csmall.txt", "w", stdout);
	int T;
	int i, j;
	scanf("%d", &T);
	for(int tt = 1; tt <= T; tt++)
	{
		scanf("%d%d%d", &R, &k, &N);
		while(!g.empty()) 
			g.pop();
		for(i = 0; i < N; i++)
		{
			scanf("%d", &j);
			g.push(j);
		}
		
		int ret = 0;
		for(i = 0; i < R; i++)
		{
			queue<int> out;
			int sum = 0;
			while(!g.empty())
			{
				if(sum + g.front() > k)
					break;
				sum += g.front();
				out.push(g.front());
				g.pop();
			}
			ret += sum;
			while(!out.empty())
			{
				g.push(out.front());
				out.pop();
			}
		}	
		printf("Case #%d: %d\n", tt, ret);
	}

	
	return 0;
}