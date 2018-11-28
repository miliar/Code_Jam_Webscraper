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


char p[1000];

int K, N;
char words[200][30];

const int CM = 101;
vector<vector<int> > Choose(CM, vector<int>(CM)); 

int mem[1 << 5][11];

int solve(char* next, int mask, int K)
{
	if (mem[mask][K] != -1)
		return mem[mask][K];


	if (K == 0)
	{
		return mem[mask][K] = mask == 0 ? 1 : 0;
	}

	int nextLen = strlen(next);
	assert(nextLen < 5);

	int res = 0;

	for (int i = 0; i < N; i++)
	{
		vector<int> terms(nextLen);
		
		for (int j = 0; j < nextLen; j++)
		{
			terms[j] = words[i][next[j] - 'a'];
		}

		for (int nmask = mask; ; nmask = (nmask - 1) & mask)
		{
			int c = 1;
			bool valid = true;

			for (int j = 0; j < nextLen; j++)
			{
				if ((mask & (1 << j)) == 0)
					continue;

				{
					if ((nmask & (1 << j)) == 0)
					{
						c = (c * terms[j]) % 10009;
					}
					else
					{
					}
				}
			}
			if (c)
			{
				res = (res + c * solve(next, nmask, K - 1)) % 10009;
			}
			if (nmask == 0)
				break;
		}
	}
	return mem[mask][K] = res;
}


int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);
	//freopen("C:\\out", "w", stdout);

	for( int i = 0; i < CM; ++i ) 
	{ 
		Choose[i][0] = 1; 
		for( int j = 1; j <= i; ++j ) 
			Choose[i][j] = ( Choose[i-1][j-1] + Choose[i-1][j] )% 10009; 
	}


	int caseCount;
	scanf("%d", &caseCount);

	for (int nCase = 1; nCase <= caseCount; nCase++)
	{
		scanf("%s%d", p, &K);

		scanf("%d", &N);

		memset(words, 0, sizeof(words));
		
		for (int i = 0; i < N; i++)
		{
			char w[1000];
			scanf("%s", w);
			for (int j = 0; j < strlen(w); j++)
				words[i][w[j] - 'a']++;
		}

		printf("Case #%i:", nCase);

		for (int i = 1; i <= K; i++)
		{

			int len = strlen(p);
			int j = 0;
			int res = 0;
			char* next = p;

			while (j < len)
			{
				while (j < len)
				{
					if (p[j] == '+')
						break;
					j++;
				}
				bool pl = p[j] == '+';
				p[j] = 0;

				memset(mem, -1, sizeof(mem));

				int res2 = solve(next, (1 << strlen(next)) - 1, i);
				res = (res + res2)% 10009;

				if (pl) p[j] = '+';

				j++;
				next = p + j;

			}
			printf(" %i", res);
		}
		printf("\n");
		

		fflush(stdout);
	}
 

	return 0;
}


