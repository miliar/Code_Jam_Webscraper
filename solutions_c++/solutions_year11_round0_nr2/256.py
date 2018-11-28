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

char reaction[130][130];
bool opposite[130][130];

char s[2000];

int main(int argc, char* argv[])
{
#ifndef ONLINE_JUDGE
	freopen("test.in", "r", stdin);
#endif
	int T;
	scanf("%d", &T);

	for (int nTest = 1; nTest <= T; nTest++)
	{		

		memset(reaction, 0, sizeof(reaction));
		memset(opposite, 0, sizeof(opposite));
		
		int C;
		scanf("%d", &C);

		while (C--)
		{
			scanf("%s", s);
			assert (strlen(s) == 3);

			reaction[s[0]][s[1]] = s[2];
			reaction[s[1]][s[0]] = s[2];
		}

		int D;
		scanf("%d", &D);

		while (D--)
		{
			scanf("%s", s);
			assert (strlen(s) == 2);

			opposite[s[0]][s[1]] = opposite[s[1]][s[0]] = true;
		}

		int N;
		scanf("%d", &N);

		scanf("%s", s);
		assert (strlen(s) == N);

		string res;

		for (int i = 0; i < N; i++)
		{
			res += s[i];

			while (res.size() >= 2 && reaction[res[res.size() - 1]][res[res.size() - 2]])
			{
				char c = reaction[res[res.size() - 1]][res[res.size() - 2]];
				
				res.resize(res.size() - 2);
				res += c;
			}


			for (int j = 0; j < (int)res.size() - 1; j++)
			{
				if (opposite[res[j]][res[res.size() - 1]])
				{
					res.clear();
					break;
				}
			}
		}

	
		printf("Case #%d: [", nTest);
		for (int i = 0; i < res.size(); i++)
		{
			if (i) printf(", ");
			putchar(res[i]);
		}
		printf("]\n");

		fflush(stdout);
	} 


	return 0;
}


