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

vector<int> table;

int solve(int row)
{
	if (row == table.size() - 1)
		return 0;

	int res = 0;
	for (int i = row; i < table.size(); i++)
	{
		if (table[i] <= row)
		{
			if (i != row)
			{
				int c = table[i];
				table.erase(table.begin() + i);
				table.insert(table.begin() + row, c);
			}

			return i - row + solve(row + 1);
		}
	}
	assert (false);

	return 0;
} 

char s[100];

int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);
	//freopen("C:\\out", "w", stdout);

	int caseCount;
	cin >> caseCount;

	for (int nCase = 1; nCase <= caseCount; nCase++)
	{
		int N;
		scanf("%d", &N);

		table.resize(N);
		
		for (int i = 0; i < N; i++)
		{
			scanf("%s", s);

			table[i] = 0;
			for (int j = N - 1; j >= 0; j--)
			{
				if (s[j] == '1')
				{
					table[i] = j;
					break;
				}
			}
		}

		int res = solve(0);

		printf("Case #%i: %d\n", nCase, res);
		fflush(stdout);
	}


	return 0;
}


