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

char table[21][21];

string mem[20][20][1000];

struct State
{
	int r, c;
	int val;
	string cur;

	string& ref() {return mem[r][c][val + 500];}
};

int dx[] = {1, 0, -1, 0, 1, 1, -1, -1};
int dy[] = {0, -1, 0, 1, 1, -1, -1, 1};

int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);
	//freopen("C:\\out", "w", stdout);

	int caseCount;
	scanf("%d", &caseCount);

	for (int nCase = 1; nCase <= caseCount; nCase++)
	{
		int W, Q;
		scanf("%d%d", &W, &Q);

		for (int i = 0; i < W; i++)
			scanf("%s", table[i]);

		printf("Case #%i:\n", nCase);

		while (Q--)
		{
			int N;
			scanf("%d", &N);

			for (int i = 0; i < W; i++)
			{
				for (int j = 0; j < W; j++)
				{
					for (int k = 0; k < 1000; k++)
					{
						mem[i][j][k] = "";
					}
				}
			}

			queue<State> q;

			for (int i = 0; i < W; i++)
			{
				for (int j = 0; j < W; j++)
				{
					if (isdigit(table[i][j]))
					{
						State s = {i, j, table[i][j] - '0', string(1, table[i][j])};
						s.ref() = s.cur;

						q.push(s);
					}
				}
			}

			string ans;

			while (!q.empty())
			{
				State s = q.front();
				q.pop();

				if (s.val == N)
				{
					if (ans == "" || ans.size() > s.cur.size() || 
						(ans.size() == s.cur.size() && ans > s.cur))
					{
						ans = s.cur;
					}
					continue;
				}
				if (ans != "" && ans.size() < s.cur.size())
					continue;
				
				for (int ss = 0; ss < 4; ss++)
				{		
					if (s.r + dy[ss] < 0 || s.c + dx[ss] < 0 || s.r + dy[ss] >= W ||  s.c + dx[ss] >= W)
						continue;

					char sign = table[s.r + dy[ss]][s.c + dx[ss]];

					for (int k = 0; k < 4; k++)
					{
						State ns = s;
						ns.r += dy[ss] + dy[k];
						ns.c += dx[ss] + dx[k];

						if (ns.r < 0 || ns.c < 0 || ns.r >= W || ns.c >= W)
							continue;

						ns.cur += sign;
						ns.cur += table[ns.r][ns.c];
						int v = table[ns.r][ns.c] - '0';
						if (sign == '-')
							v = -v;
						ns.val += v;
						if (abs(ns.val) > 500)
							continue;

						string& ans = ns.ref();
						if (ans == "" || ans.size() > ns.cur.size() || 
							(ans.size() == ns.cur.size() && ans > ns.cur))
						{
							q.push(ns);
							ans = ns.cur;
						}
					}
				}
			}

			printf("%s\n", ans.c_str());
		} 


		fflush(stdout);
	}


	return 0;
}


