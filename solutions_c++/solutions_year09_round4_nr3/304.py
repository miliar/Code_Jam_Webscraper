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

int table[30][30];
int canCombine[1 << 16];
bool intersect[30][30];
int N, K;

bool isIntersect(int f, int s)
{
	for (int i = 0; i < K; i++)
	{
		if (table[f][i] == table[s][i])
			return true;

		if (i != K - 1)
		{
			if (table[f][i] >  table[s][i] && table[f][i + 1] < table[s][i + 1])
				return true;
			if (table[f][i] < table[s][i] && table[f][i + 1] > table[s][i + 1])
				return true;
		}
	}
	return false;
}

int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);
	//freopen("C:\\out", "w", stdout);

	int caseCount;
	cin >> caseCount;

	for (int nCase = 1; nCase <= caseCount; nCase++)
	{
		scanf("%d%d", &N, &K);

		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < K; j++)
				scanf("%d", &table[i][j]);
		}

		
		for (int i = 0; i <  N; i++)
		{
			for (int j = i + 1; j < N; j++)
			{
				intersect[j][i] = intersect[i][j] = isIntersect(i, j);
			}
			intersect[i][i] = false;
		}

		memset(canCombine, 60, sizeof(canCombine));
		canCombine[0] = 1;

		for (int i = 0; i < 1 << N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				if ((1 << j) & i)
				{
					int remain = i ^ (1 << j);

					bool valid = true;

					if (canCombine[remain] == 1)
					{
						for (int k = 0; k < N; k++)
						{
							if (k != j &&((1 << k) & i))
							{
								if (intersect[j][k])
								{
									valid = false;
									break;;
								}
							}
						}

						if (valid)
							canCombine[i] = 1;
					}
				}
			}

		}


		for (int i = 0; i < 1 << N; i++)
		{
			for (int j = i - 1; j != 0; j = (j - 1) & i)
			{
				canCombine[i] = min(canCombine[i], canCombine[j] + canCombine[i ^ j]);
			}
		}

		printf("Case #%i: %d\n", nCase, canCombine[(1 << N) - 1]);


		fflush(stdout);
	}


	return 0;
}


