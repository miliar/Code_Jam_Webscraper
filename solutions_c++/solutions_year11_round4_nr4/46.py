#include <cstdio>
#include <cstdlib>
#include <queue>
#include <cstring>

using namespace std;


int TRIALS;
char w_mat[400][400];
short w_list[400][2000];
int w_list_c[400];
short dist[400];
short threat[400*400*400];

void trial(int T)
{
	printf("Case #%d: ", T);
	
	int P; int W;
	memset(w_mat, 0, sizeof(w_mat));
	memset(w_list, 0, sizeof(w_list));
	memset(w_list_c, 0, sizeof(w_list_c));
	memset(dist, -1, sizeof(dist));
	memset(threat, -1, sizeof(threat));
	
	scanf("%d%d", &P, &W);
	for (int i = 0; i < W; i++)
	{
		int B; int E;
		scanf("%d,%d", &B, &E);
		w_mat[B][E] = 1;
		w_mat[E][B] = 1;
		w_list[E][w_list_c[E]++] = B;
		w_list[B][w_list_c[B]++] = E;
	}
	queue<long long> q;
	dist[0] = 0;
	q.push(0);
	while (!q.empty())
	{
		int cur = q.front(); q.pop();
		for (int i = 0; i < w_list_c[cur]; i++)
		{
			int n = w_list[cur][i];
			if (dist[n] < 0)
			{
				dist[n] = dist[cur] + 1;
				q.push(n);
			}
		}
	}
	
	int ans = 0;
	threat[0] = w_list_c[0];
	q.push(0);
	while (!q.empty())
	{
		long long cur = q.front(); q.pop();
		int c = cur % 400;
		for (int i = 0; i < w_list_c[c]; i++)
		{
			int n = w_list[c][i];
			if (dist[n] == dist[c] + 1)
			{
				if (n == 1 && ans < threat[cur])
					ans = threat[cur];
				int m = (cur / 400) % 400;
				long long next = (cur * 400 + n) % (400*400*400);
				int tnext = threat[cur] - 1;
				for (int j = 0; j < w_list_c[n]; j++)
					if (!w_mat[c][w_list[n][j]] && !w_mat[m][w_list[n][j]] && w_list[n][j] != c) tnext++;
				if (threat[next] < 0)
					q.push(next);
				if (threat[next] < tnext)
					threat[next] = tnext;
			}
		}
	}
	printf("%d %d\n", (int)dist[1] - 1, ans);
}

int main(int argc, char* argv[])
{
	scanf("%d", &TRIALS);
	for (int T = 1; T <= TRIALS; T++)
	{
		trial(T);
	}
	
	return 0;
}