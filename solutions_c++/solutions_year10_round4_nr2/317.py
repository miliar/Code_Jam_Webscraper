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
#include <memory.h>

using namespace std; 

#define rep(i,n) for(int i=0;i<(n);++i)
#define clr(a,b) memset(a,b,sizeof(a)); 
#define all(c) (c).begin(), (c).end() 
#define inf 1000000000 

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;

int price[11][1 << 10];
int M[1 << 10];
int haveSee[1 << 10];

int solve(int from, int to)
{
	int res = 0;

	bool found = false;
	for (int i = from; i < to; i++)
	{
		if (haveSee[i] > 0)
		{
			found = true;
		}
	}

	if (found)
	{
		res++;

		for (int i = from; i < to; i++)
		{
			haveSee[i]--;
		}

		if (from + 1 != to)
		{
			res += solve(from, (from + to) / 2) + solve((from + to) / 2, to);
		}
	}
	return res;
}

int main(int argc, char* argv[])
{
//#ifdef _DEBUG
	freopen("Test.in", "r", stdin);
//#endif

	int T;
	scanf("%d", &T);


	for (int nTest = 1; nTest <= T; nTest++)
	{		
		int P;
		scanf("%d", &P);

		int N = 1 << P;

		for (int i = 0; i < N; i++)
			scanf("%d", &M[i]);

		for (int j = 0; j < P; j++)
		{
			for (int i = 0; i < 1 << (P  - 1 - j); i++)
			{
				scanf("%d", &price[j][i]);
			}
		}

		for (int i = 0; i < N; i++)
			haveSee[i] = P - M[i];

		int res = solve(0, N);

		printf("Case #%d: %d\n", nTest, res);
		fflush(stdout);
	} 


	return 0;
}


