#include <assert.h> 
#include <ctype.h> 
#include <float.h> 
#include <math.h> 
#include <stdio.h> 
#include <string> 
#include <stdlib.h> 
#include <time.h> 
#include <algorithm> 
#include <numeric> 
#include <functional> 
#include <utility> 
#include <vector> 
#include <list> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <sstream> 
#include <iostream> 

using namespace std; 

#define rep(i,n) for(int i=0;i<(n);++i)
#define clr(a,b) memset(a,b,sizeof(a)); 
#define all(c) (c).begin(), (c).end() 
#define inf 1000000000 

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;

char table[20][20];
int N, M;

int dx[] = {1, 0, -1, 0};
int dy[] = {0, -1, 0, 1};

bool isStable(vector<int>& box)
{
	vector<int> vis(box.size());

	queue<int> q;
	q.push(box[0]);
	vis[0] = true;
	while (!q.empty())
	{
		int b = q.front();
		q.pop();

		int r = b / M;
		int c = b % M;

		for (int k = 0; k < 4; k++)
		{
			int nr = r + dy[k];
			int nc = c + dx[k];

			for (int j = 0; j < box.size(); j++)
			{
				if (box[j] == nr * M + nc && !vis[j])
				{
					vis[j] = true;
					q.push(nr * M + nc);
				}
			}
		}


	}

	for (int i = 0; i < vis.size(); i++)
		if (!vis[i])
			return false;
	
	return true;
}

int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);
	//freopen("C:\\out", "w", stdout);

	int caseCount;
	scanf("%d", &caseCount);

	for (int nCase = 1; nCase <= caseCount; nCase++)
	{
		scanf("%d%d", &N, &M);

		for (int i = 0; i < N; i++)
		{
			scanf("%s", table[i]);
		}

		vector<int> goals;
		vector<int> box;

		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				if (table[i][j] == 'x' || table[i][j] == 'w')
				{
					goals.push_back(i * M + j);
				}

				if (table[i][j] == 'o' || table[i][j] == 'w')
				{
					box.push_back(i * M + j);
				}

				if (table[i][j] != '#')
					table[i][j] = '.';
			}
		}
		assert(goals.size() == box.size());

		sort(all(goals));
		sort(all(box));

		queue<vector<int> > q;
		q.push(box);
		
		map<vector<int>, int> mem;
		mem[box] = 0;

		int ans = -1;

		while (!q.empty())
		{
			vector<int> box = q.front();
			q.pop();
			
			int move = mem[box];
			bool stable = isStable(box);

			if (box == goals)
			{
				ans = move;
				break;
			}

			for (int i = 0; i < box.size(); i++)
			{
				int r = box[i] / M;
				int c = box[i] % M;

				table[r][c] = '#';
			}

			for (int i = 0; i < box.size(); i++)
			{
				int r = box[i] / M;
				int c = box[i] % M;

				for (int k = 0; k < 4; k++)
				{
					int nr = r + dy[k];
					int nc = c + dx[k];

					if (nr < 0 || nc < 0 || nr >= N || nc >= M)
						continue;
					if (table[nr][nc] != '.')
						continue;

					int nr2 = r + dy[(k + 2) % 4];
					int nc2 = c + dx[(k + 2) % 4];

					if (nr2 < 0 || nc2 < 0 || nr2 >= N || nc2 >= M)
						continue;
					if (table[nr2][nc2] != '.')
						continue;

					vector<int> nbox = box;
					nbox[i] = nr2 * M + nc2;
					sort(all(nbox));

					bool s = isStable(nbox);

					if (!s && !stable)
						continue;

					if (mem.find(nbox) == mem.end())
					{
						mem[nbox] = move + 1;
						q.push(nbox);
					}
				}
			}

			for (int i = 0; i < box.size(); i++)
			{
				int r = box[i] / M;
				int c = box[i] % M;

				table[r][c] = '.';
			}
		}

		printf("Case #%i: %i\n", nCase, ans);
		fflush(stdout);
	}
 

	return 0;
}


