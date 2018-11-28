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

int v[1000];
int N;

double solve(int N);

double mem[1001];
double mem2[1001];

double solveTail(int N)
{
	if (N <= 1)
		return 0;

	if (mem2[N] > -0.5)
		return mem2[N];

	double total = 0;
	for (int i = 1; i <= N; i++)
	{
		total += 1.0 / N * (solve(i) + solveTail(N - i));
	}
	return mem2[N] = total;
}
double solve(int N)
{
	if (N <= 1)
		return 0;

	if (mem[N] > -0.5)
		return mem[N];

	double res = 0;

	for (int i = 1; i < N; i++)
	{
		res += 1.0 / N * (solve(i) +  solveTail(N - i));
	}

	return mem[N] = (1.0 + res) / (1.0 - 1.0 / N);
}


int main(int argc, char* argv[])
{
#ifndef ONLINE_JUDGE
	freopen("test.in", "r", stdin);
#endif
	int T;
	scanf("%d", &T);

	for (int i = 0; i <= 1000; i++)
		mem[i] = -1;
	for (int i = 0; i <= 1000; i++)
		mem2[i] = -1;



	for (int nTest = 1; nTest <= T; nTest++)
	{		
		scanf("%d", &N);
		int K = 0;

		for (int i = 0; i < N; i++)
		{
			scanf("%d", v + i);
			v[i]--;
		}

		vector<int> vis(N);
		double res = 0;

		for (int i = 0; i < N; i++)
		{
			if (vis[i])
				continue;

			int C = 0;
			int j = i;
			while (!vis[j])
			{
				vis[j] = true;
				C++;
				j = v[j];
			}

			res += solve(C);
		}

		printf("Case #%d: %.6lf\n", nTest, res);
	}

	return 0;
}


