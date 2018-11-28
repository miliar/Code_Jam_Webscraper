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

long long table[60];

int mem[60][60][ 1<< 7][1 << 7];

struct State
{
	int y, x, curRow, nextRow;

	int& ref() { return mem[y][x][curRow][nextRow];}
};

char s[100];


int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);
	//freopen("C:\\out", "w", stdout);

	int caseCount;
	cin >> caseCount;

	for (int nCase = 1; nCase <= caseCount; nCase++)
	{
		int N, K, F;
		scanf("%d%d%d", &N, &K, &F);

		for (int i = 0; i < N; i++)
		{
			table[i] = 0;
			scanf("%s", s);
			
			for (int j = 0; j < K; j++)
			{
				if (s[j] == '#')
					table[i] |= 1 << j;
			}
		}
		N++;
		table[N - 1] = 1023;

		queue<State> q;
		State start = {0, 0, table[0], table[1]};
		q.push(start);

		memset(mem, 60, sizeof(mem));
		start.ref() = 0;

		int res = INT_MAX;

		while (!q.empty())
		{
			State s = q.front();
			q.pop();

			if (s.y == N - 2)
			{
				res = min(res, s.ref());
				continue;
			}

			if (s.x != K - 1 && (s.curRow & (1 << (s.x + 1))) == 0)
			{
				 if (s.nextRow & (1 << (s.x + 1)))
				 {
					 {

						 State ns = {s.y, s.x + 1, s.curRow, s.nextRow};

						 if (ns.ref() > s.ref())
						 {
							 ns.ref() = s.ref();
							 q.push(ns);
						 }
					 }

					 State ns = {s.y, s.x, s.curRow, s.nextRow ^ (1 << (s.x + 1))};

					 if (ns.ref() > 1 + s.ref())
					 {
						 ns.ref() = 1 + s.ref();
						 q.push(ns);
					 }

				 }
				 else
				 {
					 int nextRow = s.y + 1;
					 while(nextRow < N && (table[nextRow + 1] & (1 << (s.x + 1))) == 0 )
					 {
						 nextRow++;
					 }
					 if (nextRow - s.y <= F)
					 {
						 State ns = {nextRow, s.x + 1, nextRow == s.y + 1 ? s.nextRow : table[nextRow], table[nextRow + 1]};

						 if (ns.ref() > s.ref())
						 {
							 ns.ref() = s.ref();
							 q.push(ns);
						 }
					 }
				 }				 
			}

			if (s.x != 0 && (s.curRow & (1 << (s.x - 1))) == 0)
			{
				if (s.nextRow & (1 << (s.x - 1)))
				{
					{

						State ns = {s.y, s.x - 1, s.curRow, s.nextRow};

						if (ns.ref() > s.ref())
						{
							ns.ref() = s.ref();
							q.push(ns);
						}
					}

					State ns = {s.y, s.x, s.curRow, s.nextRow ^ (1 << (s.x - 1))};

					if (ns.ref() > 1 + s.ref())
					{
						ns.ref() = 1 + s.ref();
						q.push(ns);
					}

				}
				else
				{
					int nextRow = s.y + 1;
					while(nextRow < N && (table[nextRow + 1] & (1 << (s.x - 1))) == 0 )
					{
						nextRow++;
					}
					if (nextRow - s.y <= F)
					{
						State ns = {nextRow, s.x - 1, nextRow == s.y + 1 ? s.nextRow : table[nextRow], table[nextRow + 1]};

						if (ns.ref() > s.ref())
						{
							ns.ref() = s.ref();
							q.push(ns);
						}
					}
				}				 
			}

		}
		
		if (res == INT_MAX)		
			printf("Case #%i: No\n", nCase);
		else
			printf("Case #%i: Yes %d\n", nCase, res);

		fflush(stdout);
	}


	return 0;
}


