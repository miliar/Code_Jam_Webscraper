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

char s[100001];

void parse(char* s, set<string>& res)
{
	int len = strlen(s);

	res.insert(s);

	for (int i = len - 1; i >= 1;i--)
	{
		
		if (s[i] == '/')
		{
			s[i] = 0;
			res.insert(s);
		}
	}
}

int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);

	int nTestCount;
	scanf("%d", &nTestCount);

	for (int nTest = 1; nTest <= nTestCount; nTest++)
	{
		int N, M;
		scanf("%d %d", &N, &M);

		set<string> exists, need;
		exists.insert("/");

		rep(i, N)
		{
			scanf("%s", s);

			parse(s, exists);
		}

		rep(i, M)
		{
			scanf("%s", s);

			parse(s, need);
		}

		int res = 0;
		for (set<string>::iterator i = need.begin(); i!= need.end(); i++)
		{
			if (exists.find(*i) == exists.end())
				res++;
		}


		printf("Case #%d: %d\n", nTest, res);
		fflush(stdout);
	}


	return 0;
}


