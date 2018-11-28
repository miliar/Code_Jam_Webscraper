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


inline void checkMin(int& a, int b)
{
	if (a > b) a = b;
}
inline void checkMin(ll& a, ll b)
{
	if (a > b) a = b;
}

int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);

	int T;
	scanf("%d", &T);

	for (int nTest = 1; nTest <= T; nTest++)
	{		
		int N;
		scanf("%d", &N);

		map<int, int> m;
		rep(i, N)
		{
			int x, K;
			scanf("%d %d", &x, &K);

			m[x] += K;
		}

		int res = 0;

		while (true)
		{
			map<int, int> next;
			bool found = false;

			for (map<int, int>::iterator i = m.begin(); i != m.end(); i++)
			{
				if (i->second < 2)
				{
					next[i->first] += i->second;
				}
				else
				{
					int cnt = i->second / 2;

					if (i->second - 2 * cnt != 0)
						next[i->first] += 1;

					next[i->first + 1] += cnt;
					next[i->first - 1] += cnt;

					found = true;
					res+= cnt;
				}
			}
			if (!found)
				break;

			m = next;
		}


		printf("Case #%d: %d\n", nTest, res);
		
		fflush(stdout);
	} 


	return 0;
}


